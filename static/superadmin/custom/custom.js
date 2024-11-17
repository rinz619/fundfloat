function restrictAlphabets(e){
       var x = e.which || e.keycode;
   	if((x>=48 && x<=57))
   		return true;
   	else
   		return false;
   }

 $("#message_div").fadeOut(3000);

function delete_modal(id){
    $("#hid").val(id);
    $("#modaldemo5").modal('show');
}

function modal_add(id){
    $("#hid").val(id);
    $("#modalAdd").modal('show');
}


function filtercourse(data) {
  var page = '1'
    if(data != 'None'){
      page=data
    }


//    var search = $('#searchkey').val()
    var status = $('#status').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }


 function coursestatus(id,vl) {

      page=$("#page").val();


//    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,vl:vl,type:1},

      success: function(data) {

       $(".table-responsive").html(data.template)


      }
  });
  }


 function coursedelete() {

      page=$("#page").val();
      id=$("#hid").val();


//    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,type:2},

      success: function(data) {
        $("#modaldemo5").modal('hide');

       $(".table-responsive").html(data.template)


      }
  });
  }


 function levelcontentdelete() {


      id=$("#hid").val();


    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {id:id},

      success: function(data) {
        $("#modaldemo5").modal('hide');

       $("#coursecontent").html(data.template)


      }
  });
  }





 function skillteststatus(id,vl) {

      page=$("#page").val();


    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,vl:vl,type:9},

      success: function(data) {

       $(".table-responsive").html(data.template)


      }
  });
  }



 function levelstatus(id,vl) {

      page=$("#page").val();


    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,vl:vl,type:1},

      success: function(data) {

       $(".table-responsive").html(data.template)


      }
  });
  }



function filterlevel(data) {
  var page = '1'
    if(data != 'None'){
      page=data
    }


    var search = $('#searchkey').val()
    var status = $('#status').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,search:search},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }



function filterlevelquestion(data) {
  var page = '1'
    if(data != 'None'){
      page=data
    }


    var search = $('#searchkey').val()
    var status = $('#status').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,search:search},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }




 function levelquestionstatus(id,vl) {

      page=$("#page").val();


    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,vl:vl,type:1},

      success: function(data) {

       $(".table-responsive").html(data.template)


      }
  });
  }


 function levelquestiondelete() {

      page=$("#page").val();
      id=$("#hid").val();


    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,type:2,search:search},

      success: function(data) {
        $("#modaldemo5").modal('hide');

       $(".table-responsive").html(data.template)


      }
  });
  }


 function leveldelete() {

      page=$("#page").val();
      id=$("#hid").val();


    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,type:2,search:search},

      success: function(data) {
        $("#modaldemo5").modal('hide');

       $(".table-responsive").html(data.template)


      }
  });
  }



 function studymaterialdelete() {


      id=$("#hid").val();


    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {id:id},

      success: function(data) {
        $("#modaldemo5").modal('hide');

       $("#study-table").html(data.template)


      }
  });
  }


function setcount(){
    var cnt = $("#qcount").val();
    var time = $("#time").val();
    var passmark = $("#passmark").val();
    var summernote = $("#summernote").val();



    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {cnt:cnt,type:5,time:time,summernote:summernote,passmark:passmark},

      success: function(data) {
      $("#exammodel").modal('hide');
        $(".table-responsive").html(data.template)

      }
  });
}




function filtersubadmins(data) {
  var page = '1'
    if(data != 'None'){
      page=data
    }


    var search = $('#searchkey').val()
    var status = $('#status').val()
    var admintype = $('#admintype').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,search:search,admintype:admintype},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }




 function subadminstatus(id,vl) {

      page=$("#page").val();


    var search = $('#searchkey').val()
    var status = $('#status').val()
        var admintype = $('#admintype').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,vl:vl,type:1,admintype:admintype},

      success: function(data) {

       $(".table-responsive").html(data.template)


      }
  });
  }


 function subadmindelete() {

      page=$("#page").val();
      id=$("#hid").val();


    var search = $('#searchkey').val()
    var status = $('#status').val()
    var admintype = $('#admintype').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,type:2,admintype:admintype},

      success: function(data) {
        $("#modaldemo5").modal('hide');

       $(".table-responsive").html(data.template)


      }
  });
  }

function getlevels(id){
    $.ajax({
      url: '/superadmin/getlevels',
      type: 'GET',
      data: {id:id},

      success: function(data) {

        console.log(data);
        $("#levels").empty();
        $("#levels").append('<option value="">Select</option>');
        for(i=0;i<data.levels.length;i++){
            $("#levels").append('<option value="'+data.levels[i].id+'">'+data.levels[i].title+'</option>');
        }

      }
  });
}


function getbatch(id){
    $.ajax({
      url: '/superadmin/getbatch',
      type: 'GET',
      data: {id:id},

      success: function(data) {

        console.log(data);
        $("#batch").empty();
        $("#batch").append('<option value="">Select</option>');
        for(i=0;i<data.batch.length;i++){
            $("#batch").append('<option value="'+data.batch[i].id+'">'+data.batch[i].title+'</option>');
        }

      }
  });
}



