(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[192],{7031:function(e,a,n){"use strict";n(7294);var s=n(5893);a.Z=function(){return(0,s.jsxs)("div",{className:"lds-ripple",children:[(0,s.jsx)("div",{}),(0,s.jsx)("div",{})]})}},2360:function(e,a,n){"use strict";n.d(a,{Z:function(){return j}});var s=n(5567),t=n.n(s),i=n(6538),r=n.n(i),c=n(6128),l=n(5893);function o(e){var a=e.children,n=e.setFunction;return(0,l.jsx)(c.E.button,{whileHover:{scale:1.1,transition:{duration:.5}},className:r().button,onClick:n,children:a})}var d=n(1664),h=n.n(d),_=n(9473),m=n(3967),u=n(7294),g=n(8113),x=n(4422);function j(){var e=(0,u.useState)(!1),a=e[0],n=e[1],s=(0,u.useState)(null),i=s[0],r=s[1],c=(0,u.useState)(!1),d=c[0],j=c[1],p=(0,_.v9)((function(e){return e})),f=p.card,v=p.search,N=p.user,b=p.category,k=p.likes,w=(0,_.I0)();return(0,u.useEffect)((function(){i||fetch(g._+"/api/products/gif-banner/").then((function(e){return e.json()})).then((function(e){return r(e.data.image)})).catch((function(e){return console.log(e)}));var e=localStorage.getItem("like");if(e&&0===k.length){var a=JSON.parse(e);w((0,x.mN)(a))}}),[]),(0,l.jsxs)("header",{className:t().header,children:[(0,l.jsxs)("div",{className:t().container,children:[(0,l.jsxs)("div",{className:t().sec1,children:[(0,l.jsx)("div",{style:{cursor:"pointer"},children:(0,l.jsx)(h(),{href:"/",children:(0,l.jsx)("a",{children:(0,l.jsx)("img",{src:"/logo1.png",alt:"logo",width:"100px"})})})}),(0,l.jsx)("div",{className:t().gif_section,children:i&&(0,l.jsx)("img",{src:g._+i,width:"100%",height:80})}),(0,l.jsx)("div",{children:(0,l.jsxs)("ul",{className:t().navbar,children:[(0,l.jsx)("li",{children:(0,l.jsx)(h(),{href:"/media",children:(0,l.jsxs)("a",{className:t().navbar_sec,children:[(0,l.jsx)("img",{className:t().prof,width:25,height:25,src:"/play.png",alt:"phone"}),(0,l.jsx)("span",{className:t().navbar_title,children:"\u041c\u0435\u0434\u0438\u044f"})]})})}),(0,l.jsxs)("li",{onClick:function(){return n(!0)},children:[(0,l.jsx)("img",{className:t().prof,width:25,height:25,style:{objectFit:"contain"},src:"/location.png",alt:"location"}),(0,l.jsx)("span",{children:"\u041c\u0430\u0433\u0430\u0437\u0438\u043d\u044b"})]}),(0,l.jsx)("li",{children:(0,l.jsx)(h(),{href:N.token?"/profile":"/login",children:(0,l.jsxs)("a",{className:t().navbar_sec,children:[(0,l.jsx)("img",{className:t().prof,width:30,height:30,src:"/user.png",alt:"user"}),(0,l.jsx)("span",{className:t().navbar_title,children:"\u041f\u0440\u043e\u0444\u0438\u043b\u044c"})]})})})]})})]}),(0,l.jsxs)("div",{className:t().sec2,children:[(0,l.jsx)(o,{setFunction:function(){return j(!0)},children:"\u0412\u0441\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438"}),(0,l.jsxs)("div",{className:t().search_section,children:[(0,l.jsx)("input",{className:t().search,type:"text",placeholder:"\u041f\u043e\u0438\u0441\u043a",name:"Search",value:v.title,onChange:function(e){return w((a=e.target.value,{type:m.Tf,payload:a}));var a}}),(0,l.jsx)(h(),{href:"/search",children:(0,l.jsx)("a",{children:(0,l.jsx)(o,{children:(0,l.jsx)("img",{src:"/searchion.png",width:"27px",height:"30px",alt:"search icon"})})})})]}),(0,l.jsx)(h(),{href:"/like",children:(0,l.jsx)("a",{children:(0,l.jsxs)("div",{className:t().like_section,children:[(0,l.jsx)("div",{className:t().like_icon,children:(0,l.jsx)("img",{src:"/like.png",width:40,height:40,style:{cursor:"pointer",objectFit:"contain"},alt:"like icon"})}),(0,l.jsx)("div",{className:t().like_count,children:k.length})]})})}),(0,l.jsxs)("ul",{className:t().navbar,children:[(0,l.jsx)("li",{children:(0,l.jsx)("img",{className:t().icons,width:40,height:40,src:"/imo.png"})}),(0,l.jsx)("li",{children:(0,l.jsx)("img",{className:t().icons,width:40,height:40,src:"/inst.png",alt:"instogram logo"})}),(0,l.jsx)("li",{children:(0,l.jsx)("img",{className:t().icons,width:40,height:40,src:"/facebook.png",alt:"facebook logo"})})]}),(0,l.jsx)(h(),{href:"/cart",children:(0,l.jsxs)("a",{className:t().cart,children:[(0,l.jsx)("img",{src:"/cart.png",width:"26px",height:"30px"}),"+",f.length]})})]}),d&&(0,l.jsx)("div",{className:t().category__list_show,onMouseLeave:function(){return j(!1)},children:b.data&&b.data.map((function(e){return(0,l.jsxs)("div",{className:t().cat_item,children:[(0,l.jsx)("span",{children:e.title_tm}),(0,l.jsx)("div",{className:t().subcat,children:e.subcategories.map((function(e){return(0,l.jsx)(h(),{href:"/category/".concat(e.id),children:(0,l.jsx)("a",{children:(0,l.jsx)("div",{className:t().subcat_item,children:e.title_tm})})},e.id)}))})]},e.id)}))})]}),a&&(0,l.jsxs)("div",{className:t().magazin_modal,children:[(0,l.jsx)("div",{className:t().magazin_modal__close,onClick:function(){return n(!1)},children:(0,l.jsx)("img",{src:"/close.png",width:"25px",height:"25px"})}),(0,l.jsx)("div",{className:t().magazin_modal__container,children:(0,l.jsx)("div",{className:t().karta_modal,children:(0,l.jsx)("iframe",{src:"https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d25166.585301938532!2d58.39670772134997!3d37.95791483986182!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1sRysgal%20mebel!5e0!3m2!1sru!2s!4v1661403747160!5m2!1sru!2s",width:"100%",height:"100%",style:{border:"0"},loading:"lazy",referrerpolicy:"no-referrer-when-downgrade"})})})]})]})}},6355:function(e,a,n){"use strict";n.r(a);var s=n(2360),t=n(7294),i=n(8113),r=n(7031),c=n(6189),l=n(5893);a.default=function(){var e=(0,t.useState)(!0),a=e[0],n=e[1],o=(0,t.useState)({}),d=o[0],h=o[1],_=(0,t.useState)(!1),m=_[0],u=_[1];return console.log("loading state: ",a),console.log("contacts data: ",d),console.log("error state: ",m),(0,t.useEffect)((function(){fetch("".concat(i._,"/api/products/contacts/")).then((function(e){return e.json()})).then((function(e){e.response&&h(e.data)})).catch((function(e){return u(e)})).finally((function(){return n(!1)}))}),[]),(0,l.jsxs)("div",{children:[(0,l.jsx)(s.Z,{}),(0,l.jsxs)("div",{className:"content_container",children:[a&&(0,l.jsx)("div",{className:"message__container",children:(0,l.jsx)(r.Z,{})}),m&&(0,l.jsx)("div",{className:"message__container",children:(0,l.jsx)(c.Z,{message:"No internet connecting",type:"error",showIcon:!0})}),!a&&!m&&(0,l.jsx)("div",{className:"content__wrapper",children:(0,l.jsxs)("div",{className:"contact_variants",children:[(0,l.jsx)("div",{className:"contact_group_title",children:"Habarlashmak \xfc\xe7in:"}),(0,l.jsx)("div",{className:"contact_variant",children:(0,l.jsxs)("a",{href:"tel:".concat(d.mobile),children:[(0,l.jsx)("img",{src:"/telephone.png",width:"30px",alt:"phone logo"}),(0,l.jsx)("span",{children:d.mobile})]})}),(0,l.jsx)("div",{className:"contact_variant",children:(0,l.jsxs)("a",{href:"https://imo.im/",target:"_blanck",children:[(0,l.jsx)("img",{src:"/imo.png",width:"30px",alt:"phone logo"}),(0,l.jsx)("span",{children:d.imo})]})}),(0,l.jsx)("div",{className:"contact_variant",target:"_blanck",children:(0,l.jsxs)("a",{href:"https://www.instagram.com/rysgal_mebel",children:[(0,l.jsx)("img",{src:"/inst.png",width:"30px",alt:"inst logo"}),(0,l.jsx)("span",{children:d.instagram})]})}),(0,l.jsx)("div",{className:"contact_variant",children:(0,l.jsxs)("a",{href:"https://telegram.org/",target:"_blanck",children:[(0,l.jsx)("img",{src:"/telegram.png",width:"30px",alt:"inst logo"}),(0,l.jsx)("span",{children:d.telegram})]})})]})})]})]})}},4422:function(e,a,n){"use strict";n.d(a,{Fo:function(){return t},MF:function(){return i},mN:function(){return r}});var s=n(3967),t=function(e){var a=localStorage.getItem("like");if(a){var n=JSON.parse(a);n.push(e),localStorage.setItem("like",JSON.stringify(n))}else{var t=[];t.push(e),localStorage.setItem("like",JSON.stringify(t))}return{type:s.rU,payload:e}},i=function(e){var a=localStorage.getItem("like"),n=JSON.parse(a);return localStorage.setItem("like",JSON.stringify(n.filter((function(a){return a.prod_id!==e})))),{type:s.vF,payload:e}},r=function(e){return{type:s.tR,payload:e}}},8113:function(e,a,n){"use strict";n.d(a,{_:function(){return s}});var s="http://backend.rysgal-mebel.com"},9233:function(e,a,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/contacts",function(){return n(6355)}])},6538:function(e){e.exports={button:"button_button__pG_d_"}},5567:function(e){e.exports={container:"header_container__xYHxC",header:"header_header__U_Kza",sec1:"header_sec1__VJp8a",gif_section:"header_gif_section__3YVkV",navbar:"header_navbar__dOxSn",navbar_sec:"header_navbar_sec__6Iiy6",navbar_title:"header_navbar_title__HVavK",prof:"header_prof__69Sx0",profile_link:"header_profile_link__9pMuG",sec2:"header_sec2__HogPU",search_section:"header_search_section__CbajW",search:"header_search__l3PZ3",cart:"header_cart__bWN1U",magazin_modal:"header_magazin_modal__MMaLK",magazin_modal__close:"header_magazin_modal__close__8zBOl",magazin_modal__container:"header_magazin_modal__container__04Gcy",karta_modal:"header_karta_modal__GBbse",category__list_show:"header_category__list_show__nPgfa",cat_item:"header_cat_item__zydrs",subcat_item:"header_subcat_item__bjsq3",like_icon:"header_like_icon__aiXA2",like_count:"header_like_count__lvtaq",like_section:"header_like_section__5Si3n"}}},function(e){e.O(0,[128,840,189,774,888,179],(function(){return a=9233,e(e.s=a);var a}));var a=e.O();_N_E=a}]);