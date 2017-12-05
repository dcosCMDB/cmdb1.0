/*init*/
function newtable(hostres){
$('#hosttable').bootstrapTable({
    search: true,  //是否显示搜索框功能
    pagination: true,  //是否分页
    showRefresh: true, //是否显示刷新功能
    iconSize: 'outline',
   // toolbar: '#exampleTableEventsToolbar', 可以在table上方显示的一条工具栏，
    icons: {
      refresh: 'glyphicon-repeat',
      toggle: 'glyphicon-list-alt'
    },
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
