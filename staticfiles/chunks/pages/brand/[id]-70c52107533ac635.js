(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[563],{6717:function(t,e,n){"use strict";n.r(e);var i=n(29),s=n(7794),r=n.n(s),a=n(1163),d=n(7294),c=n(1697),l=n(2360),o=n(8113),u=n(5893);e.default=function(){var t,e,n,s=(0,d.useState)({}),_=s[0],p=s[1],m=(0,d.useState)({}),f=m[0],x=m[1],h=(0,d.useState)([]),v=h[0],b=h[1];(0,a.useRouter)().asPath;return(0,d.useEffect)((0,i.Z)(r().mark((function t(){var e,n,i,s,a,d,c,l;return r().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,fetch("".concat(o._,"/api/products/product-list/?brand=").concat(id,"&limit=10&offset=0"));case 2:return n=t.sent,t.next=5,n.json();case 5:return i=t.sent,t.next=8,fetch("".concat(o._,"/api/products/brands/"));case 8:return s=t.sent,t.next=11,s.json();case 11:return a=t.sent,t.next=14,fetch("".concat(o._,"/api/products/categories/"));case 14:return d=t.sent,t.next=17,d.json();case 17:c=t.sent,l={},null===a||void 0===a||null===(e=a.data)||void 0===e||e.map((function(t){t.id==id&&(l=t)})),p(i),x(l),b(c);case 23:case"end":return t.stop()}}),t)}))),[]),(0,u.jsxs)("div",{className:"brand__products",children:[(0,u.jsx)(l.Z,{}),(0,u.jsxs)("div",{className:"brand__products_container",children:[(0,u.jsxs)("div",{className:"brand__products_header",children:[(0,u.jsx)("div",{className:"brand__product_title",children:(null===f||void 0===f?void 0:f.title)&&f.title}),(0,u.jsxs)("div",{style:{display:"flex",alignItems:"end",fontSize:"1.1rem",fontWeight:600,borderBottom:"1px solid black"},children:["sany: ",null===_||void 0===_||null===(t=_.data)||void 0===t?void 0:t.count]})]}),(0,u.jsxs)("div",{className:"brand__products_main",children:[(0,u.jsx)("div",{className:"brand__products_filter",children:v&&(null===(e=v.data)||void 0===e?void 0:e.map((function(t){return(0,u.jsxs)("div",{className:"filter__item",children:[(0,u.jsx)("p",{style:{borderBottom:"1px solid black"},children:t.title_tm}),(0,u.jsx)("ul",{style:{listStyle:"none",padding:"0.5rem 1rem",fontSize:"1rem",fontWeight:"normal"},children:t.subcategories.map((function(t){return(0,u.jsxs)("li",{style:{marginBottom:"8px",marginLeft:"-10px"},children:[(0,u.jsx)("input",{type:"checkbox",id:t.id})," ",(0,u.jsx)("label",{htmlFor:t.id,children:t.title_tm})]},t.id)}))})]},t.id)})))}),(0,u.jsx)("div",{className:"brand__products_view",children:(null===(n=_.data)||void 0===n?void 0:n.results)&&_.data.results.map((function(t){return(0,u.jsx)(c.Z,{prod_id:t.id,img_url:t.main_image,title:t.title_tm,price:t.get_price,desc:t.description_tm},t.id)}))})]})]})]})}},8757:function(t,e,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/brand/[id]",function(){return n(6717)}])}},function(t){t.O(0,[128,294,774,888,179],(function(){return e=8757,t(t.s=e);var e}));var e=t.O();_N_E=e}]);