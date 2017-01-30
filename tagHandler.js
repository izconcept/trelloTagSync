/**
 * Created by IzKevin on 2017-01-26.
 */

var tagList = [["Bug", "bugs", "bog"],["product launch", "Product-launch", "launch product"],["error", "erreur"]];

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


function groupBy(tag) {
    
}

$(document).ready(function() {
    displayTags(tagList);
    $("#tags").on("click", ".tag-unique", function() {
        $(this).closest(".tag-group").children(".group-by").html("<span class='group-by-button' onclick='groupBy(this)'>Group by: "+$(this).html()+"</span>");
    })
})