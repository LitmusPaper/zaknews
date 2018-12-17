$(document).ready(function(){



    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
      }
    $('#subcomment').click(function(e){
        e.preventDefault();
        var form=$('#comment');
        form.submit();
        var button = $(this);
        var input = form.find("#content");
        input.val('');
        button.prop('disabled', true);
        
    });
});