var otp_from_back="";
    function ajax_send_otp(){
       document.getElementById("email_div").style.display='none';
       email = document.getElementById("email");
     $.post("/send_otp",
         {
             "email":email.value,
             "csrfmiddlewaretoken":"{{csrf_token}}"
         },
         function(data, status){
             if(status=="success"){
                 otp_from_back = data;
                 document.getElementById("otp_div").style.display='block';
                 }
    }
    );
    }
   function verify_otp(){
       var user_otp=document.getElementById("otp").value;
       if (user_otp==otp_from_back){
           document.getElementById("verify_text_div").style.color="green";            
           document.getElementById("verify_text_div").innerHTML="OTP Verified";
           document.getElementById("otp_div").style.display="none";
           document.getElementById("form_div").style.display="block";
       }
       else{
           document.getElementById("verify_text_div").style.color="red";
           document.getElementById("verify_text_div").innerHTML="Try Again!!";
       }
   }