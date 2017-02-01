#!/usr/bin/env python

print """
var cardList = {};
var tagCluster;

$(document).ready(function() {
    //Call login script
    authorize();
    $(".container").on("click", ".tag-unique", function() {
        var id = $(this).data("tagid");
        var clusterNumber = $(this).data("group");
        name = "kevin"
        text = "das"
        //alert("<a href='javascript:void(0)' onClick='showField(\'" + name + "\',\'" + text + "\');'>Edit</a>");
        $(this).closest(".tag-group").children(".group-by").html("<span class='group-by-button' onclick='combineAndRemoveTags(&quot;" + id + "&quot;,"+clusterNumber+")'>Group by: "+$(this).html()+"</span>");
    })

})

//Loginflow: Determines if the user is already authenticated or needs to login.
//If login succesful, executes retrieveTags() which makes the necessary API calls to return a set of labels
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

//Makes the necessary API calls to retrieve all the labels from the user
function retrieveTags() {
    Trello.get('/member/me/boards?fields=id', function(boards) {
        var dataString = "";
        var tagList = {};
        boards.forEach(function(board) {
            Trello.get('/boards/'+board['id']+'/cards?fields=labels', function(response) {
                var counter = 0;
                response.forEach(function(card) {
                    counter++;
                    cardList[card['id']] = [];
                    card["labels"].forEach(function(label) {
                        if(!tagList[label['id']]){
                            dataString += label['id'] + "=" + label['name'] + "&";
                        }
                        tagList[label['id']] = label['name']
                        cardList[card['id']].push(label['id']);
                        if(counter == 10) {
                            generateTagClusters(dataString);
                        }
                    });
                })
            }, function(response) {
                console.log("Error Retrieving Labels: " + response)
            });
        });
    }, function(error) {
        console.log("Error Retrieving Tags: "+error);
    });
}

//Given a tag ID, replaces all the closest tags with the new one
function combineAndRemoveTags(IDtoReplace, clusterNumber) {
    var cluster = tagCluster[clusterNumber];
    Object.keys(cardList).forEach(function (cardID) {
        cardList[cardID].forEach(function(labelID) {
            if(cluster[labelID] && labelID != IDtoReplace) {
                console.log("Removed: " + labelID);
                console.log("Added: " + IDtoReplace);
                /*
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
                    */
            }
        });
    });
}

//Calls python clustering functionality
function generateTagClusters(dataString) {
    console.log(dataString)
    $.ajax({
        url: "groupTags.py",
        type: "POST",
        data: dataString,
        success: function(response) {
            console.log("SUCCESS");
            tagCluster = response;
            console.log(response);
            displayTags(response);
        },
        error: function(response) {
            console.log("ERROR");
            console.log(response);
        }
    })
}

function displayTags(tag) {
    $(".container").append('<h1 class="lead">Grouped tags</h1><div id="tags"></div>')
    for(var i = 0; i < tag.length; i++) {
        $("#tags").append("<div class='tag-group' id='group-"+i+"'></div>");
        Object.keys(tag[i]).forEach(function(id) {
            $("#group-"+i).append("<span class='tag-unique' data-group='"+i+"' data-tagid='"+id+"'>"+tag[i][id]+"</span>");
        })
        if(Object.values(tag[i]).length > 1) {
            $("#group-"+i).append("<p class='group-by' id='group-by-'"+i+"></p>");
        }
    }
}
"""