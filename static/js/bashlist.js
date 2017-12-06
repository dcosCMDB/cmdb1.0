/*init*/
function newtable(cronres){
$('#bashtable').bootstrapTable({
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
      title: '查看脚本', field: 'cat',
        formatter: function (val, row, idx) {
          return '<button onclick="cat(this)""></button>';
        }
  }],
  data: bashres
});
}
$('#bashlistbtn').attr("style","color:#337ab7");
$.get("/searchbash", function (ret) {
	bashlist=ret.bashlist
  newtable(bashlist)
	}
)

function cat(obj){
	hostip="1.1.1.1"
	path="/data"
	$.get("/cat", function (ret) {
		text=ret.text
		console.log(text)
	}
	)
}
