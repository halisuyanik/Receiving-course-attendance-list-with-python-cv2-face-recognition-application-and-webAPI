using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using RollCall_webapi.Models;
using System.Data.SqlClient;
using System.Data.SQLite;
using System.Linq.Expressions;
using Devart.Data.Linq.Mapping;
using System.Data;
using Microsoft.AspNetCore.Http;


namespace RollCall_webapi.Controllers
{
    public class HomeController : Controller
    {
        
        accountsdbModel db =new accountsdbModel();
        
        public IActionResult Index()
        {

            SQLiteConnection con = new SQLiteConnection(@"Data Source=accountsdb.db;");
            con.Open();

            List<string> tables = new List<string>();
            DataTable dt = con.GetSchema("Tables");
            if (HttpContext.Session.GetString("DersKodu")!=null)
            {
                foreach (DataRow row in dt.Rows)
                {
                    string tablename = (string)row[2];
                    if (tablename.Contains("sqlite_sequence") || tablename.Contains("Kullanicilar") || tablename.Contains("_EFMigrationsHistory"))
                    {
                        continue;
                    }
                    else if (tablename.Contains(HttpContext.Session.GetString("DersKodu")))
                    {
                        tables.Add(tablename);
                    }
                }
            }
            else
            {
                return RedirectToAction("Login", "Account");
            }
            
            ViewBag.tablolar = tables;
            con.Close();

            return View();
        }

        public DataSet show_data(string secilitablo)
        {
            SQLiteConnection con = new SQLiteConnection(@"Data Source=accountsdb.db");
            SQLiteCommand cmd = new SQLiteCommand("SELECT * FROM " + secilitablo, con);
            SQLiteDataAdapter da = new SQLiteDataAdapter(cmd);
            DataSet ds = new DataSet();
            da.Fill(ds);
            return ds;
        }

        public IActionResult RollCall(string secilitablo)
        {
            if (HttpContext.Session.GetString("DersKodu") != null)
            {
                ViewBag.secilitablo = secilitablo;
                DataSet ds = show_data(secilitablo);
                ViewBag.detaylar = ds.Tables[0];
            }
            else
            {
                return RedirectToAction("Login", "Account");
            }
            return View();
        }
       

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
