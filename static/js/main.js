function spam(id){

    let values = {
        "chat_id": id,
        "count": $("input[name=count]").val(),
        "msg": $("input[name=msg]").val(),
    }
    
    $.get({
        url: '/spam',
        data: values,
        cache: false
    }).then(function(data){
    });

}
    