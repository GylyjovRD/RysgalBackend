(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[459],{519:function(n,e,t){"use strict";t.r(e),t.d(e,{default:function(){return _}});var o=t(9499),r=t(1163),s=t.n(r),i=t(7294),a=t(9473),c=t(9439),u=t(5132),l=t(8113),f=function(n){return function(e){e((0,c.K)(!0)),fetch("".concat(l._,"/api/auth/login/"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)}).then((function(n){if(200===n.status)return n.json();console.log(n)})).then((function(n){console.log("login edilende gelyan jogap",n),e((0,u.pH)(n.access)),r.Router.push("/profile")})).catch((function(n){return console.log(n)})).finally((function(){return e((0,c.K)(!1))}))}},p=t(6722),d=t.n(p),g=t(5893);function y(n,e){var t=Object.keys(n);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(n);e&&(o=o.filter((function(e){return Object.getOwnPropertyDescriptor(n,e).enumerable}))),t.push.apply(t,o)}return t}function h(n){for(var e=1;e<arguments.length;e++){var t=null!=arguments[e]?arguments[e]:{};e%2?y(Object(t),!0).forEach((function(e){(0,o.Z)(n,e,t[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(n,Object.getOwnPropertyDescriptors(t)):y(Object(t)).forEach((function(e){Object.defineProperty(n,e,Object.getOwnPropertyDescriptor(t,e))}))}return n}function _(){var n=(0,i.useState)(!0),e=n[0],t=n[1],o=(0,i.useState)({username:"+993",passowrd:"",conf_pasword:""}),c=o[0],p=o[1],y=(0,a.v9)((function(n){return n})),_=y.user,m=y.loading,b=(0,a.I0)();(0,i.useEffect)((function(){_.token&&_.token.length>10&&s().push("/profile")}),[_.token]);var j=(0,i.useState)(""),v=j[0],x=j[1];console.log(_.is_sms_verify);return(0,i.useEffect)((function(){"error"===_.is_sms_verify&&b(function(n){return function(e){console.log("registrasiya fetchden on: ",n),fetch("".concat(l._,"/api/auth/resend-sms/"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)}).then((function(n){return n.json()})).then((function(n){console.log(n),e(isSmsResend())})).catch((function(n){return console.log(n)}))}}({mobile:c.username.slice(-8)})),"success"===_.is_sms_verify&&(console.log("registrasiya bashlady"),b(function(n){return function(e){console.log("registrasiya fetchden on: ",JSON.stringify(n)),fetch("".concat(l._,"/api/auth/register/"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)}).then((function(n){return n.json()})).then((function(n){e((0,u.pH)(n.data.token)),r.Router.push("/profile")})).catch((function(n){return console.log(n)}))}}({username:c.username.slice(-8),password:c.passowrd})))}),[_.is_sms_verify]),(0,g.jsx)("div",{className:d().login,children:_.is_sms_sent?(0,g.jsx)("div",{className:d().login__container,children:(0,g.jsxs)("div",{style:{display:"flex",flexDirection:"column",padding:"0.5rem 2rem"},children:[(0,g.jsx)("p",{style:{fontSize:"18px",fontWeight:"600",padding:"0",margin:"0"},children:"gelen sms cody yazyn"}),(0,g.jsx)("input",{type:"text",value:v,onChange:function(n){return x(n.target.value)}}),(0,g.jsx)("button",{onClick:function(){b(function(n){return function(e){console.log("registrasiya fetchden on: ",n),fetch("".concat(l._,"/api/auth/verify-code/"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)}).then((function(n){return n.json()})).then((function(n){console.log(n),e((0,u.pY)(n.response))})).catch((function(n){return console.log(n)}))}}({mobile:c.username.slice(-8),sms_code:Number(v)}))},children:"ugratmak"}),(0,g.jsx)("p",{style:{padding:"0",margin:"0"},children:"Tazeden sms ugratmak"})]})}):(0,g.jsxs)("div",{className:d().login__container,children:[(0,g.jsx)("div",{className:d().login__title,children:e?"SING IN":"SING UP"}),(0,g.jsxs)("div",{className:d().login__form,children:[(0,g.jsx)("p",{children:"Telefon belgi"}),(0,g.jsx)("input",{type:"text",value:c.username,onChange:function(n){return p(h(h({},c),{},{username:n.target.value}))},name:"phone_number"}),(0,g.jsx)("p",{children:"Parol"}),(0,g.jsx)("input",{type:"password",name:"password",value:c.passowrd,onChange:function(n){return p(h(h({},c),{},{passowrd:n.target.value}))}}),!e&&(0,g.jsxs)(g.Fragment,{children:[(0,g.jsx)("p",{children:"Parolynyzy gaytalan"}),(0,g.jsx)("input",{type:"password",name:"conf_password",value:c.conf_pasword,onChange:function(n){return p(h(h({},c),{},{conf_pasword:n.target.value}))}})]}),(0,g.jsx)("button",{className:d().btn,onClick:function(){console.log("On registrasiya bolanmy?",e),console.log("User data: ",c),e?c.passowrd.length>4?b(f({username:c.username.slice(-8),password:c.passowrd})):alert("paroly gysga yazdynyz"):c.passowrd===c.conf_pasword&&c.passowrd.length>4?(console.log("registrasiya zapros",c.username.slice(-8)),b(function(n){return function(e){fetch("".concat(l._,"/api/auth/register-mobile/"),{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(n)}).then((function(n){return n.json()})).then((function(n){"success"===n.response&&e((0,u.BI)(!0))})).catch((function(n){return console.log(n)}))}}({mobile:c.username.slice(-8)}))):alert("parolynyzda yalnyshlyk bar")},children:m?"...loading":"Gir"})]}),e?(0,g.jsxs)("div",{className:d().desc,children:["Eger registrasiya bolmadyk boslanyz onda"," ",(0,g.jsx)("span",{style:{cursor:"pointer"},onClick:function(){return t(!1)},children:"Registrasiya"})," basyn!"]}):(0,g.jsxs)("div",{className:d().desc,children:["Eger registrasiya bolan boslanyz onda"," ",(0,g.jsx)("span",{onClick:function(){return t(!0)},children:"Login"})," basyn!"]})]})})}},9439:function(n,e,t){"use strict";t.d(e,{K:function(){return r}});var o=t(3967),r=function(n){return{type:o.cS,payload:n}}},5132:function(n,e,t){"use strict";t.d(e,{BI:function(){return c},MY:function(){return s},et:function(){return i},pH:function(){return r},pY:function(){return u},y3:function(){return a}});var o=t(3967),r=function(n){return localStorage.setItem("token",n),{type:o.Ys,payload:n}},s=function(){return localStorage.removeItem("token"),{type:o.z7}},i=function(n){return{type:o.hH,payload:n}},a=function(n,e){return{type:o.Zo,name:n,value:e}},c=function(n){return{type:o.n0,payload:n}},u=function(n){return{type:o.MK,payload:n}}},8113:function(n,e,t){"use strict";t.d(e,{_:function(){return o}});var o="http://backend.rysgal-mebel.com"},6429:function(n,e,t){(window.__NEXT_P=window.__NEXT_P||[]).push(["/login",function(){return t(519)}])},6722:function(n){n.exports={login:"login_login___x1HT",login__container:"login_login__container__LIP31",login__title:"login_login__title__qExF3",login__form:"login_login__form___Rn8R",btn:"login_btn__n1fd_",desc:"login_desc__TctLt"}},1163:function(n,e,t){n.exports=t(1587)}},function(n){n.O(0,[774,888,179],(function(){return e=6429,n(n.s=e);var e}));var e=n.O();_N_E=e}]);