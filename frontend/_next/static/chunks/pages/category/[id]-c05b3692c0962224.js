(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[300],{1877:function(t,e,n){"use strict";n.r(e),n.d(e,{default:function(){return p}});var c=n(29),o=n(7794),r=n.n(o),s=n(1163),i=n(7294),a=n(9473),u=n(1697),d=n(2360),l=n(3838),f=n(8113),_=n(5893),p=function(){var t,e,n,o,p,v,g=(0,s.useRouter)().asPath,h=(0,a.v9)((function(t){return t.category.data})),m=(0,a.v9)((function(t){return t.selectcategory})),y=(0,i.useState)({}),x=y[0],j=y[1],N=(0,i.useState)({}),b=N[0],w=N[1],E=(0,i.useState)({}),k=E[0],S=E[1],P=(0,i.useState)(""),T=P[0],C=P[1],F=(0,a.I0)();return console.log("category list: ",h),(0,i.useEffect)((function(){var t,e;F((t=m.selected_category,e=T,function(n){fetch("".concat(f._,"/api/products/product-list/?limit=10&offset=0&category=").concat(t,"&brand=").concat(e)).then((function(t){return t.json()})).then((function(t){return n((0,l.F)(t.data))})).catch((function(t){return console.log(t)}))}))}),[T]),(0,i.useEffect)((0,c.Z)(r().mark((function t(){var e,n,c,o,s,i,a,u,d;return r().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return n=g.split("/")[2],console.log("useeffect ichi: ",n),t.next=4,fetch("".concat(f._,"/api/products/product-list/?category=").concat(n,"&limit=10&offset=0"));case 4:return c=t.sent,t.next=7,c.json();case 7:return o=t.sent,t.next=10,fetch("".concat(f._,"/api/products/brands/"));case 10:return s=t.sent,t.next=13,s.json();case 13:return i=t.sent,t.next=16,fetch("".concat(f._,"/api/products/categories/"));case 16:return a=t.sent,t.next=19,a.json();case 19:u=t.sent,null===(e=u.data)||void 0===e||e.map((function(t){t.subcategories.map((function(t){t.id==n&&(d=t)}))})),j(o),w(i),S(d);case 24:case"end":return t.stop()}}),t)}))),[]),console.log("Products: ",x),console.log("Brands: ",b),console.log("selected category: ",k),console.log("category id: ",g.split("/")[2]),(0,_.jsxs)("div",{className:"category_products",children:[(0,_.jsx)(d.Z,{}),(0,_.jsxs)("div",{className:"category_products__container",children:[(0,_.jsxs)("div",{className:"category__header",children:[(0,_.jsx)("div",{className:"category__title",children:null===k||void 0===k?void 0:k.title_tm}),(0,_.jsxs)("div",{className:"category__products_count",children:["sany: ",null===(t=x.data)||void 0===t?void 0:t.count]})]}),(0,_.jsxs)("div",{className:"category_products_main",children:[(0,_.jsx)("div",{className:"category__products_filter",children:null===b||void 0===b||null===(e=b.data)||void 0===e?void 0:e.map((function(t){return(0,_.jsxs)("div",{children:[(0,_.jsx)("input",{type:"checkbox",id:t.id,onChange:function(){T===t.id?C(""):C(t.id)}}),(0,_.jsx)("label",{className:"brand_label",htmlFor:t.id,children:t.title})]},t.id+"i")}))}),(0,_.jsx)("div",{className:"category__produsts_view",children:(null===x||void 0===x||null===(n=x.data)||void 0===n||null===(o=n.results)||void 0===o?void 0:o.length)>0?null===x||void 0===x||null===(p=x.data)||void 0===p||null===(v=p.results)||void 0===v?void 0:v.map((function(t){return(0,_.jsx)(u.Z,{prod_id:t.id,img_url:t.main_image,title:t.title_tm,price:t.get_price,desc:t.description_tm},t.id)})):(0,_.jsx)("p",{style:{textAlign:"center",fontSize:"1.5rem",paddingTop:"2rem"},children:"No products"})})]})]})]})}},3838:function(t,e,n){"use strict";n.d(e,{F:function(){return r},T:function(){return o}});var c=n(3967),o=function(t){return{type:c.tJ,payload:t}},r=function(t){return{type:c.Rh,payload:t}}},785:function(t,e,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/category/[id]",function(){return n(1877)}])}},function(t){t.O(0,[128,294,774,888,179],(function(){return e=785,t(t.s=e);var e}));var e=t.O();_N_E=e}]);