function filterbatch(data) {
  var page = '1'
    if(data != 'None'){
      page=data
    }


    var search = $('#searchkey').val()
    var status = $('#status').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,search:search},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }



 function batchstatus(id,vl) {

      page=$("#page").val();


    var eventDate = $('#eventDate').text()
    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,vl:vl,type:1,eventDate:eventDate},

      success: function(data) {

       $(".table-responsive").html(data.template)


      }
  });
  }


 function batchdelete() {

      page=$("#page").val();
      id=$("#hid").val();


    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,type:2,search:search},

      success: function(data) {
        $("#modaldemo5").modal('hide');

       $(".table-responsive").html(data.template)


      }
  });
  }

function addremark(id){

    var remark = $("#message_"+id).val();


    page=$("#page").val();


    var eventDate = $('#eventDate').text()

    var search = $('#searchkey').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,id:id,type:6,search:search,remark:remark,eventDate:eventDate},

      success: function(data) {
        $("#modalAdd"+id).modal('hide');

       $(".table-responsive").html(data.template)


      }
  });

}

function addamount(){

    var amount = $("#amount").val();
    var id = $("#hid").val();

    page=1



//    var search = $('#searchkey').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,id:id,type:6,amount:amount},

      success: function(data) {
        $("#modalAdd").modal('hide');
        $("#amount").val('')
       $(".table-responsive").html(data.template)
       location.reload();


      }
  });

}


function filterenquiry(data) {
  var page = '1'
    if(data != 'None'){
      page=data
    }


    var search = $('#searchkey').val()
    var status = $('#status').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,search:search},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }

function getstudents(id){
   let allBatches = document.querySelectorAll('.batchCard');
    allBatches.forEach(batch => batch.classList.remove('active'));


      var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {id:id},

      success: function(data) {
        $('#batch'+id).addClass('active');
        $("#batchstudents").html(data.template)


      }
  });

}



function filterorders(data) {
  var page = '1'
    if(data != 'None'){
      page=data
    }


    var search = $('#searchkey').val()
    var status = $('#status').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,search:search},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }


function get_batches(id){

    $.ajax({
      url: '/superadmin/get_batches',
      type: 'GET',
      data: {id:id},

      success: function(data) {

            console.log(data);
        $("#batch").empty();
        $("#batch").append('<option value="">Select</option>');
        for(i=0;i<data.batch.length;i++){
            $("#batch").append('<option value="'+data.batch[i].level__id+'">'+data.batch[i].level__title+'</option>');
        }


      }
  });
}



function getuser(id) {

    userid = $("#user").val();

  $.ajax({
      url: '/superadmin/getuser',
      type: 'GET',
      data: {userid:userid,levelid:id},

      success: function(data) {

        console.log(data);
        var gstamount = (data.coursegst/100)*data.courseprice
		$("#uname").text(data.username);
		$("#uphone").text(data.userphone);
		$("#uemail").text(data.usermail);

		$("#ucourse").text(data.usercourse);
		$("#uamount").text(data.courseprice);
		$("#usubamount").text(data.courseprice);
		$("#utotamount").text(data.courseprice);
		$("#urecamount").text(data.courseprice);
		$("#coursegst").text(data.coursegst);
		$("#inwords").text(data.inwords);
		$("#gstamount").text(gstamount);

      }
  });

}


function checkmail(vl){
  $.ajax({
    url: '/superadmin/checkmail',
    type: 'GET',
    data: {vl:vl},

    success: function(data) {

        sts = data.status;
        if(sts == true){
          $("#err").show();
          $("#submitButton").attr('disabled',true);
        }else{
          $("#err").hide();
          $("#submitButton").attr('disabled',false);
        }



    }
});
}


function addnewbatch(){

  var coursetype = $("#coursetype").val();
  var course = $("#course").val();
  var levels = $("#levels").val();
  var batch = $("#batch").val();
  try{
    var batchtype = $("#batchtype").val();
  }catch{
    var batchtype = '';
  }
  var hid = $("#hid").val();

  $.ajax({
    url: '/superadmin/addnewbatch',
    type: 'GET',
    data: {coursetype:coursetype,course:course,levels:levels,batch:batch,batchtype:batchtype,hid:hid},

    success: function(data) {
      $("#modalForm").modal('hide');
      $("#coursetype").empty();
      $("#course").empty('');
      $("#levels").empty('');
      $("#batch").empty('');
      $("#batchtype").empty('');
      $(".table-responsive").html(data.template)



    }
});


}

function openmodal(id){
  $("#hid").val(id);
  $("#modalForm").modal('show');

}

function hidetype(type){
  if(type == 'Online'){
    $("#batchid").show();
  }else{
    $("#batchid").hide();
  }
}

function hidetype1(type){
  if(type == 'Online'){
    $("#batchid").show();
    $("#batchid1").hide();
  }else{
    $("#batchid").hide();
    $("#batchid1").show();
  }
}



function acceptcertificaterequest(cid,uid) {
  var page = '1'
   


    var search = $('#searchkey').val()
    var status = $('#status').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,search:search,cid:cid,uid:uid,type:5},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }