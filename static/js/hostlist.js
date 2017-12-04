/*init*/
$('#hostlistbtn').attr("style","color:#337ab7");
$.get("/searchhost", function (ret) {
	hostlist=ret.hostlist
	for (i=0;i<hostlist.length;i++){
		hostip=hostlist[i].hostip
		hostname=hostlist[i].hostname
		env=hostlist[i].env
		cpu=hostlist[i].cpu
		mem=hostlist[i].mem
		filesys=hostlist[i].filesys
		console.log(cpu)
		console.log(mem)
		context='<tr>'+
				'<th>'+
				'<input type="checkbox" class="select" onclick="changenum()"">'+
				'</th>'+
				'<td>'+hostip+'</td>'+
				'<td>'+hostname+'</td>'+
				'<td>'+env+'</td>'+
				'<td>'+cpu+'</td>'+
				'<td>'+mem+'</td>'+
				'<td>'+filesys+'</td>'+
				'</tr>'
        $('#hosttbody').append(context)
	}
})

/*table script*/
$(document).ready(function() {
  $(".search").keyup(function () {
  	clearall()
    var searchTerm = $(".search").val();
    var listItem = $('.results tbody').children('tr');
    var searchSplit = searchTerm.replace(/ /g, "'):containsi('")
    
  $.extend($.expr[':'], {'containsi': function(elem, i, match, array){
        return (elem.textContent || elem.innerText || '').toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
    }
  });
    
  $(".results tbody tr").not(":containsi('" + searchSplit + "')").each(function(e){
    $(this).attr('visible','false');
  });

  $(".results tbody tr:containsi('" + searchSplit + "')").each(function(e){
    $(this).attr('visible','true');
  });

  var jobCount = $('.results tbody tr[visible="true"]').length;
    $('.counter').text(jobCount + ' item');

  if(jobCount == '0') {$('.no-result').show();}
    else {$('.no-result').hide();}
      });
});

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