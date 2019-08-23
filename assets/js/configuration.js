jQuery(document).ready(function(){
    const receive = jQuery("#receive_email");  


    jQuery("#pswitch").on('change',function(){
        let switchOn = jQuery(this).is(":checked");
        if(switchOn){
            receive.attr("value","1");
        }else{
            receive.attr("value","0");
        }
    });
});