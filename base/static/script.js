// function clearSearchHint(input) {
//     if (input.value === "Search") {
//         input.value = "";
//     }
// }

// function restoreSearchHint(input) {
//     if (input.value === "") {
//         document.getElementById("search-form").submit();
//     }
// }

// document.addEventListener("DOMContentLoaded", function() {
//     const searchInput = document.getElementById("search-input");
//     searchInput.addEventListener("keydown", function(event) {
//         if (event.key === "Enter") {
//             document.getElementById("search-form").submit();
//         }
//     });
// });
$(document).ready(function() {
    $('#search-input').on('input', function() {
        var query = $(this).val();
        $.ajax({
            url: '{% url "search-tasks" %}',
            type: 'GET',
            data: {
                search: query
            },
            success: function(response) {
                $('#task-list').html(response);
            }
        });
    });
});