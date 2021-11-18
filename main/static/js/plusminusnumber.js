$(function() {
    $('.btn-number').click(function (e){
        e.preventDefault();
        fieldName = $(this).attr('data-field');
        type = $(this).attr('data-type');
        var input = $("input[name='" + fieldName + "']");
        var curentVal = parseInt(input.val());
        if (type == 'minus') {
            if (curentVal > input.attr('min')) {
                input
                    .val(curentVal -1)
                    .change();
            }
            if (parseInt(input.val()) == input.attr('min')) {
                $(this).attr('disabled', true);
            }
        }else if (type == 'plus') {
            if (curentVal < input.attr('max')) {
                input
                    .val(curentVal + 1)
                    .change();
            }
            if (parseInt(input.val()) ==input.attr('max')) {
                $(this).attr('disabled' ,true);
            }
        }
    });
});