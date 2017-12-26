/*init*/
function newtable(hostres){
$('#hosttable').bootstrapTable({
    search: true,  //是否显示搜索框功能
    pagination: true,  //是否分页
  columns: [{
      field: 'hostip',
      title: 'ip',
      sortable: true
  }, {
      field: 'hostname',
      title: '主机名',
      sortable: true
  }, {
      field: 'env',
      title: '区域',
      sortable: true
  }, {
      field: 'cpu',
      title: 'CPU',
      sortable: true
  }, {
      field: 'mem',
      title: '内存',
      sortable: true
  }, {
      field: 'filesys',
      title: '文件系统'
  },{
      title: '<a href="#" onclick="checkall()">全选</a><span>||</span><a href="#" onclick="reverse()">反选</a>(<span id="numofselect">0</span>)', field: 'check',
        formatter: function (val, row, idx) {
          return '<input type="checkbox" class="select" onclick="changenum()"">';
        }
  }],
  data: hostres
});
}
$('#hostlistbtn').attr("style","color:#337ab7");
$.get("/searchhost", function (ret) {
	hostlist=ret.hostlist
  newtable(hostlist)
	}
)

/*check option*/
function changenum(){
    var ho=$(".select");
    testho=ho[0]
    testho.parentElement.parentElement.getAttribute('visible')
    numofselect=0
    for(var i=0;i<ho.length;i++){
    	ifvisible=ho[i].parentElement.parentElement.getAttribute('visible')
    	if(ifvisible=="true"||ifvisible==null){
	        if (ho[i].checked==true){
	            numofselect=numofselect+1
	        }
    	}
    }
    $("#numofselect").html(numofselect)
}
function checkall(){
    var ho=$(".select");
    numofselect=0
    for(var i=0;i<ho.length;i++){
    	ifvisible=ho[i].parentElement.parentElement.getAttribute('visible')
    	if(ifvisible=="true"||ifvisible==null){
	        ho[i].checked=true;
	        numofselect=numofselect+1
    	}
    }
    $("#numofselect").html(numofselect)
}
function reverse(){
    var ho=$(".select");
    numofselect=0
    for(var i=0;i<ho.length;i++){
    	ifvisible=ho[i].parentElement.parentElement.getAttribute('visible')
    	if(ifvisible=="true"||ifvisible==null){
	        ho[i].checked=!ho[i].checked;
	        if (ho[i].checked==true){
	            numofselect=numofselect+1
	        }
    	}
    }
    $("#numofselect").html(numofselect)
}

function clearall(){
	var ho=$(".select");
    numofselect=0
    for(var i=0;i<ho.length;i++){
        ho[i].checked=false;
    }
    $("#numofselect").html(numofselect)
}

function dooptions(){
    var ho=$(".select");
    $('#modaliplist').html('')
    for(var i=0;i<ho.length;i++){
      if (ho[i].checked==true){
        context=$("<p></p>").text(ho[i].parentElement.parentElement.firstElementChild.textContent);
        $('#modaliplist').append(context)
      }
    }
    $('#mymodal').modal('show')
}

function getcheckedhost(){
  var iplist=[]
  var ho=$('#modaliplist p')
  for(var i=0;i<ho.length;i++){
    iplist.push(ho[i].textContent)
  }
  return iplist
}

function resultshow(result){
    console.log(result)
    $('#modalresult').html('')
    for(var i=0;i<result.length;i++){
      if(result[i].state==0)
        context=$("<pre style='color:green'></pre>").text(result[i].hostip+'\n'+result[i].info)
      else
        context=$("<pre style='color:red'></pre>").text(result[i].hostip+'\n'+result[i].info)
      $('#modalresult').append(context)
    }
}

function testping(){
  $('#modalresult').html('wait...')
  var iplist=getcheckedhost()
  $.get("/testping",{'iplist': iplist.join(';')}, function (ret) {
      result=ret.pingres
      resultshow(result)
    }
  )
}

function md5check(){
  $('#modalresult').html('wait...')
  var iplist=getcheckedhost()
  $.get("/md5check",{'iplist': iplist.join(';')}, function (ret) {
      result=ret.md5res
      resultshow(result)
    }
  )
}

function showlogs(){
  $('#modalresult').html('wait...')
  var iplist=getcheckedhost()
  $.get("/showlogs",{'iplist': iplist.join(';')}, function (ret) {
      result=ret.logres
      resultshow(result)
    }
  )
}

function copyfile(){
  $('#modalresult').html('wait...')
  $('#file').modal('show');
}

function testfile(){
  var filesrc=$('#copysrcfile').val()
  if(filesrc.split(':').length!=2){
    alert('illegal filename! filename should be hostip:filepath')
  }
  else{
    var hostip=filesrc.split(':')[0]
    var filename=filesrc.split(':')[1]
    $.get("/testfile",{'filename': filename,'hostip':hostip}, function (ret) {
      result=ret.testres
      state=ret.state
      if(state!=0){
        alert(result['info'])
      }
      else{
        $('#filetestbtn').removeClass('btn-default')
        $('#filetestbtn').addClass('btn-success')
        if($('#desttestbtn').hasClass('btn-success')){
          $('#copybtn').removeAttr('disabled')
        }
      }
    }
    )
  }
}

function testdest(){
  var destpath=$('#copydestpath').val()
  if (destpath[destpath.length-1]!='/'){
    alert("destpath should end with '/' !")
  }
  else{
    var iplist=getcheckedhost()
    $.get("/testdest",{'destpath': destpath,'iplist': iplist.join(';')}, function (ret) {
      result=ret.destres
      state=ret.state
      if(state!=0){
        alert(result['info'])
      }
      else{
        $('#desttestbtn').removeClass('btn-default')
        $('#desttestbtn').addClass('btn-success')
        if($('#filetestbtn').hasClass('btn-success')){
          $('#copybtn').removeAttr('disabled')
        }
      }
    }
    )
  }
}

function copy(){
  var iplist=getcheckedhost()
  var filesrc=$('#copysrcfile').val()
  if(filesrc.split(':').length!=2){
    alert('illegal filename! filename should be hostip:filepath')
  }
  else{
    var hostip=filesrc.split(':')[0]
    var filename=filesrc.split(':')[1]
    $.get("/copyfile",{'filename': filename,'hostip':hostip,'iplist': iplist.join(';')}, function (ret) {
      result=ret.copyres
      state=ret.state
    }
    )
  }
}
