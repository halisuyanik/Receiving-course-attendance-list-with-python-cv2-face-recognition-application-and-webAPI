﻿// <auto-generated />
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using RollCall_webapi.ContextData;

namespace RollCall_webapi.Migrations
{
    [DbContext(typeof(VeritabaniContext))]
    partial class VeritabaniContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "2.2.2-servicing-10034");

            modelBuilder.Entity("RollCall_webapi.Models.Kullanici", b =>
                {
                    b.Property<int>("Id")
                        .ValueGeneratedOnAdd();

                    b.Property<string>("DersKodu");

                    b.Property<string>("KAdi")
                        .IsRequired();

                    b.Property<string>("Sifre")
                        .IsRequired();

                    b.HasKey("Id");

                    b.ToTable("Kullanicilar");
                });
#pragma warning restore 612, 618
        }
    }
}
