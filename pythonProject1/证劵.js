
<input id="content" name="content" maxlength="30" placeholder="è¯·è¾å¥å³é®å­æ¥è¯¢"  />
<input id="search" type="button" value="æç´¢" onclick="javascript:ptsearch();" />
<input id="gjsearch" type="button" value="é«çº§æç´¢" onclick="window.open('/hzs-web/search/searchHigherUI.jspx?remark=chinese', '_blank')"  />


<script type=text/javascript>

	function ptsearch(){
		var keyword = document.getElementById("content").value;
		if(keyword != ""){
			simplesearch(keyword, "2", "all", "1", "10");
		}
		else {
		   alert("è¯·è¾å¥æ¥è¯¢è¯");
		}
		/*
		 $.ajax({
			 type: "GET",
			 url: "/hzs-web/search/searchLuceneSimple.jspx",
			// data: {content:$("#content").val(),sorttype:2,rangekey:all,currentpage:1,pagesize:10},
			 data :{"normalKeyword":keyword,"sorttype":sorttype,"rangekey":2,"currentpage":currentpage,"pagesize":pagesize},
			 dataType: "json",
			 success : function(result) {
				if (result.success) {
					window.open('/hzs-web/search/searchResultUI.jspx','_blank');
				}else {
					alert(result.msg);
				}
			 }
		});
		*/
	}

	function simplesearch(keyword, sorttype, rangekey, currentpage, pagesize){
		$.ajax({
			type : "POST",
			url : '/hzs-web/search/searchLuceneSimple.jspx',
			data : {
				normalKeyword:keyword,
				sorttype:sorttype,
				rangekey:rangekey,
				currentpage:currentpage,
				pagesize:pagesize,
				remark: "chinese"
			},
			dataType : "json",
			success : function(result) {
				if (result.success) {
					window.open('/hzs-web/search/searchResultUI.jspx','_blank');
				}else {
					alert(result.msg);
				}
			}
		});
	};
/*
	function ptsearch(){
		var keyword = document.getElementById("content").value;
		alert(keyword );
        if(keyword != ""){
			simplesearch(keyword, "2", "all", "1", "10");
		}
		else {
		   alert("è¯·è¾å¥æ¥è¯¢è¯");
		}
	};

	function simplesearch(keyword, sorttype, rangekey, currentpage, pagesize){
		ajax({
			type : "POST",
			url : '/hzs-web/search/searchLuceneSimple.jspx',
			data :{"normalKeyword":keyword,"sorttype":sorttype,"rangekey":rangekey,"currentpage":currentpage,"pagesize":pagesize},
			dataType : "json",
			success : function(result) {
				if (result.success) {
					window.open('/hzs-web/search/searchResultUI.jspx','_blank');
				}else {
					alert(result.msg);
				}
			}
		});
	};

	function ajax(){
	  var ajaxData = {
	    type:arguments[0].type || "GET",
	    url:arguments[0].url || "",
	    async:arguments[0].async || "true",
	    data:arguments[0].data || null,
	    dataType:arguments[0].dataType || "text",
	    contentType:arguments[0].contentType || "application/x-www-form-urlencoded",
	    beforeSend:arguments[0].beforeSend || function(){},
	    success:arguments[0].success || function(){},
	    error:arguments[0].error || function(){}
	  }

	  ajaxData.beforeSend() ;

	  var xhr = createxmlHttpRequest();
	  //alert('666888'+ajaxData.dataType);
	  console.log(ajaxData.dataType);
	  xhr.responseType=ajaxData.dataType;
	console.log(xhr.responseType);
	  xhr.open(ajaxData.type,ajaxData.url,ajaxData.async);
	  xhr.setRequestHeader("Content-Type",ajaxData.contentType);
	  xhr.send(convertData(ajaxData.data));

	  xhr.onreadystatechange = function() {
	    if (xhr.readyState == 4) {
	      if(xhr.status == 200){
	        ajaxData.success(xhr.response)
	      }else{
	        ajaxData.error()
	      }
	    }
	  }
	}

	function createxmlHttpRequest() {
	  if (window.ActiveXObject) {
	    return new ActiveXObject("Microsoft.XMLHTTP");
	  } else if (window.XMLHttpRequest) {
	    return new XMLHttpRequest();
	  }
	}

	function convertData(data){
	  if( typeof data === 'object' ){
	    var convertResult = "" ;
	    for(var c in data){
	      convertResult+= c + "=" + data[c] + "&";
	    }
	    convertResult=convertResult.substring(0,convertResult.length-1)
	    return convertResult;
	  }else{
	    return data;
	  }
	}
*/
