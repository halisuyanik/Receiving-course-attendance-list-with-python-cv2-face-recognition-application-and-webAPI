#pragma checksum "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "f3ca088bf18dae3ccaa0ac9c8e6db267e223c561"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Home_RollCall), @"mvc.1.0.view", @"/Views/Home/RollCall.cshtml")]
[assembly:global::Microsoft.AspNetCore.Mvc.Razor.Compilation.RazorViewAttribute(@"/Views/Home/RollCall.cshtml", typeof(AspNetCore.Views_Home_RollCall))]
namespace AspNetCore
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#line 1 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\_ViewImports.cshtml"
using RollCall_webapi;

#line default
#line hidden
#line 2 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\_ViewImports.cshtml"
using RollCall_webapi.Models;

#line default
#line hidden
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"f3ca088bf18dae3ccaa0ac9c8e6db267e223c561", @"/Views/Home/RollCall.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"44f944045f4c3c246f18959b84148c28f9a5d0a4", @"/Views/_ViewImports.cshtml")]
    public class Views_Home_RollCall : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<System.Data.DataSet>
    {
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
#line 2 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
  
    ViewData["Title"] = "RollCall";

#line default
#line hidden
            BeginContext(72, 286, true);
            WriteLiteral(@"<script>
    function printDiv() {
        window.frames[""print_frame""].document.body.innerHTML = document.getElementById(""printableTable"").innerHTML;
        window.frames[""print_frame""].window.focus();
        window.frames[""print_frame""].window.print();
    }
</script>

<h1>");
            EndContext();
            BeginContext(359, 19, false);
#line 13 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
Write(ViewBag.secilitablo);

#line default
#line hidden
            EndContext();
            BeginContext(378, 251, true);
            WriteLiteral("</h1>\r\n\r\n\r\n<div>\r\n    <button class=\"btn btn-info  offset-md-10\" onclick=\"printDiv()\"><i class=\"fas fa-print\"></i> Çizelgeyi Yazdır</button>\r\n</div>\r\n<div id=\"printableTable\">\r\n\r\n\r\n    <table class=\"table table-striped\">\r\n        <thead>\r\n            ");
            EndContext();
            BeginContext(630, 19, false);
#line 24 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
       Write(ViewBag.secilitablo);

#line default
#line hidden
            EndContext();
            BeginContext(649, 359, true);
            WriteLiteral(@"
            <tr>
                <th scope=""col"">Derse Giris Saati</th>
                <th scope=""col"">Ad Soyad</th>
                <th scope=""col"">Ogrenci No</th>
                <th scope=""col"">Bolum</th>
                <th scope=""col"">Yas</th>
                <th scope=""col"">Cinsiyet</th>
            </tr>
        </thead>
        <tbody>
");
            EndContext();
#line 35 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
             foreach (System.Data.DataRow dr in ViewBag.detaylar.Rows)
            {

#line default
#line hidden
            BeginContext(1095, 46, true);
            WriteLiteral("                <tr>\r\n                    <td>");
            EndContext();
            BeginContext(1143, 11, false);
#line 38 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
                    Write(dr["Zaman"]);

#line default
#line hidden
            EndContext();
            BeginContext(1155, 31, true);
            WriteLiteral("</td>\r\n                    <td>");
            EndContext();
            BeginContext(1188, 13, false);
#line 39 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
                    Write(dr["AdSoyad"]);

#line default
#line hidden
            EndContext();
            BeginContext(1202, 31, true);
            WriteLiteral("</td>\r\n                    <td>");
            EndContext();
            BeginContext(1235, 8, false);
#line 40 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
                    Write(dr["No"]);

#line default
#line hidden
            EndContext();
            BeginContext(1244, 31, true);
            WriteLiteral("</td>\r\n                    <td>");
            EndContext();
            BeginContext(1277, 11, false);
#line 41 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
                    Write(dr["Bolum"]);

#line default
#line hidden
            EndContext();
            BeginContext(1289, 31, true);
            WriteLiteral("</td>\r\n                    <td>");
            EndContext();
            BeginContext(1322, 9, false);
#line 42 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
                    Write(dr["Yas"]);

#line default
#line hidden
            EndContext();
            BeginContext(1332, 31, true);
            WriteLiteral("</td>\r\n                    <td>");
            EndContext();
            BeginContext(1365, 14, false);
#line 43 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
                    Write(dr["Cinsiyet"]);

#line default
#line hidden
            EndContext();
            BeginContext(1380, 30, true);
            WriteLiteral("</td>\r\n                </tr>\r\n");
            EndContext();
#line 45 "C:\Users\HP\Desktop\ET\python_project\RollCall_webapi\RollCall_webapi\Views\Home\RollCall.cshtml"
            }

#line default
#line hidden
            BeginContext(1425, 207, true);
            WriteLiteral("        </tbody>\r\n    </table>\r\n    <iframe name=\"print_frame\" width=\"0\" height=\"0\" frameborder=\"0\" src=\"about:blank\"></iframe>\r\n</div>\r\n<a href=\"/Home/Index\" class=\"btn btn-secondary btn-sm\"> < Geri Dön</a>");
            EndContext();
        }
        #pragma warning restore 1998
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<System.Data.DataSet> Html { get; private set; }
    }
}
#pragma warning restore 1591