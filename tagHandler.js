/**
 * Created by Kevin Zhang on 2017-01-26.
 */

var tagList = {};

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


function retrieveLabels(boards) {
    tagList = []
    boards.forEach(function(board) {
        Trello.get('/boards/'+board['id']+'/cards?fields=labels', function(response) {
            response.forEach(function(card) {
                card["labels"].forEach(function(label) {
                    tagList[label['id']] = label['name']
                })
            })
        }, function(response) {
            console.log("Error Retrieving Labels")
        });
    })
    console.log(tagList);
}

function retrieveTags() {
    Trello.get('/member/me/boards?fields=id', function(response) {
        retrieveLabels(response);
    }, function() {
        console.log("Error Retrieving Tags");
    });
}

$(document).ready(function() {
    Trello.authorize({
      type: 'popup',
      name: 'TrelloSync Login',
      scope: {
        read: 'true',
        write: 'true' },
      expiration: 'never',
      success: function(response) {
          $("#login").remove();
          retrieveTags();
      },
      error: function(response) {
          console.log("Error");
      }
    });
    /*
    displayTags(tagList);
    $("#tags").on("click", ".tag-unique", function() {
        $(this).closest(".tag-group").children(".group-by").html("<span class='group-by-button' onclick='groupBy(this)'>Group by: "+$(this).html()+"</span>");
    })
    */
})