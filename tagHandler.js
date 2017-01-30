/**
 * Created by Kevin Zhang on 2017-01-26.
 */

var tagList = {};
var cardList = {};

function displayTags(tag) {
    for(var i = 0; i < tag.length; i++) {
        $("#tags").append("<div class='tag-group' id='group-"+i+"'></div>");
        tag[i].forEach(function(uniqueTag) {
            console.log(uniqueTag)
            $("#group-"+i).append("<span class='tag-unique'>"+uniqueTag+"</span>");
        })
        if(tag[i].length > 1) {
            $("#group-"+i).append("<p class='group-by' id='group-by-'"+i+"></p>");
        }
    }
}

function combineAndRemoveTags(IDtoReplace, cluster) {
    Object.keys(cardList).forEach(function (cardID) {
        cardList[cardID].forEach(function(labelID) {
            if(cluster[labelID]) {
                Trello.post('/cards/'+cardID+'/idLabels/',{value: IDtoReplace},
                    function(response) {
                        console.log("Tag added: " + response);
                    }, function(response) {
                            console.log("Error:" + response)
                    });
                Trello.delete('/cards/'+cardID+'/idLabels/',{value: labelID},
                    function(response) {
                        console.log("Tag deleted: " + response);
                    }, function(response) {
                        console.log("Error: " + response);
                    });
            }
        });
    });
}


function retrieveLabels(boards) {
    boards.forEach(function(board) {
        Trello.get('/boards/'+board['id']+'/cards?fields=labels', function(response) {
            response.forEach(function(card) {
                cardList[card['id']] = [];
                card["labels"].forEach(function(label) {
                    tagList[label['id']] = label['name'];
                    cardList[card['id']].push(label['id']);
                })
            })
        }, function(response) {
            console.log("Error Retrieving Labels")
        });
    })
}

function retrieveTags() {
    Trello.get('/member/me/boards?fields=id', function(response) {
        retrieveLabels(response);
    }, function() {
        console.log("Error Retrieving Tags");
    });
}

function authorize() {
    Trello.authorize({
      type: 'popup',
      name: 'TrelloSync Login',
      scope: {
        read: 'true',
        write: 'true' },
      expiration: 'never',
      success: function(response) {
          console.log("Authenticated Succesfully");
          retrieveTags();
      },
      error: function(response) {
          if($("#login").length < 1) {
              $(".container").append('<p id="loginFailure">Login failed please try again</p>')
              $(".container").append('<span id="login" onclick="authorize()">Login</span>')
          }
          console.log("Error");
      }
    });
}
$(document).ready(function() {
    authorize();
    //displayTags(tagList);
    $("#tags").on("click", ".tag-unique", function() {
        $(this).closest(".tag-group").children(".group-by").html("<span class='group-by-button' onclick='groupBy(this)'>Group by: "+$(this).html()+"</span>");
    })

})