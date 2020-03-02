//ischool plus search all launchActivity
var window_top = window.top ;
var html_Pathtree = window_top.document.getElementById("s_catalog").contentWindow.document.getElementById("pathtree").contentWindow;
var launchActivity = html_Pathtree.document.getElementsByTagName('a');
launchActivity[ 1 ].onclick();

//describle driver.execute_script in python
1 = i (python)

//----------------------------------------------------------------------------------------------

//ischool plus download 
var window_top = window.top ;
var html_s_main = window_top.document.getElementById("s_main").contentWindow;
var s_main_title = html_s_main.document.getElementsByTagName('title')[0];

//debug
//s_main_title.text;

if (s_main_title.text == "臺北科技大學(NTUT) " ){
    html_s_main.document.getElementsByTagName("button")[0].onclick() ;
}
else{
    var s_main_script = html_s_main.document.getElementsByTagName('script');
    var arrScript = new Array() ;
        arrScript = s_main_script[0].text.split("var DEFAULT_URL   = '");
        strUrl_Pdf = arrScript[1].split("';")[0] ;
        strUrl_Pdf = "https://istudy.ntut.edu.tw/learn/path/" + strUrl_Pdf ;

        //download pdf 
        var downloadLink = document.createElement('a');
        downloadLink.href = strUrl_Pdf ;
        downloadLink.download = 'david';
        downloadLink.click();        
}

//----------------------------------------------------------------------------------------------
    
//download pdf 
var downloadLink = document.createElement('a');
    downloadLink.href = strUrl_Pdf ;
    downloadLink.download = 'david';
    downloadLink.click();

// getPDF.php?id=20190910194730ch06_web.pdf&ticket=c3c0cba06d60f938e07b99dd4149871a

//----------------------------------------------------------------------------------------------

//print_class_name
function print_class_name(){
    var arrClass_Name = new Array() ;
    var window_top = window.top ;
    var moocSysbar = window_top.document.getElementById("moocSysbar").contentWindow ;
    var select = moocSysbar.document.getElementById("selcourse") ;
    for( i = 0 ; i < select.length ; i++ ){
        arrClass_Name.push(select[i].text) ;
    
        //debug
        //console.log(select[i].text) ; 
    }
    select.click() ;
    return arrClass_Name ;
}

print_class_name() ;

//----------------------------------------------------------------------------------------------

//choose class
var arrClass_Name = new Array() ;
var window_top = window.top ;
var moocSysbar = window_top.document.getElementById("moocSysbar").contentWindow ;
var select = moocSysbar.document.getElementById("selcourse") ;
select[4].selected = true ;
select.onchange();

4 = i (python)

//----------------------------------------------------------------------------------------------

//choose select_class_content (SYS_04_01_002)
var window_top = window.top ;
var moocSysbar = window_top.document.getElementById("moocSysbar").contentWindow ;
moocSysbar.document.getElementById("SYS_04_01_002").click() ;