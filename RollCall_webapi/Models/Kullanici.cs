using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;

namespace RollCall_webapi.Models
{
    public class Kullanici
    {
        [Key]
        public int Id { get; set; }

        [Display(Name = "Kullanıcı Adı")]
        [Required(ErrorMessage = "Kullanıcı adı girilmelidir")]
        public string KAdi { get; set; }

        [Display(Name = "Şifre")]
        [Required(ErrorMessage = "Şifre girilmelidir")]
        [DataType(DataType.Password)]
        public string Sifre { get; set; }

        public string DersKodu { get; set; }
    }
}
