using Microsoft.EntityFrameworkCore;
using RollCall_webapi.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using RollCall_webapi;

namespace RollCall_webapi.ContextData
{
    public class VeritabaniContext : DbContext
    {
        public VeritabaniContext(DbContextOptions<VeritabaniContext> options) : base(options)
        {

        }

        public DbSet<Kullanici> Kullanicilar { get; set; }
    }
}
