$(function(){
	//页面加载完成之后执行
	pageInit();
});
function pageInit(){
	//创建jqGrid组件
	jQuery("#list2").jqGrid(
			{
				url : './static/data/xsxk.json',//组件创建完成之后请求数据的url
				datatype : "json",//请求数据返回的类型。可选json,xml,txt
				colNames : [ '学生学号', '学生姓名', '课程代码', '课程名称','开课学年', '开课学期','开课部门名称','开课部门编号','教学班名称','课程评分'],//jqGrid的列显示名字
				colModel : [ //jqGrid每一列的配置信息。包括名字，索引，宽度,对齐方式.....
				             {name : 'xsxh',index : 'xsxh',width : 110,align : "left"}, 
				             {name : 'xsxm',index : 'xsxm',width : 110,align : "left"}, 
				             {name : 'kcdm',index : 'kcdm',width : 110,align : "left"}, 
				             {name : 'kcmc',index : 'kcmc',width : 220,align : "left"}, 
				             {name : 'kkxn',index : 'kkxn',width : 110,align : "left"}, 
				             {name : 'kkxq',index : 'kkxq',width : 110,align : "left"},
				             {name : 'kkbmmc',index : 'kkbmmc',width : 160,align : "left"},
				             {name : 'kkbmbh',index : 'kkbmbh',width : 110,align : "left"},  
				             {name : 'jxbmc',index : 'jxbmc',width : 130,align : "left"}, 
				             {name : 'kcpf',index : 'kcpf',width : 150,align : "middle"}			             
				           ],
				rowNum : 30,//一页显示多少条
				rowList : [ 10, 20, 30 ],//可供用户选择一页显示多少条
				pager : '#pager2',//表格页脚的占位符(一般是div)的id
				sortname : 'id',//初始化的时候排序的字段
				sortorder : "desc",//排序方式,可选desc,asc
				mtype : "post",//向后台请求数据的ajax的类型。可选post,get
				viewrecords : true,
				caption : "已选选课信息",//表格的标题名字
				height : 200
			});
	/*创建jqGrid的操作按钮容器*/
	/*可以控制界面上增删改查的按钮是否显示*/
	jQuery("#list2").jqGrid('navGrid', '#pager2', {edit : false,add : false,del : false});


	jQuery("#list3").jqGrid(
			{
				url : './static/data/JSONData.json',//组件创建完成之后请求数据的url
				datatype : "json",//请求数据返回的类型。可选json,xml,txt
				colNames : [ '课程代码', '课程名称','开课学年', '开课学期', '教学班名称',  '上课时间地点','开课部门编号','开课部门名称' ],//jqGrid的列显示名字
				colModel : [ //jqGrid每一列的配置信息。包括名字，索引，宽度,对齐方式.....
							 {name : 'kcdm',index : 'kcdm',width : 130,align : "left"}, 
				             {name : 'kcmc',index : 'kcmc',width : 270,align : "leftleft"}, 
				             {name : 'kkxn',index : 'kkxn',width : 140,align : "left"}, 
				             {name : 'kkxq',index : 'kkxq',width : 110,align : "left"}, 
				             {name : 'jxbmc',index : 'jxbmc',width : 140,align : "left"},             
				             {name : 'sksj',index : 'sksj',width : 180,align : "left"}, 
				             {name : 'kkbmbh',index : 'kkbmbh',width : 100,align : "left"}, 
				             {name : 'kkbmmc',index : 'kkbmmc',width : 250,align : "left"} 
				           ],
				rowNum : 5,//一页显示多少条
				rowList : [ 10, 20, 30 ],//可供用户选择一页显示多少条
				pager : '#pager3',//表格页脚的占位符(一般是div)的id
				sortname : 'id',//初始化的时候排序的字段
				sortorder : "desc",//排序方式,可选desc,asc
				mtype : "post",//向后台请求数据的ajax的类型。可选post,get
				viewrecords : true,
				caption : "推荐课程信息",//表格的标题名字
				height : 200
			});
	/*创建jqGrid的操作按钮容器*/
	/*可以控制界面上增删改查的按钮是否显示*/
	jQuery("#list3").jqGrid('navGrid', '#pager3', {edit : false,add : false,del : false});
}