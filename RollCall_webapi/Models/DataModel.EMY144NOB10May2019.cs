﻿//------------------------------------------------------------------------------
// This is auto-generated code.
//------------------------------------------------------------------------------
// This code was generated by Entity Developer tool using EF Core template.
// Code is generated on: 13.05.2019 00:50:32
//
// Changes to this file may cause incorrect behavior and will be lost if
// the code is regenerated.
//------------------------------------------------------------------------------

using System;
using System.Data;
using System.ComponentModel;
using System.Linq;
using System.Linq.Expressions;
using System.Data.Common;
using System.Collections.Generic;

namespace RollCall_webapi
{
    public partial class EMY144NOB10May2019 {

        public EMY144NOB10May2019()
        {
            OnCreated();
        }

        public virtual int Id
        {
            get;
            set;
        }

        public virtual string Zaman
        {
            get;
            set;
        }

        public virtual string AdSoyad
        {
            get;
            set;
        }

        public virtual int No
        {
            get;
            set;
        }

        public virtual string Bolum
        {
            get;
            set;
        }

        public virtual int? Yas
        {
            get;
            set;
        }

        public virtual string Cinsiyet
        {
            get;
            set;
        }

        #region Extensibility Method Definitions

        partial void OnCreated();

        #endregion
    }

}
