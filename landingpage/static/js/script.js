$(document).ready(function() {
    // Handle change events for radio buttons and checkboxes using event delegation
    $(document).on('change', '.js-check :radio, .js-check :checkbox', function () {
        var $parent = $(this).closest('.js-check');
        if ($(this).is(':checked')) {
            $parent.addClass('active');
        } else {
            $parent.removeClass('active');
        }
    });

    // Initialize tooltips only if elements with data-toggle="tooltip" exist
    var $tooltipElements = $('[data-toggle="tooltip"]');
    if ($tooltipElements.length > 0) {
        $tooltipElements.tooltip();
    }

    // Add event listeners for collapsible elements
    var collapsibles = document.getElementsByClassName("collapsible");
    for (var i = 0; i < collapsibles.length; i++) {
        collapsibles[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    }
});
