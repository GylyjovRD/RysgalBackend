(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[277],{3375:function(e,i,n){"use strict";n.r(i),n.d(i,{default:function(){return g}});var t=n(6672),r=n.n(t),a=(n(8741),{src:"/_next/static/media/up-arrow.9a9fd938.png",height:512,width:512,blurDataURL:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAMAAADz0U65AAAAIVBMVEVMaXEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC+JJ50AAAACnRSTlMAN6tOnSz8zsEI9JH7fQAAAAlwSFlzAAAOxAAADsQBlSsOGwAAADJJREFUeJwdiQkKADAIw1J1h/3/g4crhEAKIPG39l5j+V5PqwMngCaCni/sCZQlF5D5eRb6AKtUNdbTAAAAAElFTkSuQmCC"}),o={src:"/_next/static/media/down-arrow.45481f21.png",height:512,width:512,blurDataURL:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAMAAADz0U65AAAAGFBMVEVMaXEAAAAAAAAAAAAAAAAAAAAAAAAAAACrC2ehAAAAB3RSTlMAMcibQK1Lo1sskwAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAC9JREFUeJwlycENADAIw0AToNl/4yridZINb2Ae0J5xA6y9EfZsgbLKkiupfELFDxYLAINXC5N8AAAAAElFTkSuQmCC"},s=n(9473),l=n(7294),_=n(1163),d=n.n(_),c=n(5132),u=n(8113),p=n(1664),m=n.n(p),A=n(9669),f=n.n(A),h=n(5893);function g(){var e=(0,l.useState)([]),i=e[0],n=e[1],t=(0,l.useState)(null),_=t[0],p=t[1],A=(0,l.useState)(null),g=A[0],v=A[1],x=(0,l.useState)(!1),j=x[0],y=x[1],N=(0,l.useState)(null),w=N[0],C=N[1],b=(0,s.v9)((function(e){return e.user.token})),k=(0,s.v9)((function(e){return e.user.user_profil})),S=(0,s.I0)();(0,l.useEffect)((function(){if(null!==b&&"undefined"!==b||localStorage.getItem("token")){var e=b||localStorage.getItem("token");S(function(e){return function(i){fetch("".concat(u._,"/api/auth/profile-create/"),{method:"GET",headers:{"Content-Type":"application/json",Authorization:"Bearer ".concat(e)}}).then((function(e){return e.json()})).then((function(e){return i((0,c.et)(e.data))})).catch((function(e){return console.log(e)}))}}(e)),fetch(u._+"/api/order/order-list/",{method:"GET",headers:{"Content-Type":"application/json",Authorization:"Bearer ".concat(e)}}).then((function(e){return e.json()})).then((function(e){return n(e.data)})).catch((function(e){return console.log(e)}))}else d().push("/login")}),[]),console.log("Order List :",i);return(0,h.jsx)("div",{className:r().profile_page,children:(0,h.jsxs)("div",{className:r().profile_page__container,children:[(0,h.jsxs)("div",{className:r().profile_page__header,children:[(0,h.jsx)(m(),{href:"/",children:(0,h.jsx)("a",{children:(0,h.jsx)("img",{src:"/left-arrow.png",width:"32px",height:"28px"})})}),(0,h.jsxs)("div",{style:{display:"flex",alignItems:"center",gap:"0.5rem",backgroundColor:"rgba(198,198,0,0.5)",padding:"0.5rem 1rem",borderRadius:"10px",fontSize:"1.2rem"},onClick:function(){d().push("/"),S((0,c.MY)())},children:[(0,h.jsx)("span",{children:"Profilden chykmak"}),(0,h.jsx)("img",{src:"/logout.png",width:"34px",height:"28px"})]})]}),(0,h.jsxs)("div",{className:r().profil_section,children:[(0,h.jsx)("div",{className:r().image__section,children:(0,h.jsxs)("div",{className:r().prof_image,children:[j?(0,h.jsx)("input",{type:"file",onChange:function(e){return C(e.target.files[0])}}):(0,h.jsx)("img",{src:"".concat(u._).concat(k?k.image:"/"),width:1,height:1}),(0,h.jsx)("div",{className:r().image_title,children:null!==k&&void 0!==k&&k.fullname?null===k||void 0===k?void 0:k.fullname:null})]})}),(0,h.jsxs)("div",{className:r().user_info_section,children:[(0,h.jsx)("h2",{children:"Maglumatlarym"}),(0,h.jsxs)("div",{className:r().user_info_section__form,children:[(0,h.jsx)("span",{children:"Doly adynyz"}),j?(0,h.jsx)("input",{name:"fullname",className:r().form_input,type:"text",onChange:function(e){return S((0,c.y3)(e.target.name,e.target.value))},value:null===k||void 0===k?void 0:k.fullname}):(0,h.jsx)("div",{className:r().form_input,children:null===k||void 0===k?void 0:k.fullname})]}),(0,h.jsxs)("div",{className:r().user_info_section__form,children:[(0,h.jsx)("span",{children:"Telefon belginiz"}),j?(0,h.jsx)("input",{disabled:!0,name:"mobile",className:r().form_input,type:"text",value:null===k||void 0===k?void 0:k.mobile}):(0,h.jsx)("div",{className:r().form_input,children:null===k||void 0===k?void 0:k.mobile})]}),(0,h.jsxs)("div",{className:r().user_info_section__form,children:[(0,h.jsx)("span",{children:"Sebit"}),j?(0,h.jsxs)("select",{name:"region",className:r().form_input,value:null===k||void 0===k?void 0:k.region,onChange:function(e){return S((0,c.y3)(e.target.name,e.target.value))},children:[(0,h.jsx)("option",{children:"Asgabat"}),(0,h.jsx)("option",{children:"Ahal"}),(0,h.jsx)("option",{children:"Balkan"}),(0,h.jsx)("option",{children:"Dashoguz"}),(0,h.jsx)("option",{children:"Lebap"}),(0,h.jsx)("option",{children:"Mary"})]}):(0,h.jsx)("div",{className:r().form_input,children:null===k||void 0===k?void 0:k.region})]}),(0,h.jsxs)("div",{className:r().user_info_section__form,children:[(0,h.jsx)("span",{children:"E-mail pochtanyz"}),j?(0,h.jsx)("input",{name:"email",className:r().form_input,type:"text",value:null===k||void 0===k?void 0:k.email,onChange:function(e){return S((0,c.y3)(e.target.name,e.target.value))}}):(0,h.jsx)("div",{className:r().form_input,children:null===k||void 0===k?void 0:k.email})]}),(0,h.jsxs)("div",{className:r().user_info_section__form,children:[(0,h.jsx)("span",{children:"Salgy 1"}),j?(0,h.jsx)("input",{name:"address_line_1",className:r().form_input,type:"text",value:null===k||void 0===k?void 0:k.address_line_1,onChange:function(e){return S((0,c.y3)(e.target.name,e.target.value))}}):(0,h.jsx)("div",{className:r().form_input,children:null===k||void 0===k?void 0:k.address_line_1})]}),(0,h.jsxs)("div",{className:r().user_info_section__form,children:[(0,h.jsx)("span",{children:"Salgy 2"}),j?(0,h.jsx)("input",{name:"address_line_2",className:r().form_input,type:"text",value:null===k||void 0===k?void 0:k.address_line_2,onChange:function(e){return S((0,c.y3)(e.target.name,e.target.value))}}):(0,h.jsx)("div",{className:r().form_input,children:null===k||void 0===k?void 0:k.address_line_2})]})]})]}),(0,h.jsx)("div",{className:r().btn_section,children:j?(0,h.jsx)("button",{onClick:function(){var e=new FormData;w&&e.append("image",w),k.fullname&&e.append("fullname",k.fullname),k.region&&e.append("region",k.region),k.email&&e.append("email",k.email),k.address_line_1&&e.append("address_line_1",k.address_line_1),k.address_line_2&&e.append("address_line_2",k.address_line_2),f()({url:"".concat(u._,"/api/auth/profile-create/"),method:"PUT",headers:{"Content-Type":"multipart/from-data",Authorization:"Bearer ".concat(b)},data:e}).then((function(e){console.log(e.data)})),console.log("Profile info update button click"),console.log("user profile: ",k),y(!1)},children:"Save"}):(0,h.jsx)("button",{onClick:function(){return y(!0)},children:"Duzeltmek"})}),(0,h.jsxs)("div",{className:r().history,children:[(0,h.jsx)("h2",{children:"Onki satyn alynan harytlar"}),(0,h.jsx)("div",{className:r().history_view,children:(null===i||void 0===i?void 0:i.length)>0?i.map((function(e,i){return(0,h.jsxs)(h.Fragment,{children:[(0,h.jsxs)("div",{className:r().history_item,children:[(0,h.jsxs)("div",{className:r().id,children:[" ",i+1,"."]}),(0,h.jsx)("div",{className:r().date,children:e.created_at}),(0,h.jsxs)("div",{className:r().status,children:["Status ",e.status]}),(0,h.jsxs)("div",{className:r().payment,children:["Tolegin gornushi ",e.payment_type]}),(0,h.jsxs)("div",{className:r().region,children:["Region ",e.region]}),(0,h.jsxs)("div",{className:r().address,children:["Address ",e.address]}),(0,h.jsx)("div",{className:r().action,onClick:function(){return i=e.id,void(_!==i?(console.log(b),p(i),fetch(u._+"/api/order/order-detail/"+i+"/",{method:"GET",headers:{"Content-Type":"application/json",Authorization:"Bearer ".concat(b)}}).then((function(e){return e.json()})).then((function(e){return v(e.data)})).catch((function(e){return console.log(e)}))):p(null));var i},children:_===e.id?(0,h.jsx)("img",{src:a,width:26,height:26}):(0,h.jsx)("img",{src:o,width:26,height:26})})]},e.id),_===e.id&&(0,h.jsxs)("div",{className:r().order_detail,children:[g&&g.items.map((function(e,i){return(0,h.jsxs)("div",{className:r().order_detail__item,children:[(0,h.jsx)("div",{className:r().oder_item__image,children:(0,h.jsx)("img",{src:u._+e.product.main_image,width:50,height:50,alt:"mebel"})}),(0,h.jsx)("div",{className:r().order_item__title,children:e.product.title_tm}),(0,h.jsxs)("div",{className:r().order_item__qty,children:["sany: ",e.qty]}),(0,h.jsxs)("div",{className:r().order_item__price,children:["Harydyn bahasy: ",e.product_price]})]},i)})),(0,h.jsx)("div",{className:r().order_item__total_price,children:(0,h.jsxs)("div",{children:["Total Price: ",null===g||void 0===g?void 0:g.total_price]})})]})]})})):(0,h.jsx)("h2",{children:"Sargyt edilen haryt yok"})})]})]})})}},5132:function(e,i,n){"use strict";n.d(i,{BI:function(){return l},MY:function(){return a},et:function(){return o},pH:function(){return r},pY:function(){return _},y3:function(){return s}});var t=n(3967),r=function(e){return localStorage.setItem("token",e),{type:t.Ys,payload:e}},a=function(){return localStorage.removeItem("token"),{type:t.z7}},o=function(e){return{type:t.hH,payload:e}},s=function(e,i){return{type:t.Zo,name:e,value:i}},l=function(e){return{type:t.n0,payload:e}},_=function(e){return{type:t.MK,payload:e}}},8113:function(e,i,n){"use strict";n.d(i,{_:function(){return t}});var t="http://backend.rysgal-mebel.com"},9344:function(e,i,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/profile",function(){return n(3375)}])},8741:function(){"use strict"},6672:function(e){e.exports={profile_page:"profile_profile_page__0TSEU",profile_page__container:"profile_profile_page__container__5br58",profile_page__header:"profile_profile_page__header__rqj48",profil_section:"profile_profil_section__NPGxJ",image__section:"profile_image__section__7TAr5",prof_image:"profile_prof_image__XDWik",image_title:"profile_image_title__TFtiK",user_info_section:"profile_user_info_section__tJPr3",user_info_section__form:"profile_user_info_section__form__4lCUM",btn_section:"profile_btn_section___3WcL",history:"profile_history__Ue4Cz",history_view:"profile_history_view__iy90d",history_item:"profile_history_item__8RIl0",id:"profile_id__cA5n8",status:"profile_status__Oj_o5",payment:"profile_payment__yrgpy",region:"profile_region__CDLtX",address:"profile_address__nz9fX",action:"profile_action__kEOnK",order_detail:"profile_order_detail__jnjk9",order_detail__item:"profile_order_detail__item__X0Ky_",oder_item__image:"profile_oder_item__image__dhefV",order_item__title:"profile_order_item__title___6M_c",order_item__qty:"profile_order_item__qty__uhgiR",order_item__price:"profile_order_item__price__mHsqS",order_item__total_price:"profile_order_item__total_price__1_zkG",form_input:"profile_form_input__w5mpr"}}},function(e){e.O(0,[630,774,888,179],(function(){return i=9344,e(e.s=i);var i}));var i=e.O();_N_E=i}]);