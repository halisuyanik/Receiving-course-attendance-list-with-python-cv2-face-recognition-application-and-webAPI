using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using RollCall_webapi.ContextData;
using RollCall_webapi.Models;

namespace RollCall_webapi.Controllers
{
    public class AccountController : Controller
    {
        private readonly VeritabaniContext _context;
        public AccountController(VeritabaniContext context)
        {
            _context = context;
        }

        public ActionResult Login()
        {
            return View();
        }
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Login(Kullanici kullanici)
        {
            TempData["girissonuc"] = "";
            
            var log = _context.Kullanicilar.Where(x => x.KAdi == kullanici.KAdi && x.Sifre == kullanici.Sifre).SingleOrDefault();
            if (log != null)
            {
                HttpContext.Session.SetString("KullaniciAdi", log.KAdi);
                HttpContext.Session.SetString("DersKodu", log.DersKodu);
                return RedirectToAction("Index", "Home");
            }
            else
            {
                TempData["girissonuc"] = "Kullanıcı adı veya şifre yanlış.";
                return RedirectToAction("Login", "Account");
            }
        }

        public IActionResult Logout()
        {
            
            HttpContext.Session.Remove("KullaniciAdi");
            HttpContext.Session.Remove("DersKodu");
            HttpContext.Session.Clear();
            return RedirectToAction("Login", "Account");
        }

        // GET: Account/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Account/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,KAdi,Sifre,DersKodu")] Kullanici kullanici)
        {
            if (ModelState.IsValid)
            {
                _context.Add(kullanici);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Login));
            }
            return View(kullanici);
        }

       
    }
}
