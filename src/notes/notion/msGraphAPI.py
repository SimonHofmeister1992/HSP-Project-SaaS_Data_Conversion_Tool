<!DOCTYPE html>
<html class="with-system-footer with-system-footer" lang="en"><head prefix="og: http://ogp.me/ns#">
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">

<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="Edit · src/notes/oneNote/msGraphAPI.py · master · Simon1 Hofmeister / HSP-SS20-Schildgen-SaaS" property="og:title">
<meta content="GitLab OTH Regensburg" property="og:description">
<meta content="https://gitlab.oth-regensburg.de/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/edit/master/src/notes/oneNote/msGraphAPI.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="Edit · src/notes/oneNote/msGraphAPI.py · master · Simon1 Hofmeister / HSP-SS20-Schildgen-SaaS" property="twitter:title">
<meta content="GitLab OTH Regensburg" property="twitter:description">
<meta content="https://gitlab.oth-regensburg.de/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="twitter:image">

<title>Edit · src/notes/oneNote/msGraphAPI.py · master · Simon1 Hofmeister / HSP-SS20-Schildgen-SaaS · GitLab</title>
<meta content="GitLab OTH Regensburg" name="description">
<link rel="shortcut icon" type="image/png" href="https://gitlab.oth-regensburg.de/assets/favicon-7901bd695fb93edb07975966062049829afb56cf11511236e61bcf425070e36e.png" id="favicon" data-original-href="/assets/favicon-7901bd695fb93edb07975966062049829afb56cf11511236e61bcf425070e36e.png">

<link rel="stylesheet" media="all" href="msGraphAPI_files/application-30a9dffe86b597151eff49443097496f0d1014bb6695a2f6.css">


<link rel="stylesheet" media="all" href="msGraphAPI_files/white-3a5ccf16b3cb943249b10b6fd8a260ac3c8a79ea432c44c3886d1d.css">

<script>
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https://gitlab.oth-regensburg.de/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=50;gon.asset_host=null;gon.webpack_public_path="/assets/webpack/";gon.relative_url_root="";gon.shortcuts_path="/help/shortcuts";gon.user_color_scheme="white";gon.gitlab_url="https://gitlab.oth-regensburg.de";gon.revision="f0a10848821";gon.gitlab_logo="/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png";gon.sprite_icons="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg";gon.sprite_file_icons="/assets/file_icons-7262fc6897e02f1ceaf8de43dc33afa5e4f9a2067f4f68ef77dcc87946575e9e.svg";gon.emoji_sprites_css_path="/assets/emoji_sprites-289eccffb1183c188b630297431be837765d9ff4aed6130cf738586fb307c170.css";gon.test_env=false;gon.disable_animations=null;gon.suggested_label_colors={"#0033CC":"UA blue","#428BCA":"Moderate blue","#44AD8E":"Lime green","#A8D695":"Feijoa","#5CB85C":"Slightly desaturated green","#69D100":"Bright green","#004E00":"Very dark lime green","#34495E":"Very dark desaturated blue","#7F8C8D":"Dark grayish cyan","#A295D6":"Slightly desaturated blue","#5843AD":"Dark moderate blue","#8E44AD":"Dark moderate violet","#FFECDB":"Very pale orange","#AD4363":"Dark moderate pink","#D10069":"Strong pink","#CC0033":"Strong red","#FF0000":"Pure red","#D9534F":"Soft red","#D1D100":"Strong yellow","#F0AD4E":"Soft orange","#AD8D43":"Dark moderate orange"};gon.first_day_of_week=0;gon.ee=true;gon.current_user_id=1710;gon.current_username="hos47096";gon.current_user_fullname="Simon1 Hofmeister";gon.current_user_avatar_url=null;gon.features={"snippetsVue":true,"monacoBlobs":true,"monacoCi":false,"snippetsEditVue":false,"webperfExperiment":false,"snippetsBinaryBlob":false};
//]]>
</script>


<script src="msGraphAPI_files/runtime.js" defer="defer"></script>
<script src="msGraphAPI_files/main.js" defer="defer"></script>
<script src="msGraphAPI_files/commons-pages_003.js" defer="defer"></script>
<script src="msGraphAPI_files/commons-pages.js" defer="defer"></script>
<script src="msGraphAPI_files/commons-pages_002.js" defer="defer"></script>
<script src="msGraphAPI_files/pages.js" defer="defer"></script>

<script>
//<![CDATA[
window.uploads_path = "/hos47096/hsp-ss20-schildgen-saas/uploads";



//]]>
</script>
<meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="K1T+VEI/B4gC4kjDr3LoIw3qYF56oU7q+KPQOqDOer3tQ5UhRZlMF799td7f0JA9R4hLPcNtslnHOnrwZ259hw==">
<meta name="csp-nonce">
<meta name="action-cable-url" content="/-/cable">
<meta content="origin-when-cross-origin" name="referrer">
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#474D57" name="theme-color">
<link rel="apple-touch-icon" type="image/x-icon" href="https://gitlab.oth-regensburg.de/assets/touch-icon-iphone-5a9cee0e8a51212e70b90c87c12f382c428870c0ff67d1eb034d884b78d2dae7.png">
<link rel="apple-touch-icon" type="image/x-icon" href="https://gitlab.oth-regensburg.de/assets/touch-icon-ipad-a6eec6aeb9da138e507593b464fdac213047e49d3093fc30e90d9a995df83ba3.png" sizes="76x76">
<link rel="apple-touch-icon" type="image/x-icon" href="https://gitlab.oth-regensburg.de/assets/touch-icon-iphone-retina-72e2aadf86513a56e050e7f0f2355deaa19cc17ed97bbe5147847f2748e5a3e3.png" sizes="120x120">
<link rel="apple-touch-icon" type="image/x-icon" href="https://gitlab.oth-regensburg.de/assets/touch-icon-ipad-retina-8ebe416f5313483d9c1bc772b5bbe03ecad52a54eba443e5215a22caed2a16a2.png" sizes="152x152">
<link color="rgb(226, 67, 41)" href="https://gitlab.oth-regensburg.de/assets/logo-d36b5212042cebc89b96df4bf6ac24e43db316143e89926c0db839ff694d2de4.svg" rel="mask-icon">
<meta content="/assets/msapplication-tile-1196ec67452f618d39cdd85e2e3a542f76574c071051ae7effbfde01710eb17d.png" name="msapplication-TileImage">
<meta content="#30353E" name="msapplication-TileColor">




<script charset="utf-8" src="msGraphAPI_files/vendors-select2.js"></script><style type="text/css">.toasted{padding:0 20px}.toasted.rounded{border-radius:24px}.toasted .primary,.toasted.toasted-primary{border-radius:2px;min-height:38px;line-height:1.1em;background-color:#353535;padding:0 20px;font-size:15px;font-weight:300;color:#fff;box-shadow:0 1px 3px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.24)}.toasted .primary.success,.toasted.toasted-primary.success{background:#4caf50}.toasted .primary.error,.toasted.toasted-primary.error{background:#f44336}.toasted .primary.info,.toasted.toasted-primary.info{background:#3f51b5}.toasted .primary .action,.toasted.toasted-primary .action{color:#a1c2fa}.toasted.bubble{border-radius:30px;min-height:38px;line-height:1.1em;background-color:#ff7043;padding:0 20px;font-size:15px;font-weight:300;color:#fff;box-shadow:0 1px 3px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.24)}.toasted.bubble.success{background:#4caf50}.toasted.bubble.error{background:#f44336}.toasted.bubble.info{background:#3f51b5}.toasted.bubble .action{color:#8e2b0c}.toasted.outline{border-radius:30px;min-height:38px;line-height:1.1em;background-color:#fff;border:1px solid #676767;padding:0 20px;font-size:15px;color:#676767;box-shadow:0 1px 3px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.24);font-weight:700}.toasted.outline.success{color:#4caf50;border-color:#4caf50}.toasted.outline.error{color:#f44336;border-color:#f44336}.toasted.outline.info{color:#3f51b5;border-color:#3f51b5}.toasted.outline .action{color:#607d8b}.toasted-container{position:fixed;z-index:10000}.toasted-container,.toasted-container.full-width{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column}.toasted-container.full-width{max-width:86%;width:100%}.toasted-container.full-width.fit-to-screen{min-width:100%}.toasted-container.full-width.fit-to-screen .toasted:first-child{margin-top:0}.toasted-container.full-width.fit-to-screen.top-right{top:0;right:0}.toasted-container.full-width.fit-to-screen.top-left{top:0;left:0}.toasted-container.full-width.fit-to-screen.top-center{top:0;left:0;-webkit-transform:translateX(0);transform:translateX(0)}.toasted-container.full-width.fit-to-screen.bottom-right{right:0;bottom:0}.toasted-container.full-width.fit-to-screen.bottom-left{left:0;bottom:0}.toasted-container.full-width.fit-to-screen.bottom-center{left:0;bottom:0;-webkit-transform:translateX(0);transform:translateX(0)}.toasted-container.top-right{top:10%;right:7%}.toasted-container.top-left{top:10%;left:7%}.toasted-container.top-center{top:10%;left:50%;-webkit-transform:translateX(-50%);transform:translateX(-50%)}.toasted-container.bottom-right{right:5%;bottom:7%}.toasted-container.bottom-left{left:5%;bottom:7%}.toasted-container.bottom-center{left:50%;-webkit-transform:translateX(-50%);transform:translateX(-50%);bottom:7%}.toasted-container.bottom-left .toasted,.toasted-container.top-left .toasted{float:left}.toasted-container.bottom-right .toasted,.toasted-container.top-right .toasted{float:right}.toasted-container .toasted{top:35px;width:auto;clear:both;margin-top:10px;position:relative;max-width:100%;height:auto;word-break:normal;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:justify;justify-content:space-between;box-sizing:inherit}.toasted-container .toasted .fa,.toasted-container .toasted .fab,.toasted-container .toasted .far,.toasted-container .toasted .fas,.toasted-container .toasted .material-icons,.toasted-container .toasted .mdi{margin-right:.5rem;margin-left:-.4rem}.toasted-container .toasted .fa.after,.toasted-container .toasted .fab.after,.toasted-container .toasted .far.after,.toasted-container .toasted .fas.after,.toasted-container .toasted .material-icons.after,.toasted-container .toasted .mdi.after{margin-left:.5rem;margin-right:-.4rem}.toasted-container .toasted .action{text-decoration:none;font-size:.8rem;padding:8px;margin:5px -7px 5px 7px;border-radius:3px;text-transform:uppercase;letter-spacing:.03em;font-weight:600;cursor:pointer}.toasted-container .toasted .action.icon{padding:4px;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:center}.toasted-container .toasted .action.icon .fa,.toasted-container .toasted .action.icon .material-icons,.toasted-container .toasted .action.icon .mdi{margin-right:0;margin-left:4px}.toasted-container .toasted .action.icon:hover{text-decoration:none}.toasted-container .toasted .action:hover{text-decoration:underline}@media only screen and (max-width:600px){#toasted-container{min-width:100%}#toasted-container .toasted:first-child{margin-top:0}#toasted-container.top-right{top:0;right:0}#toasted-container.top-left{top:0;left:0}#toasted-container.top-center{top:0;left:0;-webkit-transform:translateX(0);transform:translateX(0)}#toasted-container.bottom-right{right:0;bottom:0}#toasted-container.bottom-left{left:0;bottom:0}#toasted-container.bottom-center{left:0;bottom:0;-webkit-transform:translateX(0);transform:translateX(0)}#toasted-container.bottom-center,#toasted-container.top-center{-ms-flex-align:stretch!important;align-items:stretch!important}#toasted-container.bottom-left .toasted,#toasted-container.bottom-right .toasted,#toasted-container.top-left .toasted,#toasted-container.top-right .toasted{float:none}#toasted-container .toasted{border-radius:0}}</style><script charset="utf-8" src="msGraphAPI_files/monaco.js"></script><script charset="utf-8" src="msGraphAPI_files/vendors-monaco_editor_lite.js"></script><script charset="utf-8" src="msGraphAPI_files/commons-monaco_editor_lite-pages.js"></script><script charset="utf-8" src="msGraphAPI_files/monaco_editor_lite.js"></script><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .accessibilityHelpWidget {
	padding: 10px;
	vertical-align: middle;
	overflow: scroll;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-aria-container {
	position: absolute; /* try to hide from window but not from screen readers */
	left:-999em;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .bracket-match {
	box-sizing: border-box;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-menu .monaco-action-bar.vertical .action-label.hover {
	background-color: #EEE;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .monaco-editor-overlaymessage {
	padding-bottom: 8px;
}

@keyframes fadeIn {
	from { opacity: 0; }
	to { opacity: 1; }
}
.monaco-editor .monaco-editor-overlaymessage.fadeIn {
	animation: fadeIn 150ms ease-out;
}

@keyframes fadeOut {
	from { opacity: 1; }
	to { opacity: 0; }
}
.monaco-editor .monaco-editor-overlaymessage.fadeOut {
	animation: fadeOut 100ms ease-out;
}

.monaco-editor .monaco-editor-overlaymessage .message {
	padding: 1px 4px;
}

.monaco-editor .monaco-editor-overlaymessage .anchor {
	width: 0 !important;
	height: 0 !important;
	border-color: transparent;
	border-style: solid;
	z-index: 1000;
	border-width: 8px;
	position: absolute;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-action-bar {
	text-align: right;
	overflow: hidden;
	white-space: nowrap;
}

.monaco-action-bar .actions-container {
	display: flex;
	margin: 0 auto;
	padding: 0;
	width: 100%;
	justify-content: flex-end;
}

.monaco-action-bar.vertical .actions-container {
	display: inline-block;
}

.monaco-action-bar.reverse .actions-container {
	flex-direction: row-reverse;
}

.monaco-action-bar .action-item {
	cursor: pointer;
	display: inline-block;
	transition: transform 50ms ease;
	position: relative;  /* DO NOT REMOVE - this is the key to preventing the ghosting icon bug in Chrome 42 */
}

.monaco-action-bar .action-item.disabled {
	cursor: default;
}

.monaco-action-bar.animated .action-item.active {
	transform: scale(1.272019649, 1.272019649); /* 1.272019649 = √φ */
}

.monaco-action-bar .action-item .icon,
.monaco-action-bar .action-item .codicon {
	display: inline-block;
}

.monaco-action-bar .action-label {
	font-size: 11px;
	margin-right: 4px;
}

.monaco-action-bar .action-item.disabled .action-label,
.monaco-action-bar .action-item.disabled .action-label:hover {
	opacity: 0.4;
}

/* Vertical actions */

.monaco-action-bar.vertical {
	text-align: left;
}

.monaco-action-bar.vertical .action-item {
	display: block;
}

.monaco-action-bar.vertical .action-label.separator {
	display: block;
	border-bottom: 1px solid #bbb;
	padding-top: 1px;
	margin-left: .8em;
	margin-right: .8em;
}

.monaco-action-bar.animated.vertical .action-item.active {
	transform: translate(5px, 0);
}

.secondary-actions .monaco-action-bar .action-label {
	margin-left: 6px;
}

/* Action Items */
.monaco-action-bar .action-item.select-container {
	overflow: hidden; /* somehow the dropdown overflows its container, we prevent it here to not push */
	flex: 1;
	max-width: 170px;
	min-width: 60px;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-right: 10px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .lightbulb-glyph,
.monaco-editor .codicon-lightbulb {
	display: flex;
	align-items: center;
	justify-content: center;
	height: 16px;
	width: 20px;
	padding-left: 2px;
}

.monaco-editor .lightbulb-glyph:hover,
.monaco-editor .codicon-lightbulb:hover {
	cursor: pointer;
	/* transform: scale(1.3, 1.3); */
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .codelens-decoration {
	overflow: hidden;
	display: inline-block;
	text-overflow: ellipsis;
}

.monaco-editor .codelens-decoration > span,
.monaco-editor .codelens-decoration > a {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
	white-space: nowrap;
	vertical-align: sub;
}

.monaco-editor .codelens-decoration > a {
	text-decoration: none;
}

.monaco-editor .codelens-decoration > a:hover {
	cursor: pointer;
}

.monaco-editor .codelens-decoration .codicon {
	vertical-align: middle;
	color: currentColor !important;
}

.monaco-editor .codelens-decoration > a:hover .codicon::before {
	cursor: pointer;
}

@keyframes fadein {
	0% { opacity: 0; visibility: visible;}
	100% { opacity: 1; }
}

.monaco-editor .codelens-decoration.fadein {
	animation: fadein 0.1s linear;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-menu .monaco-action-bar.vertical {
	margin-left: 0;
	overflow: visible;
}

.monaco-menu .monaco-action-bar.vertical .actions-container {
	display: block;
}

.monaco-menu .monaco-action-bar.vertical .action-item {
	padding: 0;
	transform: none;
	display: flex;
}

.monaco-menu .monaco-action-bar.vertical .action-item.active {
	transform: none;
}

.monaco-menu .monaco-action-bar.vertical .action-menu-item {
	flex: 1 1 auto;
	display: flex;
	height: 2em;
	align-items: center;
	position: relative;
}

.monaco-menu .monaco-action-bar.vertical .action-label {
	flex: 1 1 auto;
	text-decoration: none;
	padding: 0 1em;
	background: none;
	font-size: 12px;
	line-height: 1;
}

.monaco-menu .monaco-action-bar.vertical .keybinding,
.monaco-menu .monaco-action-bar.vertical .submenu-indicator {
	display: inline-block;
	flex: 2 1 auto;
	padding: 0 1em;
	text-align: right;
	font-size: 12px;
	line-height: 1;
}

.monaco-menu .monaco-action-bar.vertical .submenu-indicator {
	height: 100%;
}

.monaco-menu .monaco-action-bar.vertical .submenu-indicator.codicon {
	font-size: 16px !important;
	display: flex;
	align-items: center;
}

.monaco-menu .monaco-action-bar.vertical .submenu-indicator.codicon::before {
	margin-left: auto;
	margin-right: -20px;
}

.monaco-menu .monaco-action-bar.vertical .action-item.disabled .keybinding,
.monaco-menu .monaco-action-bar.vertical .action-item.disabled .submenu-indicator {
	opacity: 0.4;
}

.monaco-menu .monaco-action-bar.vertical .action-label:not(.separator) {
	display: inline-block;
	box-sizing: border-box;
	margin: 0;
}

.monaco-menu .monaco-action-bar.vertical .action-item {
	position: static;
	overflow: visible;
}

.monaco-menu .monaco-action-bar.vertical .action-item .monaco-submenu {
	position: absolute;
}

.monaco-menu .monaco-action-bar.vertical .action-label.separator {
	padding: 0.5em 0 0 0;
	margin-bottom: 0.5em;
	width: 100%;
}

.monaco-menu .monaco-action-bar.vertical .action-label.separator.text {
	padding: 0.7em 1em 0.1em 1em;
	font-weight: bold;
	opacity: 1;
}

.monaco-menu .monaco-action-bar.vertical .action-label:hover {
	color: inherit;
}

.monaco-menu .monaco-action-bar.vertical .menu-item-check {
	position: absolute;
	visibility: hidden;
	width: 1em;
	height: 100%;
}

.monaco-menu .monaco-action-bar.vertical .action-menu-item.checked .menu-item-check {
	visibility: visible;
	display: flex;
	align-items: center;
	justify-content: center;
}

/* Context Menu */

.context-view.monaco-menu-container {
	outline: 0;
	border: none;
	animation: fadeIn 0.083s linear;
}

.context-view.monaco-menu-container :focus,
.context-view.monaco-menu-container .monaco-action-bar.vertical:focus,
.context-view.monaco-menu-container .monaco-action-bar.vertical :focus {
	outline: 0;
}

.monaco-menu .monaco-action-bar.vertical .action-item {
	border: thin solid transparent; /* prevents jumping behaviour on hover or focus */
}


/* High Contrast Theming */
.hc-black .context-view.monaco-menu-container {
	box-shadow: none;
}

.hc-black .monaco-menu .monaco-action-bar.vertical .action-item.focused {
	background: none;
}

/* Menubar styles */

.menubar {
	display: flex;
	flex-shrink: 1;
	box-sizing: border-box;
	height: 30px;
	overflow: hidden;
	flex-wrap: wrap;
}

.fullscreen .menubar:not(.compact) {
	margin: 0px;
	padding: 0px 5px;
}

.menubar > .menubar-menu-button {
	align-items: center;
	box-sizing: border-box;
	padding: 0px 8px;
	cursor: default;
	-webkit-app-region: no-drag;
	zoom: 1;
	white-space: nowrap;
	outline: 0;
}

.menubar.compact {
	flex-shrink: 0;
}

.menubar.compact > .menubar-menu-button {
	width: 100%;
	height: 100%;
	padding: 0px;
}

.menubar .menubar-menu-items-holder {
	position: absolute;
	left: 0px;
	opacity: 1;
	z-index: 2000;
}

.menubar .menubar-menu-items-holder.monaco-menu-container {
	outline: 0;
	border: none;
}

.menubar .menubar-menu-items-holder.monaco-menu-container :focus {
	outline: 0;
}

.menubar .toolbar-toggle-more {
	width: 20px;
	height: 100%;
}

.menubar.compact .toolbar-toggle-more {
	position: absolute;
	left: 0px;
	top: 0px;
	cursor: pointer;
	width: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.menubar .toolbar-toggle-more {
	padding: 0;
	vertical-align: sub;
}

.menubar.compact .toolbar-toggle-more::before {
	content: "\eb94" !important;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Arrows */
.monaco-scrollable-element > .scrollbar > .up-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTEgMTEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0ibTkuNDgwNDYsOC45NjE1bDEuMjYsLTEuMjZsLTUuMDQsLTUuMDRsLTUuNDYsNS4wNGwxLjI2LDEuMjZsNC4yLC0zLjc4bDMuNzgsMy43OHoiIGZpbGw9IiM0MjQyNDIiLz48L3N2Zz4=");
	cursor: pointer;
}
.monaco-scrollable-element > .scrollbar > .down-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMSAxMSI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoLTE4MCA1LjQ5MDQ1OTkxODk3NTgzLDUuODExNTAwMDcyNDc5MjQ4KSIgZmlsbD0iIzQyNDI0MiIgZD0ibTkuNDgwNDYsOC45NjE1bDEuMjYsLTEuMjZsLTUuMDQsLTUuMDRsLTUuNDYsNS4wNGwxLjI2LDEuMjZsNC4yLC0zLjc4bDMuNzgsMy43OHoiLz48L3N2Zz4=");
	cursor: pointer;
}
.monaco-scrollable-element > .scrollbar > .left-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMSAxMSI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoLTkwIDUuNDkwNDU5OTE4OTc1ODMxLDUuNDMxMzgyMTc5MjYwMjU0KSIgZmlsbD0iIzQyNDI0MiIgZD0ibTkuNDgwNDYsOC41ODEzOGwxLjI2LC0xLjI2bC01LjA0LC01LjA0bC01LjQ2LDUuMDRsMS4yNiwxLjI2bDQuMiwtMy43OGwzLjc4LDMuNzh6Ii8+PC9zdmc+");
	cursor: pointer;
}
.monaco-scrollable-element > .scrollbar > .right-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTEgMTEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoOTAgNS42MTcxNjUwODg2NTM1NjQ1LDUuNTU4MDg5NzMzMTIzNzgpICIgZmlsbD0iIzQyNDI0MiIgZD0ibTkuNjA3MTcsOC43MDgwOWwxLjI2LC0xLjI2bC01LjA0LC01LjA0bC01LjQ2LDUuMDRsMS4yNiwxLjI2bDQuMiwtMy43OGwzLjc4LDMuNzh6Ii8+PC9zdmc+");
	cursor: pointer;
}

.hc-black .monaco-scrollable-element > .scrollbar > .up-arrow,
.vs-dark .monaco-scrollable-element > .scrollbar > .up-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTEgMTEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0ibTkuNDgwNDYsOC45NjE1bDEuMjYsLTEuMjZsLTUuMDQsLTUuMDRsLTUuNDYsNS4wNGwxLjI2LDEuMjZsNC4yLC0zLjc4bDMuNzgsMy43OHoiIGZpbGw9IiNFOEU4RTgiLz48L3N2Zz4=");
}
.hc-black .monaco-scrollable-element > .scrollbar > .down-arrow,
.vs-dark .monaco-scrollable-element > .scrollbar > .down-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMSAxMSI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoLTE4MCA1LjQ5MDQ1OTkxODk3NTgzLDUuODExNTAwMDcyNDc5MjQ4KSIgZmlsbD0iI0U4RThFOCIgZD0ibTkuNDgwNDYsOC45NjE1bDEuMjYsLTEuMjZsLTUuMDQsLTUuMDRsLTUuNDYsNS4wNGwxLjI2LDEuMjZsNC4yLC0zLjc4bDMuNzgsMy43OHoiLz48L3N2Zz4=");
}
.hc-black .monaco-scrollable-element > .scrollbar > .left-arrow,
.vs-dark .monaco-scrollable-element > .scrollbar > .left-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMSAxMSI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoLTkwIDUuNDkwNDU5OTE4OTc1ODMxLDUuNDMxMzgyMTc5MjYwMjU0KSIgZmlsbD0iI0U4RThFOCIgZD0ibTkuNDgwNDYsOC41ODEzOGwxLjI2LC0xLjI2bC01LjA0LC01LjA0bC01LjQ2LDUuMDRsMS4yNiwxLjI2bDQuMiwtMy43OGwzLjc4LDMuNzh6Ii8+PC9zdmc+");
}
.hc-black .monaco-scrollable-element > .scrollbar > .right-arrow,
.vs-dark .monaco-scrollable-element > .scrollbar > .right-arrow {
	background: url("data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTEgMTEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggdHJhbnNmb3JtPSJyb3RhdGUoOTAgNS42MTcxNjUwODg2NTM1NjQ1LDUuNTU4MDg5NzMzMTIzNzgpICIgZmlsbD0iI0U4RThFOCIgZD0ibTkuNjA3MTcsOC43MDgwOWwxLjI2LC0xLjI2bC01LjA0LC01LjA0bC01LjQ2LDUuMDRsMS4yNiwxLjI2bDQuMiwtMy43OGwzLjc4LDMuNzh6Ii8+PC9zdmc+");
}

.monaco-scrollable-element > .visible {
	opacity: 1;

	/* Background rule added for IE9 - to allow clicks on dom node */
	background:rgba(0,0,0,0);

	transition: opacity 100ms linear;
}
.monaco-scrollable-element > .invisible {
	opacity: 0;
	pointer-events: none;
}
.monaco-scrollable-element > .invisible.fade {
	transition: opacity 800ms linear;
}

/* Scrollable Content Inset Shadow */
.monaco-scrollable-element > .shadow {
	position: absolute;
	display: none;
}
.monaco-scrollable-element > .shadow.top {
	display: block;
	top: 0;
	left: 3px;
	height: 3px;
	width: 100%;
	box-shadow: #DDD 0 6px 6px -6px inset;
}
.monaco-scrollable-element > .shadow.left {
	display: block;
	top: 3px;
	left: 0;
	height: 100%;
	width: 3px;
	box-shadow: #DDD 6px 0 6px -6px inset;
}
.monaco-scrollable-element > .shadow.top-left-corner {
	display: block;
	top: 0;
	left: 0;
	height: 3px;
	width: 3px;
}
.monaco-scrollable-element > .shadow.top.left {
	box-shadow: #DDD 6px 6px 6px -6px inset;
}

/* ---------- Default Style ---------- */

.vs .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(100, 100, 100, .4);
}
.vs-dark .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(121, 121, 121, .4);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider {
	background: rgba(111, 195, 223, .6);
}

.monaco-scrollable-element > .scrollbar > .slider:hover {
	background: rgba(100, 100, 100, .7);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider:hover {
	background: rgba(111, 195, 223, .8);
}

.monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(0, 0, 0, .6);
}
.vs-dark .monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(191, 191, 191, .4);
}
.hc-black .monaco-scrollable-element > .scrollbar > .slider.active {
	background: rgba(111, 195, 223, 1);
}

.vs-dark .monaco-scrollable-element .shadow.top {
	box-shadow: none;
}

.vs-dark .monaco-scrollable-element .shadow.left {
	box-shadow: #000 6px 0 6px -6px inset;
}

.vs-dark .monaco-scrollable-element .shadow.top.left {
	box-shadow: #000 6px 6px 6px -6px inset;
}

.hc-black .monaco-scrollable-element .shadow.top {
	box-shadow: none;
}

.hc-black .monaco-scrollable-element .shadow.left {
	box-shadow: none;
}

.hc-black .monaco-scrollable-element .shadow.top.left {
	box-shadow: none;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor.vs .dnd-target {
	border-right: 2px dotted black;
	color: white; /* opposite of black */
}
.monaco-editor.vs-dark .dnd-target {
	border-right: 2px dotted #AEAFAD;
	color: #51504f; /* opposite of #AEAFAD */
}
.monaco-editor.hc-black .dnd-target {
	border-right: 2px dotted #fff;
	color: #000; /* opposite of #fff */
}

.monaco-editor.mouse-default .view-lines,
.monaco-editor.vs-dark.mac.mouse-default .view-lines,
.monaco-editor.hc-black.mac.mouse-default .view-lines {
	cursor: default;
}
.monaco-editor.mouse-copy .view-lines,
.monaco-editor.vs-dark.mac.mouse-copy .view-lines,
.monaco-editor.hc-black.mac.mouse-copy .view-lines {
	cursor: copy;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-custom-checkbox {
	margin-left: 2px;
	float: left;
	cursor: pointer;
	overflow: hidden;
	opacity: 0.7;
	width: 20px;
	height: 20px;
	border: 1px solid transparent;
	padding: 1px;
	box-sizing:	border-box;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-custom-checkbox:hover,
.monaco-custom-checkbox.checked {
	opacity: 1;
}

.hc-black .monaco-custom-checkbox {
	background: none;
}

.hc-black .monaco-custom-checkbox:hover {
	background: none;
}

.monaco-custom-checkbox.monaco-simple-checkbox {
	height: 18px;
	width: 18px;
	border: 1px solid transparent;
	border-radius: 3px;
	margin-right: 9px;
	margin-left: 0px;
	padding: 0px;
	opacity: 1;
	background-size: 16px !important;
}

/* hide check when unchecked */
.monaco-custom-checkbox.monaco-simple-checkbox.unchecked:not(.checked)::before {
	visibility: hidden;;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Find widget */
.monaco-editor .find-widget {
	position: absolute;
	z-index: 10;
	height: 33px;
	overflow: hidden;
	line-height: 19px;
	transition: transform 200ms linear;
	padding: 0 4px;
	box-sizing: border-box;
	transform: translateY(calc(-100% - 10px)); /* shadow (10px) */
}

.monaco-editor .find-widget textarea {
	margin: 0px;
}

.monaco-editor .find-widget.hiddenEditor {
	display: none;
}

/* Find widget when replace is toggled on */
.monaco-editor .find-widget.replaceToggled > .replace-part {
	display: flex;
}

.monaco-editor .find-widget.visible  {
	transform: translateY(0);
}

.monaco-editor .find-widget .monaco-inputbox.synthetic-focus {
	outline: 1px solid -webkit-focus-ring-color;
	outline-offset: -1px;
}

.monaco-editor .find-widget .monaco-inputbox .input {
	background-color: transparent;
	min-height: 0;
}

.monaco-editor .find-widget .monaco-findInput .input {
	font-size: 13px;
}

.monaco-editor .find-widget > .find-part,
.monaco-editor .find-widget > .replace-part {
	margin: 4px 0 0 17px;
	font-size: 12px;
	display: flex;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox,
.monaco-editor .find-widget > .replace-part .monaco-inputbox {
	min-height: 25px;
}


.monaco-editor .find-widget > .replace-part .monaco-inputbox > .wrapper > .mirror {
	padding-right: 22px;
}

.monaco-editor .find-widget > .find-part .monaco-inputbox > .wrapper > .input,
.monaco-editor .find-widget > .find-part .monaco-inputbox > .wrapper > .mirror,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .wrapper > .input,
.monaco-editor .find-widget > .replace-part .monaco-inputbox > .wrapper > .mirror {
	padding-top: 2px;
	padding-bottom: 2px;
}

.monaco-editor .find-widget > .find-part .find-actions {
	height: 25px;
	display: flex;
	align-items: center;
}

.monaco-editor .find-widget > .replace-part .replace-actions {
	height: 25px;
	display: flex;
	align-items: center;
}

.monaco-editor .find-widget .monaco-findInput {
	vertical-align: middle;
	display: flex;
	flex:1;
}

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element {
	/* Make sure textarea inherits the width correctly */
	width: 100%;
}

.monaco-editor .find-widget .monaco-findInput .monaco-scrollable-element .scrollbar.vertical {
	/* Hide vertical scrollbar */
	opacity: 0;
}

.monaco-editor .find-widget .matchesCount {
	display: flex;
	flex: initial;
	margin: 0 0 0 3px;
	padding: 2px 0 0 2px;
	height: 25px;
	vertical-align: middle;
	box-sizing: border-box;
	text-align: center;
	line-height: 23px;
}

.monaco-editor .find-widget .button {
	width: 20px;
	height: 20px;
	display: flex;
	flex: initial;
	margin-left: 3px;
	background-position: center center;
	background-repeat: no-repeat;
	cursor: pointer;
	display: flex;
	align-items: center;
	justify-content: center;
}

.monaco-editor .find-widget .button:not(.disabled):hover {
	background-color: rgba(0, 0, 0, 0.1);
}

.monaco-editor .find-widget .button.left {
	margin-left: 0;
	margin-right: 3px;
}

.monaco-editor .find-widget .button.wide {
	width: auto;
	padding: 1px 6px;
	top: -1px;
}

.monaco-editor .find-widget .button.toggle {
	position: absolute;
	top: 0;
	left: 3px;
	width: 18px;
	height: 100%;
	box-sizing: border-box;
}

.monaco-editor .find-widget .button.toggle.disabled {
	display: none;
}

.monaco-editor .find-widget .disabled {
	opacity: 0.3;
	cursor: default;
}

.monaco-editor .find-widget > .replace-part {
	display: none;
}

.monaco-editor .find-widget > .replace-part > .monaco-findInput {
	position: relative;
	display: flex;
	vertical-align: middle;
	flex: auto;
	flex-grow: 0;
	flex-shrink: 0;
}

.monaco-editor .find-widget > .replace-part > .monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

/* REDUCED */
.monaco-editor .find-widget.reduced-find-widget .matchesCount {
	display:none;
}

/* NARROW (SMALLER THAN REDUCED) */
.monaco-editor .find-widget.narrow-find-widget {
	max-width: 257px !important;
}

/* COLLAPSED (SMALLER THAN NARROW) */
.monaco-editor .find-widget.collapsed-find-widget {
	max-width: 170px !important;
}

.monaco-editor .find-widget.collapsed-find-widget .button.previous,
.monaco-editor .find-widget.collapsed-find-widget .button.next,
.monaco-editor .find-widget.collapsed-find-widget .button.replace,
.monaco-editor .find-widget.collapsed-find-widget .button.replace-all,
.monaco-editor .find-widget.collapsed-find-widget > .find-part .monaco-findInput .controls {
	display:none;
}

.monaco-editor .findMatch {
	animation-duration: 0;
	animation-name: inherit !important;
}

.monaco-editor .find-widget .monaco-sash {
	width: 2px !important;
	margin-left: -4px;
}

.monaco-editor.hc-black .find-widget .button:not(.disabled):hover,
.monaco-editor.vs-dark .find-widget .button:not(.disabled):hover {
	background-color: rgba(255, 255, 255, 0.1);
}

.monaco-editor.hc-black .find-widget .button:before {
	position: relative;
	top: 1px;
	left: 2px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-sash {
	position: absolute;
	z-index: 35;
	touch-action: none;
}

.monaco-sash.disabled {
	pointer-events: none;
}

.monaco-sash.vertical {
	cursor: ew-resize;
	top: 0;
	width: 4px;
	height: 100%;
}

.monaco-sash.mac.vertical {
	cursor: col-resize;
}

.monaco-sash.vertical.minimum {
	cursor: e-resize;
}

.monaco-sash.vertical.maximum {
	cursor: w-resize;
}

.monaco-sash.horizontal {
	cursor: ns-resize;
	left: 0;
	width: 100%;
	height: 4px;
}

.monaco-sash.mac.horizontal {
	cursor: row-resize;
}

.monaco-sash.horizontal.minimum {
	cursor: s-resize;
}

.monaco-sash.horizontal.maximum {
	cursor: n-resize;
}

.monaco-sash:not(.disabled).orthogonal-start::before,
.monaco-sash:not(.disabled).orthogonal-end::after {
	content: ' ';
	height: 8px;
	width: 8px;
	z-index: 100;
	display: block;
	cursor: all-scroll;
	position: absolute;
}

.monaco-sash.orthogonal-start.vertical::before {
	left: -2px;
	top: -4px;
}

.monaco-sash.orthogonal-end.vertical::after {
	left: -2px;
	bottom: -4px;
}

.monaco-sash.orthogonal-start.horizontal::before {
	top: -2px;
	left: -4px;
}

.monaco-sash.orthogonal-end.horizontal::after {
	top: -2px;
	right: -4px;
}

.monaco-sash.disabled {
	cursor: default !important;
	pointer-events: none !important;
}

/** Touch **/

.monaco-sash.touch.vertical {
	width: 20px;
}

.monaco-sash.touch.horizontal {
	height: 20px;
}

/** Debug **/

.monaco-sash.debug {
	background: cyan;
}

.monaco-sash.debug.disabled {
	background: rgba(0, 255, 255, 0.2);
}

.monaco-sash.debug:not(.disabled).orthogonal-start::before,
.monaco-sash.debug:not(.disabled).orthogonal-end::after {
	background: red;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- Find input ---------- */

.monaco-findInput {
	position: relative;
}

.monaco-findInput .monaco-inputbox {
	font-size: 13px;
	width: 100%;
}

.monaco-findInput > .controls {
	position: absolute;
	top: 3px;
	right: 2px;
}

.vs .monaco-findInput.disabled {
	background-color: #E1E1E1;
}

/* Theming */
.vs-dark .monaco-findInput.disabled {
	background-color: #333;
}

/* Highlighting */
.monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-0 100ms linear 0s;
}
.monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-1 100ms linear 0s;
}
.hc-black .monaco-findInput.highlight-0 .controls,
.vs-dark  .monaco-findInput.highlight-0 .controls {
	animation: monaco-findInput-highlight-dark-0 100ms linear 0s;
}
.hc-black .monaco-findInput.highlight-1 .controls,
.vs-dark  .monaco-findInput.highlight-1 .controls {
	animation: monaco-findInput-highlight-dark-1 100ms linear 0s;
}

@keyframes monaco-findInput-highlight-0 {
	0% { background: rgba(253, 255, 0, 0.8); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-1 {
	0% { background: rgba(253, 255, 0, 0.8); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}

@keyframes monaco-findInput-highlight-dark-0 {
	0% { background: rgba(255, 255, 255, 0.44); }
	100% { background: transparent; }
}
@keyframes monaco-findInput-highlight-dark-1 {
	0% { background: rgba(255, 255, 255, 0.44); }
	/* Made intentionally different such that the CSS minifier does not collapse the two animations into a single one*/
	99% { background: transparent; }
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-inputbox {
	position: relative;
	display: block;
	padding: 0;
	box-sizing:	border-box;

	/* Customizable */
	font-size: inherit;
}

.monaco-inputbox.idle {
	border: 1px solid transparent;
}

.monaco-inputbox > .wrapper > .input,
.monaco-inputbox > .wrapper > .mirror {

	/* Customizable */
	padding: 4px;
}

.monaco-inputbox > .wrapper {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-inputbox > .wrapper > .input {
	display: inline-block;
	box-sizing:	border-box;
	width: 100%;
	height: 100%;
	line-height: inherit;
	border: none;
	font-family: inherit;
	font-size: inherit;
	resize: none;
	color: inherit;
}

.monaco-inputbox > .wrapper > input {
	text-overflow: ellipsis;
}

.monaco-inputbox > .wrapper > textarea.input {
	display: block;
	-ms-overflow-style: none; /* IE 10+: hide scrollbars */
	scrollbar-width: none; /* Firefox: hide scrollbars */
	outline: none;
}

.monaco-inputbox > .wrapper > textarea.input::-webkit-scrollbar {
	display: none; /* Chrome + Safari: hide scrollbar */
}

.monaco-inputbox > .wrapper > textarea.input.empty {
	white-space: nowrap;
}

.monaco-inputbox > .wrapper > .mirror {
	position: absolute;
	display: inline-block;
	width: 100%;
	top: 0;
	left: 0;
	box-sizing: border-box;
	white-space: pre-wrap;
	visibility: hidden;
	word-wrap: break-word;
}

/* Context view */

.monaco-inputbox-container {
	text-align: right;
}

.monaco-inputbox-container .monaco-inputbox-message {
	display: inline-block;
	overflow: hidden;
	text-align: left;
	width: 100%;
	box-sizing:	border-box;
	padding: 0.4em;
	font-size: 12px;
	line-height: 17px;
	min-height: 34px;
	margin-top: -1px;
	word-wrap: break-word;
}

/* Action bar support */
.monaco-inputbox .monaco-action-bar {
	position: absolute;
	right: 2px;
	top: 4px;
}

.monaco-inputbox .monaco-action-bar .action-item {
	margin-left: 2px;
}

.monaco-inputbox .monaco-action-bar .action-item .codicon {
	background-repeat: no-repeat;
	width: 16px;
	height: 16px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .codicon-chevron-right,
.monaco-editor .margin-view-overlays .codicon-chevron-down {
	cursor: pointer;
	opacity: 0;
	transition: opacity 0.5s;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 140%;
	margin-left: 2px;
}

.monaco-editor .margin-view-overlays:hover .codicon,
.monaco-editor .margin-view-overlays .codicon.codicon-chevron-right,
.monaco-editor .margin-view-overlays .codicon.alwaysShowFoldIcons {
	opacity: 1;
}

.monaco-editor .inline-folded:after {
	color: grey;
	margin: 0.1em 0.2em 0 0.2em;
	content: "⋯";
	display: inline;
	line-height: 1em;
	cursor: pointer;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* marker zone */

.monaco-editor .peekview-widget .head .peekview-title .severity-icon {
	display: inline-block;
	vertical-align: text-top;
	margin-right: 4px;
}

.monaco-editor .marker-widget {
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .marker-widget > .stale {
	opacity: 0.6;
	font-style: italic;
}

.monaco-editor .marker-widget .title {
	display: inline-block;
	padding-right: 5px;
}

.monaco-editor .marker-widget .descriptioncontainer {
	position: absolute;
	white-space: pre;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	padding: 8px 12px 0px 20px;
}

.monaco-editor .marker-widget .descriptioncontainer .message {
	display: flex;
	flex-direction: column;
}

.monaco-editor .marker-widget .descriptioncontainer .message .details {
	padding-left: 6px;
}

.monaco-editor .marker-widget .descriptioncontainer .message .source,
.monaco-editor .marker-widget .descriptioncontainer .message span.code {
	opacity: 0.6;
}

.monaco-editor .marker-widget .descriptioncontainer .message a.code-link {
	opacity: 0.6;
	color: inherit;
}
.monaco-editor .marker-widget .descriptioncontainer .message a.code-link:before {
	content: '(';
}
.monaco-editor .marker-widget .descriptioncontainer .message a.code-link:after {
	content: ')';
}
.monaco-editor .marker-widget .descriptioncontainer .message a.code-link > span {
	text-decoration: underline;
	/** Hack to force underline to show **/
	border-bottom: 1px solid transparent;
	text-underline-position: under;
}

.monaco-editor .marker-widget .descriptioncontainer .filename {
	cursor: pointer;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .peekview-widget .head {
	box-sizing:	border-box;
	display: flex;
}

.monaco-editor .peekview-widget .head .peekview-title {
	display: flex;
	align-items: center;
	font-size: 13px;
	margin-left: 20px;
	cursor: pointer;
}

.monaco-editor .peekview-widget .head .peekview-title .dirname:not(:empty) {
	font-size: 0.9em;
	margin-left: 0.5em;
}

.monaco-editor .peekview-widget .head .peekview-title .meta {
	white-space: nowrap;
}

.monaco-editor .peekview-widget .head .peekview-title .meta:not(:empty)::before {
	content: '-';
	padding: 0 0.3em;
}

.monaco-editor .peekview-widget .head .peekview-actions {
	flex: 1;
	text-align: right;
	padding-right: 2px;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar {
	display: inline-block;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar,
.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar > .actions-container {
	height: 100%;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar .action-item {
	margin-left: 4px;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar .action-label {
	width: 16px;
	height: 100%;
	margin: 0;
	line-height: inherit;
	background-repeat: no-repeat;
	background-position: center center;
}

.monaco-editor .peekview-widget .head .peekview-actions > .monaco-action-bar .action-label.codicon {
	margin: 0;
}

.monaco-editor .peekview-widget > .body {
	border-top: 1px solid;
	position: relative;
}

.monaco-editor .peekview-widget .head .peekview-title .codicon {
	margin-right: 4px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -------------------- IE10 remove auto clear button -------------------- */

::-ms-clear {
	display: none;
}

/* All widgets */
/* I am not a big fan of this rule */
.monaco-editor .editor-widget input {
	color: inherit;
}

/* -------------------- Editor -------------------- */

.monaco-editor {
	position: relative;
	overflow: visible;
	-webkit-text-size-adjust: 100%;
}

/* -------------------- Misc -------------------- */

.monaco-editor .overflow-guard {
	position: relative;
	overflow: hidden;
}

.monaco-editor .view-overlays {
	position: absolute;
	top: 0;
}

/*
.monaco-editor .auto-closed-character {
	opacity: 0.3;
}
*/
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .inputarea {
	min-width: 0;
	min-height: 0;
	margin: 0;
	padding: 0;
	position: absolute;
	outline: none !important;
	resize: none;
	border: none;
	overflow: hidden;
	color: transparent;
	background-color: transparent;
}
/*.monaco-editor .inputarea {
	position: fixed !important;
	width: 800px !important;
	height: 500px !important;
	top: initial !important;
	left: initial !important;
	bottom: 0 !important;
	right: 0 !important;
	color: black !important;
	background: white !important;
	line-height: 15px !important;
	font-size: 14px !important;
}*/
.monaco-editor .inputarea.ime-input {
	z-index: 10;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .margin-view-overlays .line-numbers {
	position: absolute;
	text-align: right;
	display: inline-block;
	vertical-align: middle;
	box-sizing: border-box;
	cursor: default;
	height: 100%;
}

.monaco-editor .relative-current-line-number {
	text-align: left;
	display: inline-block;
	width: 100%;
}

.monaco-editor .margin-view-overlays .line-numbers.lh-odd {
	margin-top: 1px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line {
	display: block;
	position: absolute;
	left: 0;
	top: 0;
	box-sizing: border-box;
}

.monaco-editor .margin-view-overlays .current-line.current-line-margin.current-line-margin-both {
	border-right: 0;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cdr = core decorations rendering (div)
*/
.monaco-editor .lines-content .cdr {
	position: absolute;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .glyph-margin {
	position: absolute;
	top: 0;
}

/*
	Keeping name short for faster parsing.
	cgmr = core glyph margin rendering (div)
*/
.monaco-editor .margin-view-overlays .cgmr {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cigr = core ident guides rendering (div)
*/
.monaco-editor .lines-content .cigr {
	position: absolute;
}
.monaco-editor .lines-content .cigra {
	position: absolute;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Uncomment to see lines flashing when they're painted */
/*.monaco-editor .view-lines > .view-line {
	background-color: none;
	animation-name: flash-background;
	animation-duration: 800ms;
}
@keyframes flash-background {
	0%   { background-color: lightgreen; }
	100% { background-color: none }
}*/

.monaco-editor.no-user-select .lines-content,
.monaco-editor.no-user-select .view-line,
.monaco-editor.no-user-select .view-lines {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-editor .view-lines {
	cursor: text;
	white-space: nowrap;
}

.monaco-editor.vs-dark.mac .view-lines,
.monaco-editor.hc-black.mac .view-lines {
	cursor: -webkit-image-set(url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAAL0lEQVQoz2NgCD3x//9/BhBYBWdhgFVAiVW4JBFKGIa4AqD0//9D3pt4I4tAdAMAHTQ/j5Zom30AAAAASUVORK5CYII=) 1x, url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAAz0lEQVRIx2NgYGBY/R8I/vx5eelX3n82IJ9FxGf6tksvf/8FiTMQAcAGQMDvSwu09abffY8QYSAScNk45G198eX//yev73/4///701eh//kZSARckrNBRvz//+8+6ZohwCzjGNjdgQxkAg7B9WADeBjIBqtJCbhRA0YNoIkBSNmaPEMoNmA0FkYNoFKhapJ6FGyAH3nauaSmPfwI0v/3OukVi0CIZ+F25KrtYcx/CTIy0e+rC7R1Z4KMICVTQQ14feVXIbR695u14+Ir4gwAAD49E54wc1kWAAAAAElFTkSuQmCC) 2x) 5 8, text;
}

.monaco-editor .view-line {
	position: absolute;
	width: 100%;
}

/* TODO@tokenization bootstrap fix */
/*.monaco-editor .view-line > span > span {
	float: none;
	min-height: inherit;
	margin-left: inherit;
}*/
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .lines-decorations {
	position: absolute;
	top: 0;
	background: white;
}

/*
	Keeping name short for faster parsing.
	cldr = core lines decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cldr {
	position: absolute;
	height: 100%;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cmdr = core margin decorations rendering (div)
*/
.monaco-editor .margin-view-overlays .cmdr {
	position: absolute;
	left: 0;
	width: 100%;
	height: 100%;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* START cover the case that slider is visible on mouseover */
.monaco-editor .minimap.slider-mouseover .minimap-slider {
	opacity: 0;
	transition: opacity 100ms linear;
}
.monaco-editor .minimap.slider-mouseover:hover .minimap-slider {
	opacity: 1;
}
.monaco-editor .minimap.slider-mouseover .minimap-slider.active {
	opacity: 1;
}
/* END cover the case that slider is visible on mouseover */

.monaco-editor .minimap-shadow-hidden {
	position: absolute;
	width: 0;
}
.monaco-editor .minimap-shadow-visible {
	position: absolute;
	left: -6px;
	width: 6px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .overlayWidgets {
	position: absolute;
	top: 0;
	left:0;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .view-ruler {
	position: absolute;
	top: 0;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .scroll-decoration {
	position: absolute;
	top: 0;
	left: 0;
	height: 6px;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/*
	Keeping name short for faster parsing.
	cslr = core selections layer rendering (div)
*/
.monaco-editor .lines-content .cslr {
	position: absolute;
}

.monaco-editor			.top-left-radius		{ border-top-left-radius: 3px; }
.monaco-editor			.bottom-left-radius		{ border-bottom-left-radius: 3px; }
.monaco-editor			.top-right-radius		{ border-top-right-radius: 3px; }
.monaco-editor			.bottom-right-radius	{ border-bottom-right-radius: 3px; }

.monaco-editor.hc-black .top-left-radius		{ border-top-left-radius: 0; }
.monaco-editor.hc-black .bottom-left-radius		{ border-bottom-left-radius: 0; }
.monaco-editor.hc-black .top-right-radius		{ border-top-right-radius: 0; }
.monaco-editor.hc-black .bottom-right-radius	{ border-bottom-right-radius: 0; }
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .cursors-layer {
	position: absolute;
	top: 0;
}

.monaco-editor .cursors-layer > .cursor {
	position: absolute;
	cursor: text;
	overflow: hidden;
}

/* -- smooth-caret-animation -- */
.monaco-editor .cursors-layer.cursor-smooth-caret-animation > .cursor {
	transition: all 80ms;
}

/* -- block-outline-style -- */
.monaco-editor .cursors-layer.cursor-block-outline-style > .cursor {
	box-sizing: border-box;
	background: transparent !important;
	border-style: solid;
	border-width: 1px;
}

/* -- underline-style -- */
.monaco-editor .cursors-layer.cursor-underline-style > .cursor {
	border-bottom-width: 2px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

/* -- underline-thin-style -- */
.monaco-editor .cursors-layer.cursor-underline-thin-style > .cursor {
	border-bottom-width: 1px;
	border-bottom-style: solid;
	background: transparent !important;
	box-sizing: border-box;
}

@keyframes monaco-cursor-smooth {
	0%,
	20% {
		opacity: 1;
	}
	60%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-phase {
	0%,
	20% {
		opacity: 1;
	}
	90%,
	100% {
		opacity: 0;
	}
}

@keyframes monaco-cursor-expand {
	0%,
	20% {
		transform: scaleY(1);
	}
	80%,
	100% {
		transform: scaleY(0);
	}
}

.cursor-smooth {
	animation: monaco-cursor-smooth 0.5s ease-in-out 0s 20 alternate;
}

.cursor-phase {
	animation: monaco-cursor-phase 0.5s ease-in-out 0s 20 alternate;
}

.cursor-expand > .cursor {
	animation: monaco-cursor-expand 0.5s ease-in-out 0s 20 alternate;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .zone-widget {
	position: absolute;
	z-index: 10;
}


.monaco-editor .zone-widget .zone-widget-container {
	border-top-style: solid;
	border-bottom-style: solid;
	border-top-width: 0;
	border-bottom-width: 0;
	position: relative;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-quick-open-widget {
	font-size: 13px;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* ---------- Icon label ---------- */

.monaco-icon-label {
	display: flex; /* required for icons support :before rule */
	overflow: hidden;
	text-overflow: ellipsis;
}

.monaco-icon-label::before {

	/* svg icons rendered as background image */
	background-size: 16px;
	background-position: left center;
	background-repeat: no-repeat;
	padding-right: 6px;
	width: 16px;
	height: 22px;
	line-height: inherit !important;
	display: inline-block;

	/* fonts icons */
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	vertical-align: top;

	flex-shrink: 0; /* fix for https://github.com/Microsoft/vscode/issues/13787 */
}

.monaco-icon-label > .monaco-icon-label-container {
	min-width: 0;
	overflow: hidden;
	text-overflow: ellipsis;
	flex: 1;
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-container > .label-name {
	color: inherit;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-name-container > .label-name > .label-separator {
	margin: 0 2px;
	opacity: 0.5;
}

.monaco-icon-label > .monaco-icon-label-container > .monaco-icon-description-container > .label-description {
	opacity: .7;
	margin-left: 0.5em;
	font-size: 0.9em;
	white-space: pre; /* enable to show labels that include multiple whitespaces */
}

.monaco-icon-label.italic > .monaco-icon-label-container > .monaco-icon-name-container > .label-name,
.monaco-icon-label.italic > .monaco-icon-description-container > .label-description {
	font-style: italic;
}

.monaco-icon-label::after {
	opacity: 0.75;
	font-size: 90%;
	font-weight: 600;
	padding: 0 16px 0 5px;
	text-align: center;
}

/* make sure selection color wins when a label is being selected */
.monaco-tree.focused .selected .monaco-icon-label, /* tree */
.monaco-tree.focused .selected .monaco-icon-label::after,
.monaco-list:focus .selected .monaco-icon-label, /* list */
.monaco-list:focus .selected .monaco-icon-label::after
{
	color: inherit !important;
}

.monaco-tree-row.focused.selected .label-description,
.monaco-tree-row.selected .label-description,
.monaco-list-row.focused.selected .label-description,
.monaco-list-row.selected .label-description {
	opacity: .8;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-keybinding {
	display: flex;
	align-items: center;
	line-height: 10px;
}

.monaco-keybinding > .monaco-keybinding-key {
	display: inline-block;
	border: solid 1px rgba(204, 204, 204, 0.4);
	border-bottom-color: rgba(187, 187, 187, 0.4);
	border-radius: 3px;
	box-shadow: inset 0 -1px 0 rgba(187, 187, 187, 0.4);
	background-color: rgba(221, 221, 221, 0.4);
	vertical-align: middle;
	color: #555;
	font-size: 11px;
	padding: 3px 5px;
	margin: 0 2px;
}

.monaco-keybinding > .monaco-keybinding-key:first-child {
	margin-left: 0;
}

.monaco-keybinding > .monaco-keybinding-key:last-child {
	margin-right: 0;
}

.hc-black .monaco-keybinding > .monaco-keybinding-key,
.vs-dark .monaco-keybinding > .monaco-keybinding-key {
	background-color: rgba(128, 128, 128, 0.17);
	color: #ccc;
	border: solid 1px rgba(51, 51, 51, 0.6);
	border-bottom-color: rgba(68, 68, 68, 0.6);
	box-shadow: inset 0 -1px 0 rgba(68, 68, 68, 0.6);
}

.monaco-keybinding > .monaco-keybinding-key-separator {
	display: inline-block;
}

.monaco-keybinding > .monaco-keybinding-key-chord-separator {
	width: 6px;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-quick-open-widget .monaco-tree .monaco-tree-row .monaco-highlighted-label .highlight,
.monaco-quick-open-widget .monaco-list .monaco-list-row .monaco-highlighted-label .highlight {
	color: #0066BF;
}

.vs-dark .monaco-quick-open-widget .monaco-tree .monaco-tree-row .monaco-highlighted-label .highlight,
.vs-dark .monaco-quick-open-widget .monaco-list .monaco-list-row .monaco-highlighted-label .highlight {
	color: #0097fb;
}

.hc-black .monaco-quick-open-widget .monaco-tree .monaco-tree-row .monaco-highlighted-label .highlight,
.hc-black .monaco-quick-open-widget .monaco-list .monaco-list-row .monaco-highlighted-label .highlight {
	color: #F38518;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-quick-open-widget {
	position: absolute;
	width: 600px;
	z-index: 2000;
	padding-bottom: 6px;
	left: 50%;
	margin-left: -300px;
}

.monaco-quick-open-widget .monaco-progress-container {
	position: absolute;
	left: 0;
	top: 38px;
	z-index: 1;
	height: 2px;
}

.monaco-quick-open-widget .monaco-progress-container .progress-bit {
	height: 2px;
}

.monaco-quick-open-widget .quick-open-input {
	width: 588px;
	border: none;
	margin: 6px;
}

.monaco-quick-open-widget .quick-open-input .monaco-inputbox {
	width: 100%;
	height: 25px;
}

.monaco-quick-open-widget .quick-open-result-count {
	position: absolute;
	left: -10000px;
}

.monaco-quick-open-widget .quick-open-tree {
	line-height: 22px;
}

.monaco-quick-open-widget .quick-open-tree .monaco-tree-row  > .content > .sub-content {
	overflow: hidden;
}

.monaco-quick-open-widget.content-changing .quick-open-tree .monaco-scrollable-element .slider {
	display: none; /* scrollbar slider causes some hectic updates when input changes quickly, so hide it while quick open changes */
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry {
	overflow: hidden;
	text-overflow: ellipsis;
	display: flex;
	flex-direction: column;
	height: 100%;
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry > .quick-open-row {
	display: flex;
	align-items: center;
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry .quick-open-entry-icon {
	overflow: hidden;
	width: 16px;
	height: 16px;
	margin-right: 4px;
	display: flex;
	align-items: center;
	vertical-align: middle;
	flex-shrink: 0;
}

.monaco-quick-open-widget .quick-open-tree .monaco-icon-label,
.monaco-quick-open-widget .quick-open-tree .monaco-icon-label .monaco-icon-label-container > .monaco-icon-name-container {
	flex: 1; /* make sure the icon label grows within the row */
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry .monaco-highlighted-label span {
	opacity: 1;
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry .monaco-highlighted-label .codicon {
	vertical-align: sub; /* vertically align codicon */
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry-meta {
	opacity: 0.7;
	line-height: normal;
}

.monaco-quick-open-widget .quick-open-tree .content.has-group-label .quick-open-entry-keybinding {
	margin-right: 8px;
}

.monaco-quick-open-widget .quick-open-tree .quick-open-entry-keybinding .monaco-keybinding-key {
	vertical-align: text-bottom;
}

.monaco-quick-open-widget .quick-open-tree .results-group {
	margin-right: 18px;
}

.monaco-quick-open-widget .quick-open-tree .monaco-tree-row.focused > .content.has-actions > .results-group,
.monaco-quick-open-widget .quick-open-tree .monaco-tree-row:hover:not(.highlighted) > .content.has-actions > .results-group,
.monaco-quick-open-widget .quick-open-tree .focused .monaco-tree-row.focused > .content.has-actions > .results-group {
	margin-right: 0px;
}

.monaco-quick-open-widget .quick-open-tree .results-group-separator {
	border-top-width: 1px;
	border-top-style: solid;
	box-sizing: border-box;
	margin-left: -11px;
	padding-left: 11px;
}

/* Actions in Quick Open Items */

.monaco-tree .monaco-tree-row > .content.actions {
	position: relative;
	display: flex;
}

.monaco-tree .monaco-tree-row > .content.actions > .sub-content {
	flex: 1;
}

.monaco-tree .monaco-tree-row > .content.actions .action-item {
	margin: 0;
}

.monaco-tree .monaco-tree-row > .content.actions > .primary-action-bar {
	line-height: 22px;
}

.monaco-tree .monaco-tree-row > .content.actions > .primary-action-bar {
	display: none;
	padding: 0 0.8em 0 0.4em;
}

.monaco-tree .monaco-tree-row.focused > .content.has-actions > .primary-action-bar {
	width: 0; /* in order to support a11y with keyboard, we use width: 0 to hide the actions, which still allows to "Tab" into the actions */
	display: block;
}

.monaco-tree .monaco-tree-row:hover:not(.highlighted) > .content.has-actions > .primary-action-bar,
.monaco-tree.focused .monaco-tree-row.focused > .content.has-actions > .primary-action-bar,
.monaco-tree .monaco-tree-row > .content.has-actions.more > .primary-action-bar {
	width: inherit;
	display: block;
}

.monaco-tree .monaco-tree-row > .content.actions > .primary-action-bar .action-label {
	margin-right: 0.4em;
	margin-top: 4px;
	background-repeat: no-repeat;
	width: 16px;
	height: 16px;
}

.monaco-quick-open-widget .quick-open-tree .monaco-highlighted-label .highlight {
	font-weight: bold;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-tree {
	height: 100%;
	width: 100%;
	white-space: nowrap;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
	position: relative;
}

.monaco-tree > .monaco-scrollable-element {
	height: 100%;
}

.monaco-tree > .monaco-scrollable-element > .monaco-tree-wrapper {
	height: 100%;
	width: 100%;
	position: relative;
}

.monaco-tree .monaco-tree-rows {
	position: absolute;
	width: 100%;
	height: 100%;
}

.monaco-tree .monaco-tree-rows > .monaco-tree-row {
	box-sizing:	border-box;
	cursor: pointer;
	overflow: hidden;
	width: 100%;
	touch-action: none;
}

.monaco-tree .monaco-tree-rows > .monaco-tree-row > .content {
	position: relative;
	height: 100%;
}

.monaco-tree-drag-image {
	display: inline-block;
	padding: 1px 7px;
	border-radius: 10px;
	font-size: 12px;
	position: absolute;
}

/* for OS X ballistic scrolling */
.monaco-tree .monaco-tree-rows > .monaco-tree-row.scrolling {
	display: none;
}

/* Highlighted */

.monaco-tree.highlighted .monaco-tree-rows > .monaco-tree-row:not(.highlighted) {
	opacity: 0.3;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-progress-container {
	width: 100%;
	height: 5px;
	overflow: hidden; /* keep progress bit in bounds */
}

.monaco-progress-container .progress-bit {
	width: 2%;
	height: 5px;
	position: absolute;
	left: 0;
	display: none;
}

.monaco-progress-container.active .progress-bit {
	display: inherit;
}

.monaco-progress-container.discrete .progress-bit {
	left: 0;
	transition: width 100ms linear;
}

.monaco-progress-container.discrete.done .progress-bit {
	width: 100%;
}

.monaco-progress-container.infinite .progress-bit {
	animation-name: progress;
	animation-duration: 4s;
	animation-iteration-count: infinite;
	animation-timing-function: linear;
	transform: translate3d(0px, 0px, 0px);
}

/**
 * The progress bit has a width: 2% (1/50) of the parent container. The animation moves it from 0% to 100% of
 * that container. Since translateX is relative to the progress bit size, we have to multiple it with
 * its relative size to the parent container:
 *  50%: 50 * 50 = 2500%
 * 100%: 50 * 100 - 50 (do not overflow): 4950%
 */
@keyframes progress { from { transform: translateX(0%) scaleX(1) } 50% { transform: translateX(2500%) scaleX(3) } to { transform: translateX(4950%) scaleX(1) } }
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* -- zone widget */
.monaco-editor .zone-widget .zone-widget-container.reference-zone-widget {
	border-top-width: 1px;
	border-bottom-width: 1px;
}

.monaco-editor .reference-zone-widget .inline {
	display: inline-block;
	vertical-align: top;
}

.monaco-editor .reference-zone-widget .messages {
	height: 100%;
	width: 100%;
	text-align: center;
	padding: 3em 0;
}

.monaco-editor .reference-zone-widget .ref-tree {
	line-height: 23px;
}

.monaco-editor .reference-zone-widget .ref-tree .reference {
	text-overflow: ellipsis;
	overflow: hidden;
}

.monaco-editor .reference-zone-widget .ref-tree .reference-file {
	display: inline-flex;
	width: 100%;
	height: 100%;
}

.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .selected .reference-file {
	color: inherit !important;
}

.monaco-editor .reference-zone-widget .ref-tree .reference-file .count {
	margin-right: 12px;
	margin-left: auto;
}

/* High Contrast Theming */

.monaco-editor.hc-black .reference-zone-widget .ref-tree .reference-file {
	font-weight: bold;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-count-badge {
	padding: 3px 5px;
	border-radius: 11px;
	font-size: 11px;
	min-width: 18px;
	min-height: 18px;
	line-height: 11px;
	font-weight: normal;
	text-align: center;
	display: inline-block;
	box-sizing: border-box;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-list {
	position: relative;
	height: 100%;
	width: 100%;
	white-space: nowrap;
}

.monaco-list.mouse-support {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-list > .monaco-scrollable-element {
	height: 100%;
}

.monaco-list-rows {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-list.horizontal-scrolling .monaco-list-rows {
	width: auto;
	min-width: 100%;
}

.monaco-list-row {
	position: absolute;
	box-sizing:	border-box;
	overflow: hidden;
	width: 100%;
}

.monaco-list.mouse-support .monaco-list-row {
	cursor: pointer;
	touch-action: none;
}

/* for OS X ballistic scrolling */
.monaco-list-row.scrolling {
	display: none !important;
}

/* Focus */
.monaco-list.element-focused, .monaco-list.selection-single, .monaco-list.selection-multiple {
	outline: 0 !important;
}

.monaco-list:focus .monaco-list-row.selected .codicon {
	color: inherit;
}

/* Dnd */
.monaco-drag-image {
	display: inline-block;
	padding: 1px 7px;
	border-radius: 10px;
	font-size: 12px;
	position: absolute;
}

/* Type filter */

.monaco-list-type-filter {
	display: flex;
	align-items: center;
	position: absolute;
	border-radius: 2px;
	padding: 0px 3px;
	max-width: calc(100% - 10px);
	text-overflow: ellipsis;
	overflow: hidden;
	text-align: right;
	box-sizing: border-box;
	cursor: all-scroll;
	font-size: 13px;
	line-height: 18px;
	height: 20px;
	z-index: 1;
	top: 4px;
}

.monaco-list-type-filter.dragging {
	transition: top 0.2s, left 0.2s;
}

.monaco-list-type-filter.ne {
	right: 4px;
}

.monaco-list-type-filter.nw {
	left: 4px;
}

.monaco-list-type-filter > .controls {
	display: flex;
	align-items: center;
	box-sizing: border-box;
	transition: width 0.2s;
	width: 0;
}

.monaco-list-type-filter.dragging > .controls,
.monaco-list-type-filter:hover > .controls {
	width: 36px;
}

.monaco-list-type-filter > .controls > * {
	border: none;
	box-sizing: border-box;
	-webkit-appearance: none;
	-moz-appearance: none;
	background: none;
	width: 16px;
	height: 16px;
	flex-shrink: 0;
	margin: 0;
	padding: 0;
	display: flex;
	align-items: center;
	justify-content: center;
	cursor: pointer;
}

.monaco-list-type-filter > .controls > .filter:checked::before {
	content: "\eb83" !important; /* codicon-list-filter */
}

.monaco-list-type-filter > .controls > .filter {
	margin-left: 4px;
}

.monaco-list-type-filter-message {
	position: absolute;
	box-sizing: border-box;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	padding: 40px 1em 1em 1em;
	text-align: center;
	white-space: normal;
	opacity: 0.7;
	pointer-events: none;
}

.monaco-list-type-filter-message:empty {
	display: none;
}

/* Electron */

.monaco-list-type-filter {
	cursor: grab;
}

.monaco-list-type-filter.dragging {
	cursor: grabbing;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-tl-row {
	display: flex;
	height: 100%;
	align-items: center;
	position: relative;
}

.monaco-tl-indent {
	height: 100%;
	position: absolute;
	top: 0;
	left: 16px;
	pointer-events: none;
}

.hide-arrows .monaco-tl-indent {
	left: 12px;
}

.monaco-tl-indent > .indent-guide {
	display: inline-block;
	box-sizing: border-box;
	height: 100%;
	border-left: 1px solid transparent;
}

.monaco-tl-indent > .indent-guide {
	transition: border-color 0.1s linear;
}

.monaco-tl-twistie,
.monaco-tl-contents {
	height: 100%;
}

.monaco-tl-twistie {
	font-size: 10px;
	text-align: right;
	padding-right: 6px;
	flex-shrink: 0;
	width: 16px;
	display: flex !important;
	align-items: center;
	justify-content: center;
	color: inherit !important;
	transform: translateX(3px);
}

.monaco-tl-contents {
	flex: 1;
	overflow: hidden;
}

.monaco-tl-twistie.collapsed::before {
	transform: rotate(-90deg);
}

.monaco-tl-twistie.codicon-loading::before {
	animation: codicon-spin 1.25s linear infinite;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-split-view2 {
	position: relative;
	width: 100%;
	height: 100%;
}

.monaco-split-view2 > .sash-container {
	position: absolute;
	width: 100%;
	height: 100%;
	pointer-events: none;
}

.monaco-split-view2 > .sash-container > .monaco-sash {
	pointer-events: initial;
}

.monaco-split-view2 > .split-view-container {
	width: 100%;
	height: 100%;
	white-space: nowrap;
	position: relative;
}

.monaco-split-view2 > .split-view-container > .split-view-view {
	white-space: initial;
	position: absolute;
}

.monaco-split-view2 > .split-view-container > .split-view-view:not(.visible) {
	display: none;
}

.monaco-split-view2.vertical > .split-view-container > .split-view-view {
	width: 100%;
}

.monaco-split-view2.horizontal > .split-view-container > .split-view-view {
	height: 100%;
}

.monaco-split-view2.separator-border > .split-view-container > .split-view-view:not(:first-child)::before {
	content: ' ';
	position: absolute;
	top: 0;
	left: 0;
	z-index: 5;
	pointer-events: none;
	background-color: var(--separator-border);
}

.monaco-split-view2.separator-border.horizontal > .split-view-container > .split-view-view:not(:first-child)::before {
	height: 100%;
	width: 1px;
}

.monaco-split-view2.separator-border.vertical > .split-view-container > .split-view-view:not(:first-child)::before {
	height: 1px;
	width: 100%;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .goto-definition-link {
	text-decoration: underline;
	cursor: pointer;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor-hover {
	cursor: default;
	position: absolute;
	overflow: hidden;
	z-index: 50;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	box-sizing: initial;
	animation: fadein 100ms linear;
	line-height: 1.5em;
}

.monaco-editor-hover.hidden {
	display: none;
}

.monaco-editor-hover .hover-contents {
	padding: 4px 8px;
}

.monaco-editor-hover .markdown-hover > .hover-contents:not(.code-hover-contents) {
	max-width: 500px;
	word-wrap: break-word;
}

.monaco-editor-hover .markdown-hover > .hover-contents:not(.code-hover-contents) hr {
	min-width: 100vw;
}

.monaco-editor-hover p,
.monaco-editor-hover ul {
	margin: 8px 0;
}

.monaco-editor-hover code {
	font-family: var(--monaco-monospace-font);
}

.monaco-editor-hover hr {
	margin-top: 4px;
	margin-bottom: -6px;
	margin-left: -10px;
	margin-right: -10px;
	height: 1px;
}

.monaco-editor-hover p:first-child,
.monaco-editor-hover ul:first-child {
	margin-top: 0;
}

.monaco-editor-hover p:last-child,
.monaco-editor-hover ul:last-child {
	margin-bottom: 0;
}

/* MarkupContent Layout */
.monaco-editor-hover ul {
	padding-left: 20px;
}
.monaco-editor-hover ol {
	padding-left: 20px;
}

.monaco-editor-hover li > p {
	margin-bottom: 0;
}

.monaco-editor-hover li > ul {
	margin-top: 0;
}

.monaco-editor-hover code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-editor-hover .monaco-tokenized-source {
	white-space: pre-wrap;
	word-break: break-all;
}

.monaco-editor-hover .hover-row.status-bar {
	font-size: 12px;
	line-height: 22px;
}

.monaco-editor-hover .hover-row.status-bar .actions {
	display: flex;
	padding: 0px 8px;
}

.monaco-editor-hover .hover-row.status-bar .actions .action-container {
	margin-right: 16px;
	cursor: pointer;
}

.monaco-editor-hover .hover-row.status-bar .actions .action-container .action .icon {
	padding-right: 4px;
}

.monaco-editor-hover .markdown-hover .hover-contents .codicon {
	color: inherit;
	font-size: inherit;
	vertical-align: middle;
}

.monaco-editor-hover .hover-contents a.code-link:before {
	content: '(';
}
.monaco-editor-hover .hover-contents a.code-link:after {
	content: ')';
}

.monaco-editor-hover .hover-contents a.code-link {
	color: inherit;
}
.monaco-editor-hover .hover-contents a.code-link > span {
	text-decoration: underline;
	/** Hack to force underline to show **/
	border-bottom: 1px solid transparent;
	text-underline-position: under;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.colorpicker-widget {
	height: 190px;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-editor .colorpicker-hover:focus {
	outline: none;
}


/* Header */

.colorpicker-header {
	display: flex;
	height: 24px;
	position: relative;
	background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTZEaa/1AAAAHUlEQVQYV2PYvXu3JAi7uLiAMaYAjAGTQBPYLQkAa/0Zef3qRswAAAAASUVORK5CYII=");
	background-size: 9px 9px;
	image-rendering: pixelated;
}

.colorpicker-header .picked-color {
	width: 216px;
	text-align: center;
	line-height: 24px;
	cursor: pointer;
	color: white;
	flex: 1;
	text-align: center;
}

.colorpicker-header .picked-color.light {
	color: black;
}

.colorpicker-header .original-color {
	width: 74px;
	z-index: inherit;
	cursor: pointer;
}


/* Body */

.colorpicker-body {
	display: flex;
	padding: 8px;
	position: relative;
}

.colorpicker-body .saturation-wrap {
	overflow: hidden;
	height: 150px;
	position: relative;
	min-width: 220px;
	flex: 1;
}

.colorpicker-body .saturation-box {
	height: 150px;
	position: absolute;
}

.colorpicker-body .saturation-selection {
	width: 9px;
	height: 9px;
	margin: -5px 0 0 -5px;
	border: 1px solid rgb(255, 255, 255);
	border-radius: 100%;
	box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.8);
	position: absolute;
}

.colorpicker-body .strip {
	width: 25px;
	height: 150px;
}

.colorpicker-body .hue-strip {
	position: relative;
	margin-left: 8px;
	cursor: grab;
	background: linear-gradient(to bottom, #ff0000 0%, #ffff00 17%, #00ff00 33%, #00ffff 50%, #0000ff 67%, #ff00ff 83%, #ff0000 100%);
}

.colorpicker-body .opacity-strip {
	position: relative;
	margin-left: 8px;
	cursor: grab;
	background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAZdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuMTZEaa/1AAAAHUlEQVQYV2PYvXu3JAi7uLiAMaYAjAGTQBPYLQkAa/0Zef3qRswAAAAASUVORK5CYII=");
	background-size: 9px 9px;
	image-rendering: pixelated;
}

.colorpicker-body .strip.grabbing {
	cursor: grabbing;
}

.colorpicker-body .slider {
	position: absolute;
	top: 0;
	left: -2px;
	width: calc(100% + 4px);
	height: 4px;
	box-sizing: border-box;
	border: 1px solid rgba(255, 255, 255, 0.71);
	box-shadow: 0px 0px 1px rgba(0, 0, 0, 0.85);
}

.colorpicker-body .strip .overlay {
	height: 150px;
	pointer-events: none;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .iPadShowKeyboard {
	width: 58px;
	min-width: 0;
	height: 36px;
	min-height: 0;
	margin: 0;
	padding: 0;
	position: absolute;
	resize: none;
	overflow: hidden;
	background: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIHZpZXdCb3g9IjAgMCA1MyAzNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMCkiPg0KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00OC4wMzY0IDQuMDEwNDJINC4wMDc3OUw0LjAwNzc5IDMyLjAyODZINDguMDM2NFY0LjAxMDQyWk00LjAwNzc5IDAuMDA3ODEyNUMxLjc5NzIxIDAuMDA3ODEyNSAwLjAwNTE4Nzk5IDEuNzk5ODQgMC4wMDUxODc5OSA0LjAxMDQyVjMyLjAyODZDMC4wMDUxODc5OSAzNC4yMzkyIDEuNzk3MjEgMzYuMDMxMiA0LjAwNzc5IDM2LjAzMTJINDguMDM2NEM1MC4yNDcgMzYuMDMxMiA1Mi4wMzkgMzQuMjM5MiA1Mi4wMzkgMzIuMDI4NlY0LjAxMDQyQzUyLjAzOSAxLjc5OTg0IDUwLjI0NyAwLjAwNzgxMjUgNDguMDM2NCAwLjAwNzgxMjVINC4wMDc3OVpNOC4wMTA0MiA4LjAxMzAySDEyLjAxM1YxMi4wMTU2SDguMDEwNDJWOC4wMTMwMlpNMjAuMDE4MiA4LjAxMzAySDE2LjAxNTZWMTIuMDE1NkgyMC4wMTgyVjguMDEzMDJaTTI0LjAyMDggOC4wMTMwMkgyOC4wMjM0VjEyLjAxNTZIMjQuMDIwOFY4LjAxMzAyWk0zNi4wMjg2IDguMDEzMDJIMzIuMDI2VjEyLjAxNTZIMzYuMDI4NlY4LjAxMzAyWk00MC4wMzEyIDguMDEzMDJINDQuMDMzOVYxMi4wMTU2SDQwLjAzMTJWOC4wMTMwMlpNMTYuMDE1NiAxNi4wMTgySDguMDEwNDJWMjAuMDIwOEgxNi4wMTU2VjE2LjAxODJaTTIwLjAxODIgMTYuMDE4MkgyNC4wMjA4VjIwLjAyMDhIMjAuMDE4MlYxNi4wMTgyWk0zMi4wMjYgMTYuMDE4MkgyOC4wMjM0VjIwLjAyMDhIMzIuMDI2VjE2LjAxODJaTTQ0LjAzMzkgMTYuMDE4MlYyMC4wMjA4SDM2LjAyODZWMTYuMDE4Mkg0NC4wMzM5Wk0xMi4wMTMgMjQuMDIzNEg4LjAxMDQyVjI4LjAyNkgxMi4wMTNWMjQuMDIzNFpNMTYuMDE1NiAyNC4wMjM0SDM2LjAyODZWMjguMDI2SDE2LjAxNTZWMjQuMDIzNFpNNDQuMDMzOSAyNC4wMjM0SDQwLjAzMTJWMjguMDI2SDQ0LjAzMzlWMjQuMDIzNFoiIGZpbGw9IiM0MjQyNDIiLz4NCjwvZz4NCjxkZWZzPg0KPGNsaXBQYXRoIGlkPSJjbGlwMCI+DQo8cmVjdCB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIGZpbGw9IndoaXRlIi8+DQo8L2NsaXBQYXRoPg0KPC9kZWZzPg0KPC9zdmc+DQo=") center center no-repeat;
	border: 4px solid #F6F6F6;
	border-radius: 4px;
}

.monaco-editor.vs-dark .iPadShowKeyboard {
	background: url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIHZpZXdCb3g9IjAgMCA1MyAzNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxnIGNsaXAtcGF0aD0idXJsKCNjbGlwMCkiPg0KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00OC4wMzY0IDQuMDEwNDJINC4wMDc3OUw0LjAwNzc5IDMyLjAyODZINDguMDM2NFY0LjAxMDQyWk00LjAwNzc5IDAuMDA3ODEyNUMxLjc5NzIxIDAuMDA3ODEyNSAwLjAwNTE4Nzk5IDEuNzk5ODQgMC4wMDUxODc5OSA0LjAxMDQyVjMyLjAyODZDMC4wMDUxODc5OSAzNC4yMzkyIDEuNzk3MjEgMzYuMDMxMiA0LjAwNzc5IDM2LjAzMTJINDguMDM2NEM1MC4yNDcgMzYuMDMxMiA1Mi4wMzkgMzQuMjM5MiA1Mi4wMzkgMzIuMDI4NlY0LjAxMDQyQzUyLjAzOSAxLjc5OTg0IDUwLjI0NyAwLjAwNzgxMjUgNDguMDM2NCAwLjAwNzgxMjVINC4wMDc3OVpNOC4wMTA0MiA4LjAxMzAySDEyLjAxM1YxMi4wMTU2SDguMDEwNDJWOC4wMTMwMlpNMjAuMDE4MiA4LjAxMzAySDE2LjAxNTZWMTIuMDE1NkgyMC4wMTgyVjguMDEzMDJaTTI0LjAyMDggOC4wMTMwMkgyOC4wMjM0VjEyLjAxNTZIMjQuMDIwOFY4LjAxMzAyWk0zNi4wMjg2IDguMDEzMDJIMzIuMDI2VjEyLjAxNTZIMzYuMDI4NlY4LjAxMzAyWk00MC4wMzEyIDguMDEzMDJINDQuMDMzOVYxMi4wMTU2SDQwLjAzMTJWOC4wMTMwMlpNMTYuMDE1NiAxNi4wMTgySDguMDEwNDJWMjAuMDIwOEgxNi4wMTU2VjE2LjAxODJaTTIwLjAxODIgMTYuMDE4MkgyNC4wMjA4VjIwLjAyMDhIMjAuMDE4MlYxNi4wMTgyWk0zMi4wMjYgMTYuMDE4MkgyOC4wMjM0VjIwLjAyMDhIMzIuMDI2VjE2LjAxODJaTTQ0LjAzMzkgMTYuMDE4MlYyMC4wMjA4SDM2LjAyODZWMTYuMDE4Mkg0NC4wMzM5Wk0xMi4wMTMgMjQuMDIzNEg4LjAxMDQyVjI4LjAyNkgxMi4wMTNWMjQuMDIzNFpNMTYuMDE1NiAyNC4wMjM0SDM2LjAyODZWMjguMDI2SDE2LjAxNTZWMjQuMDIzNFpNNDQuMDMzOSAyNC4wMjM0SDQwLjAzMTJWMjguMDI2SDQ0LjAzMzlWMjQuMDIzNFoiIGZpbGw9IiNDNUM1QzUiLz4NCjwvZz4NCjxkZWZzPg0KPGNsaXBQYXRoIGlkPSJjbGlwMCI+DQo8cmVjdCB3aWR0aD0iNTMiIGhlaWdodD0iMzYiIGZpbGw9IndoaXRlIi8+DQo8L2NsaXBQYXRoPg0KPC9kZWZzPg0KPC9zdmc+DQo=") center center no-repeat;
	border: 4px solid #252526;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .tokens-inspect-widget {
	z-index: 50;
	user-select: text;
	-webkit-user-select: text;
	-ms-user-select: text;
	padding: 10px;
}

.tokens-inspect-separator {
	height: 1px;
	border: 0;
}

.monaco-editor .tokens-inspect-widget .tm-token {
	font-family: monospace;
}

.monaco-editor .tokens-inspect-widget .tm-token-length {
	font-weight: normal;
	font-size: 60%;
	float: right;
}

.monaco-editor .tokens-inspect-widget .tm-metadata-table {
	width: 100%;
}

.monaco-editor .tokens-inspect-widget .tm-metadata-value {
	font-family: monospace;
	text-align: right;
}

.monaco-editor .tokens-inspect-widget .tm-token-type {
	font-family: monospace;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
.monaco-editor .detected-link,
.monaco-editor .detected-link-active {
	text-decoration: underline;
	text-underline-position: under;
}

.monaco-editor .detected-link-active {
	cursor: pointer;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .parameter-hints-widget {
	z-index: 10;
	display: flex;
	flex-direction: column;
	line-height: 1.5em;
}

.monaco-editor .parameter-hints-widget > .wrapper {
	max-width: 440px;
	display: flex;
	flex-direction: row;
}

.monaco-editor .parameter-hints-widget.multiple {
	min-height: 3.3em;
	padding: 0;
}

.monaco-editor .parameter-hints-widget.visible {
	transition: left .05s ease-in-out;
}

.monaco-editor .parameter-hints-widget p,
.monaco-editor .parameter-hints-widget ul {
	margin: 8px 0;
}

.monaco-editor .parameter-hints-widget .monaco-scrollable-element,
.monaco-editor .parameter-hints-widget .body {
	display: flex;
	flex-direction: column;
	min-height: 100%;
}

.monaco-editor .parameter-hints-widget .signature {
	padding: 4px 5px;
}

.monaco-editor .parameter-hints-widget .docs {
	padding: 0 10px 0 5px;
	white-space: pre-wrap;
}

.monaco-editor .parameter-hints-widget .docs.empty {
	display: none;
}

.monaco-editor .parameter-hints-widget .docs .markdown-docs {
	white-space: initial;
}

.monaco-editor .parameter-hints-widget .docs .markdown-docs code {
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .parameter-hints-widget .docs .code {
	white-space: pre-wrap;
}

.monaco-editor .parameter-hints-widget .docs code {
	border-radius: 3px;
	padding: 0 0.4em;
}

.monaco-editor .parameter-hints-widget .controls {
	display: none;
	flex-direction: column;
	align-items: center;
	min-width: 22px;
	justify-content: flex-end;
}

.monaco-editor .parameter-hints-widget.multiple .controls {
	display: flex;
	padding: 0 2px;
}

.monaco-editor .parameter-hints-widget.multiple .button {
	width: 16px;
	height: 16px;
	background-repeat: no-repeat;
	cursor: pointer;
}

.monaco-editor .parameter-hints-widget .button.previous {
	bottom: 24px;
}

.monaco-editor .parameter-hints-widget .overloads {
	text-align: center;
	height: 12px;
	line-height: 12px;
	opacity: 0.5;
	font-family: var(--monaco-monospace-font);
}

.monaco-editor .parameter-hints-widget .signature .parameter.active {
	font-weight: bold;
	text-decoration: underline;
}

.monaco-editor .parameter-hints-widget .documentation-parameter > .parameter {
	font-weight: bold;
	margin-right: 0.5em;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-quick-open-widget {
	font-size: 13px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

@font-face {
	font-family: "codicon";
	src: url(/assets/webpack/codicon.a609dc0f.ttf) format("truetype");
}

.codicon[class*='codicon-'] {
	font: normal normal normal 16px/1 codicon;
	display: inline-block;
	text-decoration: none;
	text-rendering: auto;
	text-align: center;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}


.codicon-add:before { content: "\ea60" }
.codicon-plus:before { content: "\ea60" }
.codicon-gist-new:before { content: "\ea60" }
.codicon-repo-create:before { content: "\ea60" }
.codicon-lightbulb:before { content: "\ea61" }
.codicon-light-bulb:before { content: "\ea61" }
.codicon-repo:before { content: "\ea62" }
.codicon-repo-delete:before { content: "\ea62" }
.codicon-gist-fork:before { content: "\ea63" }
.codicon-repo-forked:before { content: "\ea63" }
.codicon-git-pull-request:before { content: "\ea64" }
.codicon-git-pull-request-abandoned:before { content: "\ea64" }
.codicon-record-keys:before { content: "\ea65" }
.codicon-keyboard:before { content: "\ea65" }
.codicon-tag:before { content: "\ea66" }
.codicon-tag-add:before { content: "\ea66" }
.codicon-tag-remove:before { content: "\ea66" }
.codicon-person:before { content: "\ea67" }
.codicon-person-add:before { content: "\ea67" }
.codicon-person-follow:before { content: "\ea67" }
.codicon-person-outline:before { content: "\ea67" }
.codicon-person-filled:before { content: "\ea67" }
.codicon-git-branch:before { content: "\ea68" }
.codicon-git-branch-create:before { content: "\ea68" }
.codicon-git-branch-delete:before { content: "\ea68" }
.codicon-source-control:before { content: "\ea68" }
.codicon-mirror:before { content: "\ea69" }
.codicon-mirror-public:before { content: "\ea69" }
.codicon-star:before { content: "\ea6a" }
.codicon-star-add:before { content: "\ea6a" }
.codicon-star-delete:before { content: "\ea6a" }
.codicon-star-empty:before { content: "\ea6a" }
.codicon-comment:before { content: "\ea6b" }
.codicon-comment-add:before { content: "\ea6b" }
.codicon-alert:before { content: "\ea6c" }
.codicon-warning:before { content: "\ea6c" }
.codicon-search:before { content: "\ea6d" }
.codicon-search-save:before { content: "\ea6d" }
.codicon-log-out:before { content: "\ea6e" }
.codicon-sign-out:before { content: "\ea6e" }
.codicon-log-in:before { content: "\ea6f" }
.codicon-sign-in:before { content: "\ea6f" }
.codicon-eye:before { content: "\ea70" }
.codicon-eye-unwatch:before { content: "\ea70" }
.codicon-eye-watch:before { content: "\ea70" }
.codicon-circle-filled:before { content: "\ea71" }
.codicon-primitive-dot:before { content: "\ea71" }
.codicon-close-dirty:before { content: "\ea71" }
.codicon-debug-breakpoint:before { content: "\ea71" }
.codicon-debug-breakpoint-disabled:before { content: "\ea71" }
.codicon-debug-hint:before { content: "\ea71" }
.codicon-primitive-square:before { content: "\ea72" }
.codicon-edit:before { content: "\ea73" }
.codicon-pencil:before { content: "\ea73" }
.codicon-info:before { content: "\ea74" }
.codicon-issue-opened:before { content: "\ea74" }
.codicon-gist-private:before { content: "\ea75" }
.codicon-git-fork-private:before { content: "\ea75" }
.codicon-lock:before { content: "\ea75" }
.codicon-mirror-private:before { content: "\ea75" }
.codicon-close:before { content: "\ea76" }
.codicon-remove-close:before { content: "\ea76" }
.codicon-x:before { content: "\ea76" }
.codicon-repo-sync:before { content: "\ea77" }
.codicon-sync:before { content: "\ea77" }
.codicon-clone:before { content: "\ea78" }
.codicon-desktop-download:before { content: "\ea78" }
.codicon-beaker:before { content: "\ea79" }
.codicon-microscope:before { content: "\ea79" }
.codicon-vm:before { content: "\ea7a" }
.codicon-device-desktop:before { content: "\ea7a" }
.codicon-file:before { content: "\ea7b" }
.codicon-file-text:before { content: "\ea7b" }
.codicon-more:before { content: "\ea7c" }
.codicon-ellipsis:before { content: "\ea7c" }
.codicon-kebab-horizontal:before { content: "\ea7c" }
.codicon-mail-reply:before { content: "\ea7d" }
.codicon-reply:before { content: "\ea7d" }
.codicon-organization:before { content: "\ea7e" }
.codicon-organization-filled:before { content: "\ea7e" }
.codicon-organization-outline:before { content: "\ea7e" }
.codicon-new-file:before { content: "\ea7f" }
.codicon-file-add:before { content: "\ea7f" }
.codicon-new-folder:before { content: "\ea80" }
.codicon-file-directory-create:before { content: "\ea80" }
.codicon-trash:before { content: "\ea81" }
.codicon-trashcan:before { content: "\ea81" }
.codicon-history:before { content: "\ea82" }
.codicon-clock:before { content: "\ea82" }
.codicon-folder:before { content: "\ea83" }
.codicon-file-directory:before { content: "\ea83" }
.codicon-symbol-folder:before { content: "\ea83" }
.codicon-logo-github:before { content: "\ea84" }
.codicon-mark-github:before { content: "\ea84" }
.codicon-github:before { content: "\ea84" }
.codicon-terminal:before { content: "\ea85" }
.codicon-console:before { content: "\ea85" }
.codicon-repl:before { content: "\ea85" }
.codicon-zap:before { content: "\ea86" }
.codicon-symbol-event:before { content: "\ea86" }
.codicon-error:before { content: "\ea87" }
.codicon-stop:before { content: "\ea87" }
.codicon-variable:before { content: "\ea88" }
.codicon-symbol-variable:before { content: "\ea88" }
.codicon-array:before { content: "\ea8a" }
.codicon-symbol-array:before { content: "\ea8a" }
.codicon-symbol-module:before { content: "\ea8b" }
.codicon-symbol-package:before { content: "\ea8b" }
.codicon-symbol-namespace:before { content: "\ea8b" }
.codicon-symbol-object:before { content: "\ea8b" }
.codicon-symbol-method:before { content: "\ea8c" }
.codicon-symbol-function:before { content: "\ea8c" }
.codicon-symbol-constructor:before { content: "\ea8c" }
.codicon-symbol-boolean:before { content: "\ea8f" }
.codicon-symbol-null:before { content: "\ea8f" }
.codicon-symbol-numeric:before { content: "\ea90" }
.codicon-symbol-number:before { content: "\ea90" }
.codicon-symbol-structure:before { content: "\ea91" }
.codicon-symbol-struct:before { content: "\ea91" }
.codicon-symbol-parameter:before { content: "\ea92" }
.codicon-symbol-type-parameter:before { content: "\ea92" }
.codicon-symbol-key:before { content: "\ea93" }
.codicon-symbol-text:before { content: "\ea93" }
.codicon-symbol-reference:before { content: "\ea94" }
.codicon-go-to-file:before { content: "\ea94" }
.codicon-symbol-enum:before { content: "\ea95" }
.codicon-symbol-value:before { content: "\ea95" }
.codicon-symbol-ruler:before { content: "\ea96" }
.codicon-symbol-unit:before { content: "\ea96" }
.codicon-activate-breakpoints:before { content: "\ea97" }
.codicon-archive:before { content: "\ea98" }
.codicon-arrow-both:before { content: "\ea99" }
.codicon-arrow-down:before { content: "\ea9a" }
.codicon-arrow-left:before { content: "\ea9b" }
.codicon-arrow-right:before { content: "\ea9c" }
.codicon-arrow-small-down:before { content: "\ea9d" }
.codicon-arrow-small-left:before { content: "\ea9e" }
.codicon-arrow-small-right:before { content: "\ea9f" }
.codicon-arrow-small-up:before { content: "\eaa0" }
.codicon-arrow-up:before { content: "\eaa1" }
.codicon-bell:before { content: "\eaa2" }
.codicon-bold:before { content: "\eaa3" }
.codicon-book:before { content: "\eaa4" }
.codicon-bookmark:before { content: "\eaa5" }
.codicon-debug-breakpoint-conditional-unverified:before { content: "\eaa6" }
.codicon-debug-breakpoint-conditional:before { content: "\eaa7" }
.codicon-debug-breakpoint-conditional-disabled:before { content: "\eaa7" }
.codicon-debug-breakpoint-data-unverified:before { content: "\eaa8" }
.codicon-debug-breakpoint-data:before { content: "\eaa9" }
.codicon-debug-breakpoint-data-disabled:before { content: "\eaa9" }
.codicon-debug-breakpoint-log-unverified:before { content: "\eaaa" }
.codicon-debug-breakpoint-log:before { content: "\eaab" }
.codicon-debug-breakpoint-log-disabled:before { content: "\eaab" }
.codicon-briefcase:before { content: "\eaac" }
.codicon-broadcast:before { content: "\eaad" }
.codicon-browser:before { content: "\eaae" }
.codicon-bug:before { content: "\eaaf" }
.codicon-calendar:before { content: "\eab0" }
.codicon-case-sensitive:before { content: "\eab1" }
.codicon-check:before { content: "\eab2" }
.codicon-checklist:before { content: "\eab3" }
.codicon-chevron-down:before { content: "\eab4" }
.codicon-chevron-left:before { content: "\eab5" }
.codicon-chevron-right:before { content: "\eab6" }
.codicon-chevron-up:before { content: "\eab7" }
.codicon-chrome-close:before { content: "\eab8" }
.codicon-chrome-maximize:before { content: "\eab9" }
.codicon-chrome-minimize:before { content: "\eaba" }
.codicon-chrome-restore:before { content: "\eabb" }
.codicon-circle-outline:before { content: "\eabc" }
.codicon-debug-breakpoint-unverified:before { content: "\eabc" }
.codicon-circle-slash:before { content: "\eabd" }
.codicon-circuit-board:before { content: "\eabe" }
.codicon-clear-all:before { content: "\eabf" }
.codicon-clippy:before { content: "\eac0" }
.codicon-close-all:before { content: "\eac1" }
.codicon-cloud-download:before { content: "\eac2" }
.codicon-cloud-upload:before { content: "\eac3" }
.codicon-code:before { content: "\eac4" }
.codicon-collapse-all:before { content: "\eac5" }
.codicon-color-mode:before { content: "\eac6" }
.codicon-comment-discussion:before { content: "\eac7" }
.codicon-compare-changes:before { content: "\eac8" }
.codicon-credit-card:before { content: "\eac9" }
.codicon-dash:before { content: "\eacc" }
.codicon-dashboard:before { content: "\eacd" }
.codicon-database:before { content: "\eace" }
.codicon-debug-continue:before { content: "\eacf" }
.codicon-debug-disconnect:before { content: "\ead0" }
.codicon-debug-pause:before { content: "\ead1" }
.codicon-debug-restart:before { content: "\ead2" }
.codicon-debug-start:before { content: "\ead3" }
.codicon-debug-step-into:before { content: "\ead4" }
.codicon-debug-step-out:before { content: "\ead5" }
.codicon-debug-step-over:before { content: "\ead6" }
.codicon-debug-stop:before { content: "\ead7" }
.codicon-debug:before { content: "\ead8" }
.codicon-device-camera-video:before { content: "\ead9" }
.codicon-device-camera:before { content: "\eada" }
.codicon-device-mobile:before { content: "\eadb" }
.codicon-diff-added:before { content: "\eadc" }
.codicon-diff-ignored:before { content: "\eadd" }
.codicon-diff-modified:before { content: "\eade" }
.codicon-diff-removed:before { content: "\eadf" }
.codicon-diff-renamed:before { content: "\eae0" }
.codicon-diff:before { content: "\eae1" }
.codicon-discard:before { content: "\eae2" }
.codicon-editor-layout:before { content: "\eae3" }
.codicon-empty-window:before { content: "\eae4" }
.codicon-exclude:before { content: "\eae5" }
.codicon-extensions:before { content: "\eae6" }
.codicon-eye-closed:before { content: "\eae7" }
.codicon-file-binary:before { content: "\eae8" }
.codicon-file-code:before { content: "\eae9" }
.codicon-file-media:before { content: "\eaea" }
.codicon-file-pdf:before { content: "\eaeb" }
.codicon-file-submodule:before { content: "\eaec" }
.codicon-file-symlink-directory:before { content: "\eaed" }
.codicon-file-symlink-file:before { content: "\eaee" }
.codicon-file-zip:before { content: "\eaef" }
.codicon-files:before { content: "\eaf0" }
.codicon-filter:before { content: "\eaf1" }
.codicon-flame:before { content: "\eaf2" }
.codicon-fold-down:before { content: "\eaf3" }
.codicon-fold-up:before { content: "\eaf4" }
.codicon-fold:before { content: "\eaf5" }
.codicon-folder-active:before { content: "\eaf6" }
.codicon-folder-opened:before { content: "\eaf7" }
.codicon-gear:before { content: "\eaf8" }
.codicon-gift:before { content: "\eaf9" }
.codicon-gist-secret:before { content: "\eafa" }
.codicon-gist:before { content: "\eafb" }
.codicon-git-commit:before { content: "\eafc" }
.codicon-git-compare:before { content: "\eafd" }
.codicon-git-merge:before { content: "\eafe" }
.codicon-github-action:before { content: "\eaff" }
.codicon-github-alt:before { content: "\eb00" }
.codicon-globe:before { content: "\eb01" }
.codicon-grabber:before { content: "\eb02" }
.codicon-graph:before { content: "\eb03" }
.codicon-gripper:before { content: "\eb04" }
.codicon-heart:before { content: "\eb05" }
.codicon-home:before { content: "\eb06" }
.codicon-horizontal-rule:before { content: "\eb07" }
.codicon-hubot:before { content: "\eb08" }
.codicon-inbox:before { content: "\eb09" }
.codicon-issue-closed:before { content: "\eb0a" }
.codicon-issue-reopened:before { content: "\eb0b" }
.codicon-issues:before { content: "\eb0c" }
.codicon-italic:before { content: "\eb0d" }
.codicon-jersey:before { content: "\eb0e" }
.codicon-json:before { content: "\eb0f" }
.codicon-kebab-vertical:before { content: "\eb10" }
.codicon-key:before { content: "\eb11" }
.codicon-law:before { content: "\eb12" }
.codicon-lightbulb-autofix:before { content: "\eb13" }
.codicon-link-external:before { content: "\eb14" }
.codicon-link:before { content: "\eb15" }
.codicon-list-ordered:before { content: "\eb16" }
.codicon-list-unordered:before { content: "\eb17" }
.codicon-live-share:before { content: "\eb18" }
.codicon-loading:before { content: "\eb19" }
.codicon-location:before { content: "\eb1a" }
.codicon-mail-read:before { content: "\eb1b" }
.codicon-mail:before { content: "\eb1c" }
.codicon-markdown:before { content: "\eb1d" }
.codicon-megaphone:before { content: "\eb1e" }
.codicon-mention:before { content: "\eb1f" }
.codicon-milestone:before { content: "\eb20" }
.codicon-mortar-board:before { content: "\eb21" }
.codicon-move:before { content: "\eb22" }
.codicon-multiple-windows:before { content: "\eb23" }
.codicon-mute:before { content: "\eb24" }
.codicon-no-newline:before { content: "\eb25" }
.codicon-note:before { content: "\eb26" }
.codicon-octoface:before { content: "\eb27" }
.codicon-open-preview:before { content: "\eb28" }
.codicon-package:before { content: "\eb29" }
.codicon-paintcan:before { content: "\eb2a" }
.codicon-pin:before { content: "\eb2b" }
.codicon-play:before { content: "\eb2c" }
.codicon-plug:before { content: "\eb2d" }
.codicon-preserve-case:before { content: "\eb2e" }
.codicon-preview:before { content: "\eb2f" }
.codicon-project:before { content: "\eb30" }
.codicon-pulse:before { content: "\eb31" }
.codicon-question:before { content: "\eb32" }
.codicon-quote:before { content: "\eb33" }
.codicon-radio-tower:before { content: "\eb34" }
.codicon-reactions:before { content: "\eb35" }
.codicon-references:before { content: "\eb36" }
.codicon-refresh:before { content: "\eb37" }
.codicon-regex:before { content: "\eb38" }
.codicon-remote-explorer:before { content: "\eb39" }
.codicon-remote:before { content: "\eb3a" }
.codicon-remove:before { content: "\eb3b" }
.codicon-replace-all:before { content: "\eb3c" }
.codicon-replace:before { content: "\eb3d" }
.codicon-repo-clone:before { content: "\eb3e" }
.codicon-repo-force-push:before { content: "\eb3f" }
.codicon-repo-pull:before { content: "\eb40" }
.codicon-repo-push:before { content: "\eb41" }
.codicon-report:before { content: "\eb42" }
.codicon-request-changes:before { content: "\eb43" }
.codicon-rocket:before { content: "\eb44" }
.codicon-root-folder-opened:before { content: "\eb45" }
.codicon-root-folder:before { content: "\eb46" }
.codicon-rss:before { content: "\eb47" }
.codicon-ruby:before { content: "\eb48" }
.codicon-save-all:before { content: "\eb49" }
.codicon-save-as:before { content: "\eb4a" }
.codicon-save:before { content: "\eb4b" }
.codicon-screen-full:before { content: "\eb4c" }
.codicon-screen-normal:before { content: "\eb4d" }
.codicon-search-stop:before { content: "\eb4e" }
.codicon-server:before { content: "\eb50" }
.codicon-settings-gear:before { content: "\eb51" }
.codicon-settings:before { content: "\eb52" }
.codicon-shield:before { content: "\eb53" }
.codicon-smiley:before { content: "\eb54" }
.codicon-sort-precedence:before { content: "\eb55" }
.codicon-split-horizontal:before { content: "\eb56" }
.codicon-split-vertical:before { content: "\eb57" }
.codicon-squirrel:before { content: "\eb58" }
.codicon-star-full:before { content: "\eb59" }
.codicon-star-half:before { content: "\eb5a" }
.codicon-symbol-class:before { content: "\eb5b" }
.codicon-symbol-color:before { content: "\eb5c" }
.codicon-symbol-constant:before { content: "\eb5d" }
.codicon-symbol-enum-member:before { content: "\eb5e" }
.codicon-symbol-field:before { content: "\eb5f" }
.codicon-symbol-file:before { content: "\eb60" }
.codicon-symbol-interface:before { content: "\eb61" }
.codicon-symbol-keyword:before { content: "\eb62" }
.codicon-symbol-misc:before { content: "\eb63" }
.codicon-symbol-operator:before { content: "\eb64" }
.codicon-symbol-property:before { content: "\eb65" }
.codicon-symbol-snippet:before { content: "\eb66" }
.codicon-tasklist:before { content: "\eb67" }
.codicon-telescope:before { content: "\eb68" }
.codicon-text-size:before { content: "\eb69" }
.codicon-three-bars:before { content: "\eb6a" }
.codicon-thumbsdown:before { content: "\eb6b" }
.codicon-thumbsup:before { content: "\eb6c" }
.codicon-tools:before { content: "\eb6d" }
.codicon-triangle-down:before { content: "\eb6e" }
.codicon-triangle-left:before { content: "\eb6f" }
.codicon-triangle-right:before { content: "\eb70" }
.codicon-triangle-up:before { content: "\eb71" }
.codicon-twitter:before { content: "\eb72" }
.codicon-unfold:before { content: "\eb73" }
.codicon-unlock:before { content: "\eb74" }
.codicon-unmute:before { content: "\eb75" }
.codicon-unverified:before { content: "\eb76" }
.codicon-verified:before { content: "\eb77" }
.codicon-versions:before { content: "\eb78" }
.codicon-vm-active:before { content: "\eb79" }
.codicon-vm-outline:before { content: "\eb7a" }
.codicon-vm-running:before { content: "\eb7b" }
.codicon-watch:before { content: "\eb7c" }
.codicon-whitespace:before { content: "\eb7d" }
.codicon-whole-word:before { content: "\eb7e" }
.codicon-window:before { content: "\eb7f" }
.codicon-word-wrap:before { content: "\eb80" }
.codicon-zoom-in:before { content: "\eb81" }
.codicon-zoom-out:before { content: "\eb82" }
.codicon-list-filter:before { content: "\eb83" }
.codicon-list-flat:before { content: "\eb84" }
.codicon-list-selection:before { content: "\eb85" }
.codicon-selection:before { content: "\eb85" }
.codicon-list-tree:before { content: "\eb86" }
.codicon-debug-breakpoint-function-unverified:before { content: "\eb87" }
.codicon-debug-breakpoint-function:before { content: "\eb88" }
.codicon-debug-breakpoint-function-disabled:before { content: "\eb88" }
.codicon-debug-stackframe-active:before { content: "\eb89" }
.codicon-debug-stackframe-dot:before { content: "\eb8a" }
.codicon-debug-stackframe:before { content: "\eb8b" }
.codicon-debug-stackframe-focused:before { content: "\eb8b" }
.codicon-debug-breakpoint-unsupported:before { content: "\eb8c" }
.codicon-symbol-string:before { content: "\eb8d" }
.codicon-debug-reverse-continue:before { content: "\eb8e" }
.codicon-debug-step-back:before { content: "\eb8f" }
.codicon-debug-restart-frame:before { content: "\eb90" }
.codicon-debug-alternate:before { content: "\eb91" }
.codicon-call-incoming:before { content: "\eb92" }
.codicon-call-outgoing:before { content: "\eb93" }
.codicon-menu:before { content: "\eb94" }
.codicon-expand-all:before { content: "\eb95" }
.codicon-feedback:before { content: "\eb96" }
.codicon-group-by-ref-type:before { content: "\eb97" }
.codicon-ungroup-by-ref-type:before { content: "\eb98" }
.codicon-debug-alt:before { content: "\f101" }
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

@keyframes codicon-spin {
	100% {
		transform:rotate(360deg);
	}
}

.codicon-animation-spin {
	animation: codicon-spin 1.5s linear infinite;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-list .monaco-list-row.focused.selected .outline-element .monaco-highlighted-label,
.monaco-list .monaco-list-row.focused.selected .outline-element-decoration {
	/* make sure selection color wins when a label is being selected */
	color: inherit !important;
}

.monaco-list .outline-element {
	display: flex;
	flex: 1;
	flex-flow: row nowrap;
	align-items: center;
}

.monaco-list .outline-element .monaco-highlighted-label {
	color: var(--outline-element-color);
}

.monaco-tree .monaco-tree-row.focused .outline-element .outline-element-detail {
	visibility: inherit;
}

.monaco-list .outline-element .outline-element-decoration {
	opacity: 0.75;
	font-size: 90%;
	font-weight: 600;
	padding: 0 12px 0 5px;
	margin-left: auto;
	text-align: center;
	color: var(--outline-element-color);
}

.monaco-list .outline-element .outline-element-decoration.bubble {
	font-family: codicon;
	font-size: 14px;
	opacity: 0.4;
}

.monaco-list .outline-element .outline-element-icon {
	margin-right: 4px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-icon-label.deprecated {
	text-decoration: line-through;
	opacity: 0.66;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .rename-box {
	z-index: 100;
	color: inherit;
}

.monaco-editor .rename-box.preview {
	padding: 3px 3px 0 3px;
}

.monaco-editor .rename-box .rename-input {
	padding: 3px;
	width: calc(100% - 6px);
}

.monaco-editor .rename-box .rename-label {
	display: none;
	opacity: .8;
}

.monaco-editor .rename-box.preview .rename-label {
	display: inherit;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .snippet-placeholder {
	min-width: 2px;
	outline-style: solid;
	outline-width: 1px;
}

.monaco-editor .finish-snippet-placeholder {
	outline-style: solid;
	outline-width: 1px;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

/* Suggest widget*/
.monaco-editor .suggest-widget {
	z-index: 40;
}

/** Initial widths **/

.monaco-editor .suggest-widget {
	width: 430px;
}

.monaco-editor .suggest-widget > .message,
.monaco-editor .suggest-widget > .tree,
.monaco-editor .suggest-widget > .details {
	width: 100%;
	border-style: solid;
	border-width: 1px;
	box-sizing: border-box;
}

.monaco-editor.hc-black .suggest-widget > .message,
.monaco-editor.hc-black .suggest-widget > .tree,
.monaco-editor.hc-black .suggest-widget > .details {
	border-width: 2px;
}

/** Adjust width when docs are expanded to the side **/
.monaco-editor .suggest-widget.docs-side {
	width: 660px;
}

.monaco-editor .suggest-widget.docs-side > .tree,
.monaco-editor .suggest-widget.docs-side > .details {
	width: 50%;
	float: left;
}

.monaco-editor .suggest-widget.docs-side.list-right > .tree,
.monaco-editor .suggest-widget.docs-side.list-right > .details  {
	float: right;
}

/* MarkupContent Layout */
.monaco-editor .suggest-widget > .details ul {
	padding-left: 20px;
}
.monaco-editor .suggest-widget > .details ol {
	padding-left: 20px;
}

.monaco-editor .suggest-widget > .details p code {
	font-family: var(--monaco-monospace-font);
}

/* Styles for Message element for when widget is loading or is empty */
.monaco-editor .suggest-widget > .message {
	padding-left: 22px;
}

/** Styles for the list element **/
.monaco-editor .suggest-widget > .tree {
	height: 100%;
}

.monaco-editor .suggest-widget .monaco-list {
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

/** Styles for each row in the list element **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row {
	display: flex;
	-mox-box-sizing: border-box;
	box-sizing: border-box;
	padding-right: 10px;
	background-repeat: no-repeat;
	background-position: 2px 2px;
	white-space: nowrap;
	cursor: pointer;
	touch-action: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents {
	flex: 1;
	height: 100%;
	overflow: hidden;
	padding-left: 2px;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main {
	display: flex;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: pre;
	justify-content: space-between;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .left,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right {
	display: flex;
}

.monaco-editor .suggest-widget:not(.frozen) .monaco-highlighted-label .highlight {
	font-weight: bold;
}

/** Status Bar **/

.monaco-editor .suggest-widget > .suggest-status-bar {
	visibility: hidden;

	position: absolute;
	left: 0;

	box-sizing: border-box;

	display: flex;
	flex-flow: row nowrap;
	justify-content: space-between;

	width: 100%;

	font-size: 80%;

	border-left-width: 1px;
	border-left-style: solid;
	border-right-width: 1px;
	border-right-style: solid;
	border-bottom-width: 1px;
	border-bottom-style: solid;

	padding: 1px 8px 1px 4px;

	box-shadow: 0 -.5px 3px #ddd;
}
.monaco-editor .suggest-widget > .suggest-status-bar span {
	opacity: 0.7;
}
.monaco-editor .suggest-widget.list-right.docs-side > .suggest-status-bar {
	left: auto;
	right: 0;
}
.monaco-editor .suggest-widget.docs-side > .suggest-status-bar {
	width: 50%;
}

/** ReadMore Icon styles **/

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .header > .codicon-close,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right > .readMore::before {
	color: inherit;
	opacity: 1;
	font-size: 14px;
	cursor: pointer;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .header > .codicon-close {
	position: absolute;
	top: 2px;
	right: 2px;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .header > .codicon-close:hover,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right > .readMore:hover {
	opacity: 1;
}

/** signature, qualifier, type/details opacity **/
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .left > .signature-label,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .left > .qualifier-label,
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right > .details-label {
	opacity: 0.7;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .left > .qualifier-label {
	margin-left: 4px;
	opacity: 0.4;
	font-size: 90%;
	text-overflow: ellipsis;
	overflow: hidden;
	line-height: 17px;
	align-self: center;
}

/** Type Info and icon next to the label in the focused completion item **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right > .details-label {
	margin-left: 0.8em;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right > .details-label > .monaco-tokenized-source {
	display: inline;
}

/** Details: if using CompletionItem#details, show on focus **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right > .details-label,
.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row.focused > .contents > .main > .right > .details-label {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused > .contents > .main > .right > .details-label {
	display: inline;
}

/** Details: if using CompletionItemLabel#details, always show **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right.always-show-details > .details-label,
.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row.focused > .contents > .main > .right.always-show-details > .details-label {
	display: inline;
}

/** Ellipsis on hover **/
.monaco-editor .suggest-widget:not(.docs-side) .monaco-list .monaco-list-row:hover > .contents > .main > .right.can-expand-details > .details-label {
	width: calc(100% - 26px);
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .left {
	flex-shrink: 1;
	overflow: hidden;
}
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .left > .monaco-icon-label {
	flex-shrink: 1;
}
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right {
	overflow: hidden;
	flex-shrink: 0;
	max-width: 45%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right > .readMore {
	display: inline-block;
	position: absolute;
	right: 10px;
	width: 18px;
	height: 18px;
	visibility: hidden;
}

/** Do NOT display ReadMore when docs is side/below **/
.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row > .contents > .main > .right > .readMore,
.monaco-editor .suggest-widget.docs-below .monaco-list .monaco-list-row > .contents > .main > .right > .readMore {
	display: none !important;
}

/** Do NOT display ReadMore when using plain CompletionItemLabel (details/documentation might not be resolved) **/
.monaco-editor .suggest-widget .monaco-list .monaco-list-row > .contents > .main > .right:not(.always-show-details) > .readMore {
	display: none;
}
/** Focused item can show ReadMore, but can't when docs is side/below **/
.monaco-editor .suggest-widget .monaco-list .monaco-list-row.focused > .contents > .main > .right:not(.always-show-details) > .readMore {
	display: inline-block;
}

.monaco-editor .suggest-widget.docs-side .monaco-list .monaco-list-row > .contents > .main > .right > .readMore,
.monaco-editor .suggest-widget.docs-below .monaco-list .monaco-list-row > .contents > .main > .right > .readMore {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row:hover > .contents > .main > .right > .readMore {
	visibility: visible;
}

/** Styles for each row in the list **/

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label.deprecated {
	opacity: 0.66;
	text-decoration: unset;
}
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label.deprecated > .monaco-icon-label-container > .monaco-icon-name-container {
	text-decoration: line-through;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-icon-label::before {
	height: 100%;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon {
	display: block;
	height: 16px;
	width: 16px;
	margin-left: 2px;
	background-repeat: no-repeat;
	background-size: 80%;
	background-position: center;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.hide {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .suggest-icon {
	display: flex;
	align-items: center;
	margin-right: 4px;
}

.monaco-editor .suggest-widget.no-icons .monaco-list .monaco-list-row .icon,
.monaco-editor .suggest-widget.no-icons .monaco-list .monaco-list-row .suggest-icon::before {
	display: none;
}

.monaco-editor .suggest-widget .monaco-list .monaco-list-row .icon.customcolor .colorspan {
	margin: 0 0 0 0.3em;
	border: 0.1em solid #000;
	width: 0.7em;
	height: 0.7em;
	display: inline-block;
}

/** Styles for the docs of the completion item in focus **/
.monaco-editor .suggest-widget .details {
	display: flex;
	flex-direction: column;
	cursor: default;
}

.monaco-editor .suggest-widget .details.no-docs {
	display: none;
}

.monaco-editor .suggest-widget.docs-below .details {
	border-top-width: 0;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element {
	flex: 1;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body {
	position: absolute;
	box-sizing: border-box;
	height: 100%;
	width: 100%;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .header > .type {
	flex: 2;
	overflow: hidden;
	text-overflow: ellipsis;
	opacity: 0.7;
	word-break: break-all;
	margin: 0 24px 0 0;
	padding: 4px 0 12px 5px;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .docs {
	margin: 0;
	padding: 4px 5px;
	white-space: pre-wrap;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .docs.markdown-docs {
	padding: 0;
	white-space: initial;
	min-height: calc(1rem + 8px);
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .docs.markdown-docs > div,
.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .docs.markdown-docs > span:not(:empty) {
	padding: 4px 5px;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .docs.markdown-docs > div > p:first-child {
	margin-top: 0;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .docs.markdown-docs > div > p:last-child	 {
	margin-bottom: 0;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > .docs .code {
	white-space: pre-wrap;
	word-wrap: break-word;
}

.monaco-editor .suggest-widget .details > .monaco-scrollable-element > .body > p:empty {
	display: none;
}

.monaco-editor .suggest-widget .details code {
	border-radius: 3px;
	padding: 0 0.4em;
}


/* replace/insert decorations */

.monaco-editor .suggest-insert-unexpected {
	font-style: italic;
}

</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar {
	visibility: visible;
}
.monaco-editor .suggest-widget.with-status-bar > .tree {
	margin-bottom: 18px;
}

.monaco-editor .suggest-widget.with-status-bar .suggest-status-bar span {
	min-height: 18px;
}

.monaco-editor .suggest-widget.with-status-bar .monaco-list .monaco-list-row > .contents > .main > .right > .readMore,
.monaco-editor .suggest-widget.with-status-bar .monaco-list .monaco-list-row.focused > .contents > .main > .right:not(.always-show-details) > .readMore {
	display: none;
}

.monaco-editor .suggest-widget.with-status-bar:not(.docs-side) .monaco-list .monaco-list-row:hover > .contents > .main > .right.can-expand-details > .details-label {
	width: 100%;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/


/* Default standalone editor font */
.monaco-editor {
	font-family: -apple-system, BlinkMacSystemFont, "Segoe WPC", "Segoe UI", "HelveticaNeue-Light", "Ubuntu", "Droid Sans", sans-serif;
}

.monaco-menu .monaco-action-bar.vertical .action-item .action-menu-item:focus .action-label {
	stroke-width: 1.2px;
}

.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
.monaco-editor.hc-black .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label {
	stroke-width: 1.2px;
}

.monaco-editor-hover p {
	margin: 0;
}

/* The hc-black theme is already high contrast optimized */
.monaco-editor.hc-black {
	-ms-high-contrast-adjust: none;
}
/* In case the browser goes into high contrast mode and the editor is not configured with the hc-black theme */
@media screen and (-ms-high-contrast:active) {

	/* current line highlight */
	.monaco-editor.vs .view-overlays .current-line,
	.monaco-editor.vs-dark .view-overlays .current-line {
		border-color: windowtext !important;
		border-left: 0;
		border-right: 0;
	}

	/* view cursors */
	.monaco-editor.vs .cursor,
	.monaco-editor.vs-dark .cursor {
		background-color: windowtext !important;
	}
	/* dnd target */
	.monaco-editor.vs .dnd-target,
	.monaco-editor.vs-dark .dnd-target {
		border-color: windowtext !important;
	}

	/* selected text background */
	.monaco-editor.vs .selected-text,
	.monaco-editor.vs-dark .selected-text {
		background-color: highlight !important;
	}

	/* allow the text to have a transparent background. */
	.monaco-editor.vs .view-line,
	.monaco-editor.vs-dark .view-line {
		-ms-high-contrast-adjust: none;
	}

	/* text color */
	.monaco-editor.vs .view-line span,
	.monaco-editor.vs-dark .view-line span {
		color: windowtext !important;
	}
	/* selected text color */
	.monaco-editor.vs .view-line span.inline-selected-text,
	.monaco-editor.vs-dark .view-line span.inline-selected-text {
		color: highlighttext !important;
	}

	/* allow decorations */
	.monaco-editor.vs .view-overlays,
	.monaco-editor.vs-dark .view-overlays {
		-ms-high-contrast-adjust: none;
	}

	/* various decorations */
	.monaco-editor.vs .selectionHighlight,
	.monaco-editor.vs-dark .selectionHighlight,
	.monaco-editor.vs .wordHighlight,
	.monaco-editor.vs-dark .wordHighlight,
	.monaco-editor.vs .wordHighlightStrong,
	.monaco-editor.vs-dark .wordHighlightStrong,
	.monaco-editor.vs .reference-decoration,
	.monaco-editor.vs-dark .reference-decoration {
		border: 2px dotted highlight !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .rangeHighlight,
	.monaco-editor.vs-dark .rangeHighlight {
		background: transparent !important;
		border: 1px dotted activeborder !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .bracket-match,
	.monaco-editor.vs-dark .bracket-match {
		border-color: windowtext !important;
		background: transparent !important;
	}

	/* find widget */
	.monaco-editor.vs .findMatch,
	.monaco-editor.vs-dark .findMatch,
	.monaco-editor.vs .currentFindMatch,
	.monaco-editor.vs-dark .currentFindMatch {
		border: 2px dotted activeborder !important;
		background: transparent !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .find-widget,
	.monaco-editor.vs-dark .find-widget {
		border: 1px solid windowtext;
	}

	/* list - used by suggest widget */
	.monaco-editor.vs .monaco-list .monaco-list-row,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row {
		-ms-high-contrast-adjust: none;
		color: windowtext !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row.focused,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row.focused {
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-list .monaco-list-row:hover,
	.monaco-editor.vs-dark .monaco-list .monaco-list-row:hover {
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* tree */
	.monaco-editor.vs .monaco-tree .monaco-tree-row,
	.monaco-editor.vs-dark .monaco-tree .monaco-tree-row {
		-ms-high-contrast-adjust: none;
		color: windowtext !important;
	}
	.monaco-editor.vs .monaco-tree .monaco-tree-row.selected,
	.monaco-editor.vs-dark .monaco-tree .monaco-tree-row.selected,
	.monaco-editor.vs .monaco-tree .monaco-tree-row.focused,
	.monaco-editor.vs-dark .monaco-tree .monaco-tree-row.focused {
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-tree .monaco-tree-row:hover,
	.monaco-editor.vs-dark .monaco-tree .monaco-tree-row:hover {
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* scrollbars */
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar {
		-ms-high-contrast-adjust: none;
		background: background !important;
		border: 1px solid windowtext;
		box-sizing: border-box;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider {
		background: windowtext !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider:hover,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider:hover {
		background: highlight !important;
	}
	.monaco-editor.vs .monaco-scrollable-element > .scrollbar > .slider.active,
	.monaco-editor.vs-dark .monaco-scrollable-element > .scrollbar > .slider.active {
		background: highlight !important;
	}

	/* overview ruler */
	.monaco-editor.vs .decorationsOverviewRuler,
	.monaco-editor.vs-dark .decorationsOverviewRuler {
		opacity: 0;
	}

	/* minimap */
	.monaco-editor.vs .minimap,
	.monaco-editor.vs-dark .minimap {
		display: none;
	}

	/* squiggles */
	.monaco-editor.vs .squiggly-d-error,
	.monaco-editor.vs-dark .squiggly-d-error {
		background: transparent !important;
		border-bottom: 4px double #E47777;
	}
	.monaco-editor.vs .squiggly-c-warning,
	.monaco-editor.vs-dark .squiggly-c-warning {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-b-info,
	.monaco-editor.vs-dark .squiggly-b-info {
		border-bottom: 4px double #71B771;
	}
	.monaco-editor.vs .squiggly-a-hint,
	.monaco-editor.vs-dark .squiggly-a-hint {
		border-bottom: 4px double #6c6c6c;
	}

	/* contextmenu */
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:focus .action-label {
		-ms-high-contrast-adjust: none;
		color: highlighttext !important;
		background-color: highlight !important;
	}
	.monaco-editor.vs .monaco-menu .monaco-action-bar.vertical .action-menu-item:hover .action-label,
	.monaco-editor.vs-dark .monaco-menu .monaco-action-bar.vertical .action-menu-item:hover .action-label {
		-ms-high-contrast-adjust: none;
		background: transparent !important;
		border: 1px solid highlight;
		box-sizing: border-box;
	}

	/* diff editor */
	.monaco-diff-editor.vs .diffOverviewRuler,
	.monaco-diff-editor.vs-dark .diffOverviewRuler {
		display: none;
	}
	.monaco-editor.vs .line-insert,
	.monaco-editor.vs-dark .line-insert,
	.monaco-editor.vs .line-delete,
	.monaco-editor.vs-dark .line-delete {
		background: transparent !important;
		border: 1px solid highlight !important;
		box-sizing: border-box;
	}
	.monaco-editor.vs .char-insert,
	.monaco-editor.vs-dark .char-insert,
	.monaco-editor.vs .char-delete,
	.monaco-editor.vs-dark .char-delete {
		background: transparent !important;
	}
}

/*.monaco-editor.vs [tabindex="0"]:focus {
	outline: 1px solid rgba(0, 122, 204, 0.4);
	outline-offset: -1px;
	opacity: 1 !important;
}

.monaco-editor.vs-dark [tabindex="0"]:focus {
	outline: 1px solid rgba(14, 99, 156, 0.6);
	outline-offset: -1px;
	opacity: 1 !important;
}*/
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/* ---------- DiffEditor ---------- */

.monaco-diff-editor .diffOverview {
	z-index: 9;
}

/* colors not externalized: using transparancy on background */
.monaco-diff-editor.vs			.diffOverview { background: rgba(0, 0, 0, 0.03); }
.monaco-diff-editor.vs-dark		.diffOverview { background: rgba(255, 255, 255, 0.01); }

.monaco-diff-editor .diffViewport {
	box-shadow: inset 0px 0px 1px 0px #B9B9B9;
	background: rgba(0, 0, 0, 0.10);
}

.monaco-diff-editor.vs-dark .diffViewport,
.monaco-diff-editor.hc-black .diffViewport {
	background: rgba(255, 255, 255, 0.10);
}
.monaco-scrollable-element.modified-in-monaco-diff-editor.vs		.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.vs-dark	.scrollbar { background: rgba(0,0,0,0); }
.monaco-scrollable-element.modified-in-monaco-diff-editor.hc-black	.scrollbar { background: none; }

.monaco-scrollable-element.modified-in-monaco-diff-editor .slider {
	z-index: 10;
}
.modified-in-monaco-diff-editor				.slider.active { background: rgba(171, 171, 171, .4); }
.modified-in-monaco-diff-editor.hc-black	.slider.active { background: none; }

/* ---------- Diff ---------- */

.monaco-editor .insert-sign,
.monaco-diff-editor .insert-sign,
.monaco-editor .delete-sign,
.monaco-diff-editor .delete-sign {
	font-size: 11px !important;
	opacity: 0.7 !important;
	display: flex !important;
	align-items: center;
}
.monaco-editor.hc-black .insert-sign,
.monaco-diff-editor.hc-black .insert-sign,
.monaco-editor.hc-black .delete-sign,
.monaco-diff-editor.hc-black .delete-sign {
	opacity: 1;
}

.monaco-editor .inline-deleted-margin-view-zone {
	text-align: right;
}
.monaco-editor .inline-added-margin-view-zone {
	text-align: right;
}

.monaco-editor .diagonal-fill {
	background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAJCAYAAADgkQYQAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAadEVYdFNvZnR3YXJlAFBhaW50Lk5FVCB2My41LjEwMPRyoQAAAChJREFUKFNjOH/+fAMDDgCSu3Dhwn9c8gwwBTgNGR4KQP4HhQOhsAIAZCBTkhtqePcAAAAASUVORK5CYII=");
}
.monaco-editor.vs-dark .diagonal-fill {
	opacity: 0.2;
}
.monaco-editor.hc-black .diagonal-fill {
	background: none;
}

/* ---------- Inline Diff ---------- */

.monaco-editor .view-zones .view-lines .view-line span {
	display: inline-block;
}

.monaco-editor .margin-view-zones .lightbulb-glyph:hover {
	cursor: pointer;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.monaco-diff-editor .diff-review-line-number {
	text-align: right;
	display: inline-block;
}

.monaco-diff-editor .diff-review {
	position: absolute;
	user-select: none;
	-webkit-user-select: none;
	-ms-user-select: none;
}

.monaco-diff-editor .diff-review-summary {
	padding-left: 10px;
}

.monaco-diff-editor .diff-review-shadow {
	position: absolute;
}

.monaco-diff-editor .diff-review-row {
	white-space: pre;
}

.monaco-diff-editor .diff-review-table {
	display: table;
	min-width: 100%;
}

.monaco-diff-editor .diff-review-row {
	display: table-row;
	width: 100%;
}

.monaco-diff-editor .diff-review-cell {
	display: table-cell;
}

.monaco-diff-editor .diff-review-spacer {
	display: inline-block;
	width: 10px;
}

.monaco-diff-editor .diff-review-actions {
	display: inline-block;
	position: absolute;
	right: 10px;
	top: 2px;
}

.monaco-diff-editor .diff-review-actions .action-label {
	width: 16px;
	height: 16px;
	margin: 2px 0;
}
</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view .monaco-menu {
	min-width: 130px;
}

.context-view-block {
	position: fixed;
	left:0;
	top:0;
	z-index: -1;
	width: 100%;
	height: 100%;
}</style><style type="text/css">/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.context-view {
	position: absolute;
	z-index: 2500;
}
</style><script charset="utf-8" src="msGraphAPI_files/537.js"></script><style type="text/css" media="screen" class="monaco-colors">.monaco-editor .accessibilityHelpWidget { background-color: #f3f3f3; }
.monaco-editor .accessibilityHelpWidget { color: #616161; }
.monaco-editor .accessibilityHelpWidget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor, .monaco-editor-background, .monaco-editor .inputarea.ime-input { background-color: #fffffe; }
.monaco-editor, .monaco-editor .inputarea.ime-input { color: #2e2e2e; }
.monaco-editor .margin { background-color: #fffffe; }
.monaco-editor .rangeHighlight { background-color: rgba(253, 255, 0, 0.2); }
.monaco-editor .symbolHighlight { background-color: rgba(234, 92, 0, 0.33); }
.vs-whitespace { color: #bbbbbb !important; }
.monaco-editor .bracket-match { background-color: rgba(0, 100, 0, 0.1); }
.monaco-editor .bracket-match { border: 1px solid #b9b9b9; }
.monaco-editor .monaco-editor-overlaymessage .anchor { border-top-color: #007acc; }
.monaco-editor .monaco-editor-overlaymessage .message { border: 1px solid #007acc; }
.monaco-editor .monaco-editor-overlaymessage .message { background-color: #d6ecf2; }

		.monaco-editor .contentWidgets .codicon-lightbulb {
			color: #ddb100;
		}

		.monaco-editor .contentWidgets .codicon-lightbulb-autofix {
			color: #007acc;
		}
.monaco-editor .codelens-decoration { color: #999999; }
.monaco-editor .codelens-decoration .codicon { color: #999999; }
.monaco-editor .codelens-decoration > a:hover { color: #0000ff !important; }
.monaco-editor .codelens-decoration > a:hover .codicon { color: #0000ff !important; }
.monaco-editor .findOptionsWidget { background-color: #f3f3f3; }
.monaco-editor .findOptionsWidget { color: #616161; }
.monaco-editor .findOptionsWidget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 2px 8px #a8a8a8; }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; width: 3px !important; margin-left: -4px;}
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: rgba(0, 122, 204, 0.4); }
.monaco-editor .folded-background { background-color: rgba(170, 214, 248, 0.3); }
.monaco-editor .line-numbers { color: #cccccc; }
.monaco-editor .current-line ~ .line-numbers { color: #0b216f; }
.monaco-editor .view-overlays .current-line { background-color: #fffeeb; }
.monaco-editor .margin-view-overlays .current-line-margin { background-color: #fffeeb; border: none; }
.monaco-editor .lines-content .cigr { box-shadow: 1px 0 0 0 #bbbbbb inset; }
.monaco-editor .lines-content .cigra { box-shadow: 1px 0 0 0 #cccccc inset; }
.monaco-editor .minimap-slider, .monaco-editor .minimap-slider .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.2); }
.monaco-editor .minimap-slider:hover, .monaco-editor .minimap-slider:hover .minimap-slider-horizontal { background: rgba(100, 100, 100, 0.35); }
.monaco-editor .minimap-slider.active, .monaco-editor .minimap-slider.active .minimap-slider-horizontal { background: rgba(0, 0, 0, 0.3); }
.monaco-editor .minimap-shadow-visible { box-shadow: #dddddd -6px 0 6px -6px inset; }
.monaco-editor .view-ruler { box-shadow: 1px 0 0 0 #d3d3d3 inset; }
.monaco-editor .scroll-decoration { box-shadow: #dddddd 0 6px 6px -6px inset; }
.monaco-editor .focused .selected-text { background-color: #aad6f8; }
.monaco-editor .selected-text { background-color: rgba(170, 214, 248, 0.5); }
.monaco-editor .cursor { background-color: #666666; border-color: #666666; color: #999999; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e9a700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%2375beff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor .squiggly-inline-deprecated { text-decoration: line-through; text-decoration-color: #2e2e2e}

			.monaco-editor .zone-widget .codicon-error,
			.markers-panel .marker-icon.codicon-error,
			.extensions-viewlet > .extensions .codicon-error,
			.monaco-dialog-box .dialog-message-row .codicon-error {
				color: #e51400;
			}
		

			.monaco-editor .zone-widget .codicon-warning,
			.markers-panel .marker-icon.codicon-warning,
			.extensions-viewlet > .extensions .codicon-warning,
			.extension-editor .codicon-warning,
			.monaco-dialog-box .dialog-message-row .codicon-warning {
				color: #e9a700;
			}
		

			.monaco-editor .zone-widget .codicon-info,
			.markers-panel .marker-icon.codicon-info,
			.extensions-viewlet > .extensions .codicon-info,
			.extension-editor .codicon-info,
			.monaco-dialog-box .dialog-message-row .codicon-info {
				color: #75beff;
			}
		
.monaco-editor .marker-widget a { color: #006ab1; }
.monaco-editor .marker-widget a.code-link span:hover { color: #006ab1; }
.monaco-editor .reference-zone-widget .ref-tree .referenceMatch .highlight { background-color: rgba(234, 92, 0, 0.3); }
.monaco-editor .reference-zone-widget .preview .reference-decoration { background-color: rgba(245, 216, 2, 0.87); }
.monaco-editor .reference-zone-widget .ref-tree { background-color: #f3f3f3; }
.monaco-editor .reference-zone-widget .ref-tree { color: #646465; }
.monaco-editor .reference-zone-widget .ref-tree .reference-file { color: #1e1e1e; }
.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .monaco-list-rows > .monaco-list-row.selected:not(.highlighted) { background-color: rgba(51, 153, 255, 0.2); }
.monaco-editor .reference-zone-widget .ref-tree .monaco-list:focus .monaco-list-rows > .monaco-list-row.selected:not(.highlighted) { color: #6c6c6c !important; }
.monaco-editor .reference-zone-widget .preview .monaco-editor .monaco-editor-background,.monaco-editor .reference-zone-widget .preview .monaco-editor .inputarea.ime-input {	background-color: #f2f8fc;}
.monaco-editor .reference-zone-widget .preview .monaco-editor .margin {	background-color: #f2f8fc;}
.monaco-editor .goto-definition-link { color: #0000ff !important; }
.monaco-editor-hover .hover-contents a.code-link span:hover { color: #006ab1; }
.monaco-editor .hoverHighlight { background-color: rgba(173, 214, 255, 0.15); }
.monaco-editor .monaco-editor-hover { background-color: #f3f3f3; }
.monaco-editor .monaco-editor-hover { border: 1px solid #c8c8c8; }
.monaco-editor .monaco-editor-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-editor-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-editor-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-editor-hover a { color: #006ab1; }
.monaco-editor .monaco-editor-hover { color: #616161; }
.monaco-editor .monaco-editor-hover .hover-row .actions { background-color: #e7e7e7; }
.monaco-editor .monaco-editor-hover code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor.vs .valueSetReplacement { outline: solid 2px #b9b9b9; }
.monaco-editor .tokens-inspect-widget { border: 1px solid #c8c8c8; }
.monaco-editor .tokens-inspect-widget .tokens-inspect-separator { background-color: #c8c8c8; }
.monaco-editor .tokens-inspect-widget { background-color: #f3f3f3; }
.monaco-editor .tokens-inspect-widget { color: #616161; }
.monaco-editor .detected-link-active { color: #0000ff !important; }
.monaco-editor .parameter-hints-widget { border: 1px solid #c8c8c8; }
.monaco-editor .parameter-hints-widget.multiple .body { border-left: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .parameter-hints-widget .signature.has-docs { border-bottom: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .parameter-hints-widget { background-color: #f3f3f3; }
.monaco-editor .parameter-hints-widget a { color: #006ab1; }
.monaco-editor .parameter-hints-widget { color: #616161; }
.monaco-editor .parameter-hints-widget code { background-color: rgba(220, 220, 220, 0.4); }
.codicon-symbol-array { color: #616161 !important; }
.codicon-symbol-boolean { color: #616161 !important; }
.codicon-symbol-class { color: #d67e00 !important; }
.codicon-symbol-method { color: #652d90 !important; }
.codicon-symbol-color { color: #616161 !important; }
.codicon-symbol-constant { color: #616161 !important; }
.codicon-symbol-constructor { color: #652d90 !important; }

			.codicon-symbol-value,.codicon-symbol-enum { color: #d67e00 !important; }
.codicon-symbol-enum-member { color: #007acc !important; }
.codicon-symbol-event { color: #d67e00 !important; }
.codicon-symbol-field { color: #007acc !important; }
.codicon-symbol-file { color: #616161 !important; }
.codicon-symbol-folder { color: #616161 !important; }
.codicon-symbol-function { color: #652d90 !important; }
.codicon-symbol-interface { color: #007acc !important; }
.codicon-symbol-key { color: #616161 !important; }
.codicon-symbol-keyword { color: #616161 !important; }
.codicon-symbol-module { color: #616161 !important; }
.codicon-symbol-namespace { color: #616161 !important; }
.codicon-symbol-null { color: #616161 !important; }
.codicon-symbol-number { color: #616161 !important; }
.codicon-symbol-object { color: #616161 !important; }
.codicon-symbol-operator { color: #616161 !important; }
.codicon-symbol-package { color: #616161 !important; }
.codicon-symbol-property { color: #616161 !important; }
.codicon-symbol-reference { color: #616161 !important; }
.codicon-symbol-snippet { color: #616161 !important; }
.codicon-symbol-string { color: #616161 !important; }
.codicon-symbol-struct { color: #616161 !important; }
.codicon-symbol-text { color: #616161 !important; }
.codicon-symbol-type-parameter { color: #616161 !important; }
.codicon-symbol-unit { color: #616161 !important; }
.codicon-symbol-variable { color: #007acc !important; }
.monaco-editor .snippet-placeholder { background-color: rgba(10, 50, 100, 0.2); outline-color: transparent; }
.monaco-editor .finish-snippet-placeholder { background-color: transparent; outline-color: rgba(10, 50, 100, 0.5); }
.monaco-editor .suggest-widget .monaco-list .monaco-list-row .monaco-highlighted-label .highlight { color: #0066bf; }
.monaco-editor .suggest-widget { color: #2e2e2e; }
.monaco-editor .suggest-widget a { color: #006ab1; }
.monaco-editor .suggest-widget code { background-color: rgba(220, 220, 220, 0.4); }
.monaco-editor .focused .selectionHighlight { background-color: rgba(213, 235, 252, 0.6); }
.monaco-editor .selectionHighlight { background-color: rgba(213, 235, 252, 0.3); }
.monaco-editor .wordHighlight { background-color: rgba(87, 87, 87, 0.25); }
.monaco-editor .wordHighlightStrong { background-color: rgba(14, 99, 156, 0.25); }
.monaco-diff-editor .diff-review-line-number { color: #cccccc; }
.monaco-diff-editor .diff-review-shadow { box-shadow: #dddddd 0 -6px 6px -6px inset; }
.monaco-editor .line-insert, .monaco-editor .char-insert { background-color: rgba(160, 245, 180, 0.13); }
.monaco-diff-editor .line-insert, .monaco-diff-editor .char-insert { background-color: rgba(160, 245, 180, 0.13); }
.monaco-editor .inline-added-margin-view-zone { background-color: rgba(160, 245, 180, 0.13); }
.monaco-editor .line-delete, .monaco-editor .char-delete { background-color: rgba(249, 215, 220, 0.13); }
.monaco-diff-editor .line-delete, .monaco-diff-editor .char-delete { background-color: rgba(249, 215, 220, 0.13); }
.monaco-editor .inline-deleted-margin-view-zone { background-color: rgba(249, 215, 220, 0.13); }
.monaco-diff-editor.side-by-side .editor.modified { box-shadow: -6px 0 5px -5px #dddddd; }

.mtk1 { color: #2e2e2e; }
.mtk2 { color: #ffffff; }
.mtk3 { color: #008080; }
.mtk4 { color: #dd1144; }
.mtk5 { color: #0086b3; }
.mtk6 { color: #aa0000; }
.mtk7 { color: #009999; }
.mtk8 { color: #999988; }
.mtk9 { color: #999999; }
.mtk10 { color: #800080; }
.mtk11 { color: #990073; }
.mtk12 { color: #666666; }
.mtk13 { color: #000080; }
.mtk14 { color: #445588; }
.mtk15 { color: #e3d2d2; }
.mtk16 { color: #863b00; }
.mtk17 { color: #000000; }
.mtk18 { color: #ffdddd; }
.mtk19 { color: #ddffdd; }
.mtk20 { color: #808080; }
.mtk21 { color: #eaf2f5; }
.mtk22 { color: #4183c4; }
.mtk23 { color: #800000; }
.mtk24 { color: #e00000; }
.mtk25 { color: #3030c0; }
.mtk26 { color: #009926; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }</style><style type="text/css" media="screen">
		.monaco-editor .codelens-decoration.ee1f61 { height: 21px; line-height: 19px; font-size: 13px; padding-right: 6px;}
		.monaco-editor .codelens-decoration.ee1f61 > a > .codicon { line-height: 19px; font-size: 13px; }
		</style></head>

<body class="ui-indigo tab-width-8 gl-browser-firefox gl-platform-linux page-initialised" data-find-file="/hos47096/hsp-ss20-schildgen-saas/-/find_file/master" data-namespace-id="1866" data-page="projects:blob:edit" data-page-type-id="master/src/notes/oneNote/msGraphAPI.py" data-project="hsp-ss20-schildgen-saas" data-project-id="4437">

<script>
//<![CDATA[
gl = window.gl || {};
gl.client = {"isFirefox":true,"isLinux":true};


//]]>
</script>


<header class="navbar navbar-gitlab navbar-expand-sm js-navbar" data-qa-selector="navbar">
<a class="sr-only gl-accessibility" href="#content-body" tabindex="1">Skip to content</a>
<div class="container-fluid">
<div class="header-content">
<div class="title-container">
<h1 class="title">
<span class="gl-sr-only">GitLab</span>
<a title="Dashboard" id="logo" href="https://gitlab.oth-regensburg.de/"><svg width="24" height="24" class="tanuki-logo" viewBox="0 0 36 36">
  <path class="tanuki-shape tanuki-left-ear" fill="#e24329" d="M2 14l9.38 9v-9l-4-12.28c-.205-.632-1.176-.632-1.38 0z"></path>
  <path class="tanuki-shape tanuki-right-ear" fill="#e24329" d="M34 14l-9.38 9v-9l4-12.28c.205-.632 1.176-.632 1.38 0z"></path>
  <path class="tanuki-shape tanuki-nose" fill="#e24329" d="M18,34.38 3,14 33,14 Z"></path>
  <path class="tanuki-shape tanuki-left-eye" fill="#fc6d26" d="M18,34.38 11.38,14 2,14 6,25Z"></path>
  <path class="tanuki-shape tanuki-right-eye" fill="#fc6d26" d="M18,34.38 24.62,14 34,14 30,25Z"></path>
  <path class="tanuki-shape tanuki-left-cheek" fill="#fca326" d="M2 14L.1 20.16c-.18.565 0 1.2.5 1.56l17.42 12.66z"></path>
  <path class="tanuki-shape tanuki-right-cheek" fill="#fca326" d="M34 14l1.9 6.16c.18.565 0 1.2-.5 1.56L18 34.38z"></path>
</svg>

<span class="logo-text d-none d-lg-block gl-ml-3">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 617 169"><path d="M315.26 2.97h-21.8l.1 162.5h88.3v-20.1h-66.5l-.1-142.4M465.89 136.95c-5.5 5.7-14.6 11.4-27 11.4-16.6 0-23.3-8.2-23.3-18.9 0-16.1 11.2-23.8 35-23.8 4.5 0 11.7.5 15.4 1.2v30.1h-.1m-22.6-98.5c-17.6 0-33.8 6.2-46.4 16.7l7.7 13.4c8.9-5.2 19.8-10.4 35.5-10.4 17.9 0 25.8 9.2 25.8 24.6v7.9c-3.5-.7-10.7-1.2-15.1-1.2-38.2 0-57.6 13.4-57.6 41.4 0 25.1 15.4 37.7 38.7 37.7 15.7 0 30.8-7.2 36-18.9l4 15.9h15.4v-83.2c-.1-26.3-11.5-43.9-44-43.9M557.63 149.1c-8.2 0-15.4-1-20.8-3.5V70.5c7.4-6.2 16.6-10.7 28.3-10.7 21.1 0 29.2 14.9 29.2 39 0 34.2-13.1 50.3-36.7 50.3m9.2-110.6c-19.5 0-30 13.3-30 13.3v-21l-.1-27.8h-21.3l.1 158.5c10.7 4.5 25.3 6.9 41.2 6.9 40.7 0 60.3-26 60.3-70.9-.1-35.5-18.2-59-50.2-59M77.9 20.6c19.3 0 31.8 6.4 39.9 12.9l9.4-16.3C114.5 6 97.3 0 78.9 0 32.5 0 0 28.3 0 85.4c0 59.8 35.1 83.1 75.2 83.1 20.1 0 37.2-4.7 48.4-9.4l-.5-63.9V75.1H63.6v20.1h38l.5 48.5c-5 2.5-13.6 4.5-25.3 4.5-32.2 0-53.8-20.3-53.8-63-.1-43.5 22.2-64.6 54.9-64.6M231.43 2.95h-21.3l.1 27.3v94.3c0 26.3 11.4 43.9 43.9 43.9 4.5 0 8.9-.4 13.1-1.2v-19.1c-3.1.5-6.4.7-9.9.7-17.9 0-25.8-9.2-25.8-24.6v-65h35.7v-17.8h-35.7l-.1-38.5M155.96 165.47h21.3v-124h-21.3v124M155.96 24.37h21.3V3.07h-21.3v21.3"></path></svg>

</span>
</a></h1>
<ul class="list-unstyled navbar-sub-nav">
<li id="nav-projects-dropdown" class="home dropdown header-projects qa-projects-dropdown" data-track-label="projects_dropdown" data-track-event="click_dropdown" data-track-value=""><button class="btn" data-toggle="dropdown" type="button">
Projects
<svg class="s16 caret-down" data-testid="angle-down-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#angle-down"></use></svg>
</button>
<div class="dropdown-menu frequent-items-dropdown-menu">
<div class="frequent-items-dropdown-container">
<div class="frequent-items-dropdown-sidebar qa-projects-dropdown-sidebar">
<ul>
<li class=""><a class="qa-your-projects-link" href="https://gitlab.oth-regensburg.de/dashboard/projects">Your projects
</a></li><li class=""><a href="https://gitlab.oth-regensburg.de/dashboard/projects/starred">Starred projects
</a></li><li class=""><a href="https://gitlab.oth-regensburg.de/explore">Explore projects
</a></li></ul>
</div>
<div class="frequent-items-dropdown-content">
<div data-project-id="4437" data-project-name="HSP-SS20-Schildgen-SaaS" data-project-namespace="Simon1 Hofmeister / HSP-SS20-Schildgen-SaaS" data-project-web-url="/hos47096/hsp-ss20-schildgen-saas" data-user-name="hos47096" id="js-projects-dropdown"></div>
</div>
</div>

</div>
</li><li id="nav-groups-dropdown" class="d-none d-md-block home dropdown header-groups qa-groups-dropdown" data-track-label="groups_dropdown" data-track-event="click_dropdown" data-track-value=""><button class="btn" data-toggle="dropdown" type="button">
Groups
<svg class="s16 caret-down" data-testid="angle-down-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#angle-down"></use></svg>
</button>
<div class="dropdown-menu frequent-items-dropdown-menu">
<div class="frequent-items-dropdown-container">
<div class="frequent-items-dropdown-sidebar qa-groups-dropdown-sidebar">
<ul>
<li class=""><a class="qa-your-groups-link" href="https://gitlab.oth-regensburg.de/dashboard/groups">Your groups
</a></li><li class=""><a href="https://gitlab.oth-regensburg.de/explore/groups">Explore groups
</a></li></ul>
</div>
<div class="frequent-items-dropdown-content">
<div data-user-name="hos47096" id="js-groups-dropdown"></div>
</div>
</div>

</div>
</li><li class="header-more dropdown">
<a data-qa-selector="more_dropdown" data-toggle="dropdown" href="#">
More
<svg class="s16 caret-down" data-testid="angle-down-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#angle-down"></use></svg>
</a>
<div class="dropdown-menu">
<ul>
<li class="d-md-none">
<a class="dashboard-shortcuts-groups" data-qa-selector="groups_link" href="https://gitlab.oth-regensburg.de/dashboard/groups">Groups
</a></li>
<li class=""><a class="dashboard-shortcuts-activity" data-qa-selector="activity_link" href="https://gitlab.oth-regensburg.de/dashboard/activity">Activity
</a></li><li class=""><a class="dashboard-shortcuts-milestones" data-qa-selector="milestones_link" href="https://gitlab.oth-regensburg.de/dashboard/milestones">Milestones
</a></li><li class=""><a class="dashboard-shortcuts-snippets" data-qa-selector="snippets_link" href="https://gitlab.oth-regensburg.de/dashboard/snippets">Snippets
</a></li><li class=""><a class="d-xl-none" href="https://gitlab.oth-regensburg.de/-/analytics">Analytics
</a></li>
<li class="dropdown">

</li>
</ul>
</div>
</li>
<li class="d-none d-xl-block"><a class="chart-icon" title="Analytics" aria-label="Analytics" data-toggle="tooltip" data-placement="bottom" data-container="body" href="https://gitlab.oth-regensburg.de/-/instance_statistics"><svg class="s18" data-testid="chart-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#chart"></use></svg>
</a></li>
<li class="hidden">
<a class="dashboard-shortcuts-projects" href="https://gitlab.oth-regensburg.de/dashboard/projects">Projects
</a></li>

</ul>

</div>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li class="header-new dropdown" data-track-event="click_dropdown" data-track-label="new_dropdown" data-track-value="">
<a class="header-new-dropdown-toggle has-tooltip qa-new-menu-toggle" id="js-onboarding-new-project-link" title="New..." ref="tooltip" aria-label="New..." data-toggle="dropdown" data-placement="bottom" data-container="body" data-display="static" href="https://gitlab.oth-regensburg.de/projects/new"><svg class="s16" data-testid="plus-square-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#plus-square"></use></svg>
<svg class="s16 caret-down" data-testid="angle-down-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#angle-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="dropdown-bold-header">
This project
</li>
<li><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/issues/new">New issue</a></li>
<li><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/merge_requests/new">New merge request</a></li>
<li><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/snippets/new">New snippet</a></li>
<li class="divider"></li>
<li class="dropdown-bold-header">GitLab</li>
<li><a class="qa-global-new-project-link" href="https://gitlab.oth-regensburg.de/projects/new">New project</a></li>
<li><a class="qa-global-new-snippet-link" href="https://gitlab.oth-regensburg.de/-/snippets/new">New snippet</a></li>
</ul>
</div>
</li>

<li class="nav-item d-none d-lg-block m-auto">
<div class="search search-form" data-track-event="activate_form_input" data-track-label="navbar_search" data-track-value="">
<form class="form-inline" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="✓"><div class="search-input-container">
<div class="search-input-wrap">
<div class="dropdown" data-url="/search/autocomplete">
<input type="search" name="search" id="search" placeholder="Search or jump to…" class="search-input dropdown-menu-toggle no-outline js-search-dashboard-options js-autocomplete-disabled" spellcheck="false" tabindex="1" autocomplete="off" data-issues-path="/dashboard/issues" data-mr-path="/dashboard/merge_requests" data-qa-selector="search_term_field" aria-label="Search or jump to…">
<button class="hidden js-dropdown-search-toggle" data-toggle="dropdown" type="button"></button>
<div class="dropdown-menu dropdown-select js-dashboard-search-options">
<div class="dropdown-content"><ul>
<li class="dropdown-menu-empty-item">
<a>
Loading...
</a>
</li>
</ul>
</div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div>
</div>
<svg class="s16 search-icon" data-testid="search-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#search"></use></svg>
<svg class="s16 clear-icon js-clear-input" data-testid="close-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#close"></use></svg>
</div>
</div>
</div>
<input type="hidden" name="group_id" id="group_id" value="" class="js-search-group-options">
<input type="hidden" name="project_id" id="search_project_id" value="4437" class="js-search-project-options" data-project-path="hsp-ss20-schildgen-saas" data-name="HSP-SS20-Schildgen-SaaS" data-issues-path="/hos47096/hsp-ss20-schildgen-saas/-/issues" data-mr-path="/hos47096/hsp-ss20-schildgen-saas/-/merge_requests" data-issues-disabled="false">
<input type="hidden" name="scope" id="scope">
<input type="hidden" name="search_code" id="search_code" value="true">
<input type="hidden" name="snippets" id="snippets" value="false">
<input type="hidden" name="repository_ref" id="repository_ref" value="master">
<input type="hidden" name="nav_source" id="nav_source" value="navbar">
<div class="search-autocomplete-opts hide" data-autocomplete-path="/search/autocomplete" data-autocomplete-project-id="4437" data-autocomplete-project-ref="master"></div>
</form></div>

</li>
<li class="nav-item d-inline-block d-lg-none">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="https://gitlab.oth-regensburg.de/search?project_id=4437"><svg class="s16" data-testid="search-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#search"></use></svg>
</a></li>
<li class="user-counter"><a title="Issues" class="dashboard-shortcuts-issues" aria-label="Issues" data-qa-selector="issues_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-event="click_issues_link" data-track-property="navigation" data-container="body" href="https://gitlab.oth-regensburg.de/dashboard/issues?assignee_username=hos47096"><svg class="s16" data-testid="issues-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#issues"></use></svg>
<span class="badge badge-pill green-badge hidden issues-count">
0
</span>
</a></li><li class="user-counter"><a title="Merge requests" class="dashboard-shortcuts-merge_requests" aria-label="Merge requests" data-qa-selector="merge_requests_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-event="click_merge_link" data-track-property="navigation" data-container="body" href="https://gitlab.oth-regensburg.de/dashboard/merge_requests?assignee_username=hos47096"><svg class="s16" data-testid="git-merge-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#git-merge"></use></svg>
<span class="badge badge-pill hidden merge-requests-count">
0
</span>
</a></li><li class="user-counter"><a title="To-Do List" aria-label="To-Do List" class="shortcuts-todos" data-qa-selector="todos_shortcut_button" data-toggle="tooltip" data-placement="bottom" data-track-label="main_navigation" data-track-event="click_to_do_link" data-track-property="navigation" data-container="body" href="https://gitlab.oth-regensburg.de/dashboard/todos"><svg class="s16" data-testid="todo-done-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#todo-done"></use></svg>
<span class="badge badge-pill hidden todos-count">
0
</span>
</a></li><li class="nav-item header-help dropdown d-none d-md-block">
<a class="header-help-dropdown-toggle" data-toggle="dropdown" href="https://gitlab.oth-regensburg.de/help"><span class="gl-sr-only">
Help
</span>
<svg class="s16" data-testid="question-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#question"></use></svg>
<svg class="s16 caret-down" data-testid="angle-down-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#angle-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>

<li>
<a href="https://gitlab.oth-regensburg.de/help">Help</a>
</li>
<li>
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li>
<button class="js-shortcuts-modal-trigger" type="button">
Keyboard shortcuts
<span aria-hidden="" class="text-secondary float-right">?</span>
</button>
</li>
<li class="divider"></li>
<li>
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li>

</li>

</ul>

</div>
</li>
<li class="dropdown header-user js-nav-user-dropdown nav-item" data-qa-selector="user_menu" data-track-event="click_dropdown" data-track-label="profile_dropdown" data-track-value="">
<a class="header-user-dropdown-toggle" data-toggle="dropdown" href="https://gitlab.oth-regensburg.de/hos47096"><img class="header-user-avatar qa-user-avatar js-lazy-loaded qa-js-lazy-loaded" alt="Simon1 Hofmeister" src="msGraphAPI_files/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c4.png" loading="lazy" width="23" height="23">

<svg class="s16 caret-down" data-testid="angle-down-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#angle-down"></use></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li class="current-user">
<div class="user-name bold">
Simon1 Hofmeister
</div>
@hos47096
</li>
<li class="divider"></li>
<li>
<button type="button" class="btn menu-item">Set status</button>
</li>
<li>
<a class="profile-link" data-user="hos47096" href="https://gitlab.oth-regensburg.de/hos47096">Profile</a>
</li>
<li>
<a data-qa-selector="settings_link" href="https://gitlab.oth-regensburg.de/profile">Settings</a>
</li>


<li class="divider d-md-none"></li>
<li class="d-md-none">
<a href="https://gitlab.oth-regensburg.de/help">Help</a>
</li>
<li class="d-md-none">
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li class="d-md-none">
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li class="d-md-none">

</li>

<li class="divider"></li>
<li>
<a class="sign-out-link" data-qa-selector="sign_out_link" rel="nofollow" data-method="post" href="https://gitlab.oth-regensburg.de/users/sign_out">Sign out</a>
</li>
</ul>

</div>
</li>
</ul>
</div>
<button class="navbar-toggler d-block d-sm-none" type="button">
<span class="sr-only">Toggle navigation</span>
<svg class="s12 more-icon js-navbar-toggle-right" data-testid="ellipsis_h-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#ellipsis_h"></use></svg>
<svg class="s12 close-icon js-navbar-toggle-left" data-testid="close-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#close"></use></svg>
</button>
</div>
</div>
</header>
<!---->

<div class="layout-page page-with-contextual-sidebar">
<div class="nav-sidebar js-sidebar-collapsed">
<div class="nav-sidebar-inner-scroll" style="overflow-y: scroll;">
<div class="context-header">
<a title="HSP-SS20-Schildgen-SaaS" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas"><div class="avatar-container rect-avatar s40 project-avatar">
<div class="avatar s40 avatar-tile identicon bg7">H</div>
</div>
<div class="sidebar-context-title">
HSP-SS20-Schildgen-SaaS
</div>
</a></div>
<ul class="sidebar-top-level-items qa-project-sidebar">
<li class="home"><a class="shortcuts-project rspec-project-link" data-qa-selector="project_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas"><div class="nav-icon-container">
<svg class="s16" data-testid="home-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#home"></use></svg>
</div>
<span class="nav-item-name">
Project overview
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas"><strong class="fly-out-top-item-name">
Project overview
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Project details" class="shortcuts-project" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas"><span>Details</span>
</a></li><li class=""><a title="Activity" class="shortcuts-project-activity" data-qa-selector="activity_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/activity"><span>Activity</span>
</a></li><li class=""><a title="Releases" class="shortcuts-project-releases" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/releases"><span>Releases</span>
</a></li></ul>
</li><li class="active"><a class="shortcuts-tree" data-qa-selector="repository_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/tree/master"><div class="nav-icon-container">
<svg class="s16" data-testid="doc-text-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#doc-text"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-repo-link">
Repository
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/tree/master"><strong class="fly-out-top-item-name">
Repository
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class="active"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/tree/master">Files
</a></li><li class=""><a id="js-onboarding-commits-link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/commits/master">Commits
</a></li><li class=""><a data-qa-selector="branches_link" id="js-onboarding-branches-link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/branches">Branches
</a></li><li class=""><a data-qa-selector="tags_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/tags">Tags
</a></li><li class=""><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/graphs/master">Contributors
</a></li><li class=""><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/network/master">Graph
</a></li><li class=""><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/compare?from=master&amp;to=master">Compare
</a></li>
</ul>
</li><li class=""><a class="shortcuts-issues qa-issues-item" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/issues"><div class="nav-icon-container">
<svg class="s16" data-testid="issues-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#issues"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-issues-link">
Issues
</span>
<span class="badge badge-pill count issue_counter">
0
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/issues"><strong class="fly-out-top-item-name">
Issues
</strong>
<span class="badge badge-pill count issue_counter fly-out-badge">
0
</span>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Issues" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/issues"><span>
List
</span>
</a></li><li class=""><a title="Boards" data-qa-selector="issue_boards_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/boards"><span>
Boards
</span>
</a></li><li class=""><a title="Labels" class="qa-labels-link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/labels"><span>
Labels
</span>
</a></li><li class=""><a title="Service Desk" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/issues/service_desk">Service Desk
</a></li>
<li class=""><a title="Milestones" class="qa-milestones-link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/milestones"><span>
Milestones
</span>
</a></li>
</ul>
</li><li class=""><a class="shortcuts-merge_requests" data-qa-selector="merge_requests_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/merge_requests"><div class="nav-icon-container">
<svg class="s16" data-testid="git-merge-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#git-merge"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-mr-link">
Merge Requests
</span>
<span class="badge badge-pill count merge_counter js-merge-counter">
0
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/merge_requests"><strong class="fly-out-top-item-name">
Merge Requests
</strong>
<span class="badge badge-pill count merge_counter js-merge-counter fly-out-badge">
0
</span>
</a></li></ul>
</li>
<li class=""><a class="shortcuts-pipelines qa-link-pipelines rspec-link-pipelines" data-qa-selector="ci_cd_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/pipelines"><div class="nav-icon-container">
<svg class="s16" data-testid="rocket-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#rocket"></use></svg>
</div>
<span class="nav-item-name" id="js-onboarding-pipelines-link">
CI / CD
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/pipelines"><strong class="fly-out-top-item-name">
CI / CD
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Pipelines" class="shortcuts-pipelines" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/pipelines"><span>
Pipelines
</span>
</a></li><li class=""><a title="Jobs" class="shortcuts-builds" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/jobs"><span>
Jobs
</span>
</a></li><li class=""><a title="Schedules" class="shortcuts-builds" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/pipeline_schedules"><span>
Schedules
</span>
</a></li></ul>
</li>
<li class=""><a class="shortcuts-operations" data-qa-selector="operations_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/environments/metrics"><div class="nav-icon-container">
<svg class="s16" data-testid="cloud-gear-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#cloud-gear"></use></svg>
</div>
<span class="nav-item-name">
Operations
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/environments/metrics"><strong class="fly-out-top-item-name">
Operations
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Metrics" class="shortcuts-metrics" data-qa-selector="operations_metrics_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/metrics"><span>
Metrics
</span>
</a></li><li class=""><a title="Alerts" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/alert_management"><span>
Alerts
</span>
</a></li><li class=""><a title="Incidents" data-qa-selector="operations_incidents_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/incidents"><span>
Incidents
</span>
</a></li>
<li class=""><a title="Environments" class="shortcuts-environments qa-operations-environments-link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/environments"><span>
Environments
</span>
</a></li><li class=""><a title="Error Tracking" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/error_tracking"><span>
Error Tracking
</span>
</a></li><li class=""><a title="Serverless" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/serverless/functions"><span>
Serverless
</span>
</a></li><li class=""><a title="Logs" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/logs"><span>
Logs
</span>
</a></li><li class=""><a title="Kubernetes" class="shortcuts-kubernetes" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/clusters"><span>
Kubernetes
</span>
</a></li>
</ul>
</li><li class=""><a data-qa-selector="packages_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/packages"><div class="nav-icon-container">
<svg class="s16" data-testid="package-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#package"></use></svg>
</div>
<span class="nav-item-name">
Packages &amp; Registries
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/packages"><strong class="fly-out-top-item-name">
Packages &amp; Registries
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="Package Registry" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/packages"><span>Package Registry</span>
</a></li></ul>
</li>
<li class=""><a data-qa-selector="analytics_anchor" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/value_stream_analytics"><div class="nav-icon-container">
<svg class="s16" data-testid="chart-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#chart"></use></svg>
</div>
<span class="nav-item-name" data-qa-selector="analytics_link">
Analytics
</span>
</a><ul class="sidebar-sub-level-items" data-qa-selector="analytics_sidebar_submenu">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/value_stream_analytics"><strong class="fly-out-top-item-name">
Analytics
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="CI / CD" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/pipelines/charts"><span>CI / CD</span>
</a></li><li class=""><a class="shortcuts-repository-charts" title="Repository" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/graphs/master/charts"><span>Repository</span>
</a></li><li class=""><a class="shortcuts-project-cycle-analytics" title="Value Stream" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/value_stream_analytics"><span>Value Stream</span>
</a></li></ul>
</li>
<li class=""><a class="shortcuts-wiki" data-qa-selector="wiki_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/wikis/home"><div class="nav-icon-container">
<svg class="s16" data-testid="book-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#book"></use></svg>
</div>
<span class="nav-item-name">
Wiki
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/wikis/home"><strong class="fly-out-top-item-name">
Wiki
</strong>
</a></li></ul>
</li>
<li class=""><a class="shortcuts-snippets" data-qa-selector="snippets_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/snippets"><div class="nav-icon-container">
<svg class="s16" data-testid="snippet-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#snippet"></use></svg>
</div>
<span class="nav-item-name">
Snippets
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/snippets"><strong class="fly-out-top-item-name">
Snippets
</strong>
</a></li></ul>
</li><li class=""><a title="Members" class="qa-members-link" id="js-onboarding-members-link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/project_members"><div class="nav-icon-container">
<svg class="s16" data-testid="users-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#users"></use></svg>
</div>
<span class="nav-item-name">
Members
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/project_members"><strong class="fly-out-top-item-name">
Members
</strong>
</a></li></ul>
</li><li class=""><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/edit"><div class="nav-icon-container">
<svg class="s16" data-testid="settings-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#settings"></use></svg>
</div>
<span class="nav-item-name qa-settings-item" id="js-onboarding-settings-link">
Settings
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/edit"><strong class="fly-out-top-item-name">
Settings
</strong>
</a></li><li class="divider fly-out-top-item"></li>
<li class=""><a title="General" class="qa-general-settings-link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/edit"><span>
General
</span>
</a></li><li class=""><a title="Integrations" data-qa-selector="integrations_settings_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/settings/integrations"><span>
Integrations
</span>
</a></li><li class=""><a title="Webhooks" data-qa-selector="webhooks_settings_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/hooks"><span>
Webhooks
</span>
</a></li><li class=""><a title="Access Tokens" data-qa-selector="access_tokens_settings_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/settings/access_tokens"><span>
Access Tokens
</span>
</a></li><li class=""><a title="Repository" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/settings/repository"><span>
Repository
</span>
</a></li><li class=""><a title="CI / CD" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/settings/ci_cd"><span>
CI / CD
</span>
</a></li><li class=""><a title="Operations" data-qa-selector="operations_settings_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/settings/operations">Operations
</a></li><li class=""><a title="Audit Events" data-qa-selector="audit_events_settings_link" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/audit_events">Audit Events
</a></li>
</ul>
</li><a class="toggle-sidebar-button js-toggle-sidebar qa-toggle-sidebar rspec-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg class="s16 icon-chevron-double-lg-left" data-testid="chevron-double-lg-left-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#chevron-double-lg-left"></use></svg>
<svg class="s16 icon-chevron-double-lg-right" data-testid="chevron-double-lg-right-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#chevron-double-lg-right"></use></svg>
<span class="collapse-text">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg class="s16" data-testid="close-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#close"></use></svg>
<span class="collapse-text">Close sidebar</span>
</button>
<li class="hidden">
<a title="Activity" class="shortcuts-project-activity" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/activity"><span>
Activity
</span>
</a></li>
<li class="hidden">
<a title="Network" class="shortcuts-network" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/network/master">Graph
</a></li>
<li class="hidden">
<a class="shortcuts-new-issue" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a title="Jobs" class="shortcuts-builds" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/jobs">Jobs
</a></li>
<li class="hidden">
<a title="Commits" class="shortcuts-commits" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/commits/master">Commits
</a></li>
<li class="hidden">
<a title="Issue Boards" class="shortcuts-issue-boards" href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/boards">Issue Boards</a>
</li>
</ul>
</div>
</div>

<div class="content-wrapper">
<div class="mobile-overlay"></div>
<div class="alert-wrapper">














<nav class="breadcrumbs container-fluid container-limited" role="navigation">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav"><span class="sr-only">Open sidebar</span>
<svg class="s16" data-testid="hamburger-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#hamburger"></use></svg>
</button><div class="breadcrumbs-links js-title-container" data-qa-selector="breadcrumb_links_content">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a href="https://gitlab.oth-regensburg.de/hos47096">Simon1 Hofmeister</a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#angle-right"></use></svg></li> <li><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas"><span class="breadcrumb-item-text js-breadcrumb-item-text">HSP-SS20-Schildgen-SaaS</span></a><svg class="s8 breadcrumbs-list-angle" data-testid="angle-right-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#angle-right"></use></svg></li>

<li>
<h2 class="breadcrumbs-sub-title"><a href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/edit/master/src/notes/oneNote/msGraphAPI.py">Repository</a></h2>
</li>
</ul>
</div>

</div>
</nav>

<div class="d-flex"></div>
</div>
<div class="container-fluid container-limited ">
<div class="content" id="content-body">
<div class="flash-container flash-container-page sticky">
</div>

<div class="editor-title-row">
<h3 class="page-title blob-edit-page-title">
Edit file
</h3>
</div>
<div class="file-editor">
<ul class="nav-links no-bottom js-edit-mode nav nav-tabs">
<li class="active">
<a href="#editor">Write
</a></li>
<li>
<a data-preview-url="/hos47096/hsp-ss20-schildgen-saas/-/preview/master/src/notes/oneNote/msGraphAPI.py" href="#preview">Preview changes
</a></li>
</ul>
<form class="js-quick-submit js-requires-input js-edit-blob-form" data-assets-prefix="/assets" data-blob-filename="src/notes/oneNote/msGraphAPI.py" data-project-id="4437" data-is-markdown="false" action="/hos47096/hsp-ss20-schildgen-saas/-/update/master/src/notes/oneNote/msGraphAPI.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="_method" value="put"><input type="hidden" name="authenticity_token" value="K1T+VEI/B4gC4kjDr3LoIw3qYF56oU7q+KPQOqDOer3tQ5UhRZlMF799td7f0JA9R4hLPcNtslnHOnrwZ259hw=="><div class="file-holder-bottom-radius file-holder file gl-mb-3">
<div class="js-file-title file-title align-items-center clearfix" data-current-action="edit">
<div class="editor-ref block-truncated has-tooltip" title="master">
<svg class="s12" data-testid="fork-icon"><use xlink:href="/assets/icons-81bca028cfa382a852fa2c8a6dfb4fb2b7467093d38f9fe9a07a519ca785299c.svg#fork"></use></svg>
master
</div>
<span class="float-left gl-mr-3"></span>
<input type="text" name="file_path" id="file_path" value="src/notes/oneNote/msGraphAPI.py" class="form-control new-file-path js-file-path-name-input">
<div class="template-selectors-menu gl-pl-2-deprecated-no-really-do-not-use-me" style="display: none;">
<div class="template-selector-dropdowns-wrap">
<div class="template-type-selector js-template-type-selector-wrap hidden">
<div class="dropdown "><button class="dropdown-menu-toggle js-template-type-selector qa-template-type-dropdown" type="button" data-toggle="dropdown"><span class="dropdown-toggle-text ">Select a template type</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-content "></div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div></div></div>
</div>
<div class="license-selector js-license-selector-wrap js-template-selector-wrap hidden">
<div class="dropdown "><button class="dropdown-menu-toggle js-license-selector qa-license-dropdown" type="button" data-data="{&quot;Other&quot;:[{&quot;name&quot;:&quot;GNU Lesser General Public License v2.1&quot;,&quot;id&quot;:&quot;lgpl-2.1&quot;},{&quot;name&quot;:&quot;GNU Affero General Public License v3.0&quot;,&quot;id&quot;:&quot;agpl-3.0&quot;},{&quot;name&quot;:&quot;GNU Lesser General Public License v3.0&quot;,&quot;id&quot;:&quot;lgpl-3.0&quot;},{&quot;name&quot;:&quot;Mozilla Public License 2.0&quot;,&quot;id&quot;:&quot;mpl-2.0&quot;},{&quot;name&quot;:&quot;BSD 2-clause \&quot;Simplified\&quot; License&quot;,&quot;id&quot;:&quot;bsd-2-clause&quot;},{&quot;name&quot;:&quot;Eclipse Public License 1.0&quot;,&quot;id&quot;:&quot;epl-1.0&quot;},{&quot;name&quot;:&quot;BSD 3-clause \&quot;New\&quot; or \&quot;Revised\&quot; License&quot;,&quot;id&quot;:&quot;bsd-3-clause&quot;},{&quot;name&quot;:&quot;The Unlicense&quot;,&quot;id&quot;:&quot;unlicense&quot;},{&quot;name&quot;:&quot;GNU General Public License v2.0&quot;,&quot;id&quot;:&quot;gpl-2.0&quot;}],&quot;Popular&quot;:[{&quot;name&quot;:&quot;MIT License&quot;,&quot;id&quot;:&quot;mit&quot;},{&quot;name&quot;:&quot;Apache License 2.0&quot;,&quot;id&quot;:&quot;apache-2.0&quot;},{&quot;name&quot;:&quot;GNU General Public License v3.0&quot;,&quot;id&quot;:&quot;gpl-3.0&quot;}]}" data-project="HSP-SS20-Schildgen-SaaS" data-fullname="Simon1 Hofmeister" data-toggle="dropdown"><span class="dropdown-toggle-text ">Apply a template</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-input"><input type="search" id="" class="dropdown-input-field qa-dropdown-input-field" placeholder="Filter" autocomplete="off"><i aria-hidden="true" data-hidden="true" class="fa fa-search dropdown-input-search"></i><i aria-hidden="true" data-hidden="true" role="button" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div><div class="dropdown-content "></div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div></div></div>
</div>
<div class="gitignore-selector js-gitignore-selector-wrap js-template-selector-wrap hidden">
<div class="dropdown "><button class="dropdown-menu-toggle js-gitignore-selector qa-gitignore-dropdown" type="button" data-data="{&quot;Languages&quot;:[{&quot;name&quot;:&quot;Actionscript&quot;,&quot;id&quot;:&quot;Actionscript&quot;},{&quot;name&quot;:&quot;Ada&quot;,&quot;id&quot;:&quot;Ada&quot;},{&quot;name&quot;:&quot;Agda&quot;,&quot;id&quot;:&quot;Agda&quot;},{&quot;name&quot;:&quot;Android&quot;,&quot;id&quot;:&quot;Android&quot;},{&quot;name&quot;:&quot;AppEngine&quot;,&quot;id&quot;:&quot;AppEngine&quot;},{&quot;name&quot;:&quot;AppceleratorTitanium&quot;,&quot;id&quot;:&quot;AppceleratorTitanium&quot;},{&quot;name&quot;:&quot;ArchLinuxPackages&quot;,&quot;id&quot;:&quot;ArchLinuxPackages&quot;},{&quot;name&quot;:&quot;Autotools&quot;,&quot;id&quot;:&quot;Autotools&quot;},{&quot;name&quot;:&quot;C&quot;,&quot;id&quot;:&quot;C&quot;},{&quot;name&quot;:&quot;C++&quot;,&quot;id&quot;:&quot;C++&quot;},{&quot;name&quot;:&quot;CFWheels&quot;,&quot;id&quot;:&quot;CFWheels&quot;},{&quot;name&quot;:&quot;CMake&quot;,&quot;id&quot;:&quot;CMake&quot;},{&quot;name&quot;:&quot;CUDA&quot;,&quot;id&quot;:&quot;CUDA&quot;},{&quot;name&quot;:&quot;CakePHP&quot;,&quot;id&quot;:&quot;CakePHP&quot;},{&quot;name&quot;:&quot;ChefCookbook&quot;,&quot;id&quot;:&quot;ChefCookbook&quot;},{&quot;name&quot;:&quot;Clojure&quot;,&quot;id&quot;:&quot;Clojure&quot;},{&quot;name&quot;:&quot;CodeIgniter&quot;,&quot;id&quot;:&quot;CodeIgniter&quot;},{&quot;name&quot;:&quot;CommonLisp&quot;,&quot;id&quot;:&quot;CommonLisp&quot;},{&quot;name&quot;:&quot;Composer&quot;,&quot;id&quot;:&quot;Composer&quot;},{&quot;name&quot;:&quot;Concrete5&quot;,&quot;id&quot;:&quot;Concrete5&quot;},{&quot;name&quot;:&quot;Coq&quot;,&quot;id&quot;:&quot;Coq&quot;},{&quot;name&quot;:&quot;CraftCMS&quot;,&quot;id&quot;:&quot;CraftCMS&quot;},{&quot;name&quot;:&quot;D&quot;,&quot;id&quot;:&quot;D&quot;},{&quot;name&quot;:&quot;DM&quot;,&quot;id&quot;:&quot;DM&quot;},{&quot;name&quot;:&quot;Dart&quot;,&quot;id&quot;:&quot;Dart&quot;},{&quot;name&quot;:&quot;Delphi&quot;,&quot;id&quot;:&quot;Delphi&quot;},{&quot;name&quot;:&quot;Drupal&quot;,&quot;id&quot;:&quot;Drupal&quot;},{&quot;name&quot;:&quot;EPiServer&quot;,&quot;id&quot;:&quot;EPiServer&quot;},{&quot;name&quot;:&quot;Eagle&quot;,&quot;id&quot;:&quot;Eagle&quot;},{&quot;name&quot;:&quot;Elisp&quot;,&quot;id&quot;:&quot;Elisp&quot;},{&quot;name&quot;:&quot;Elixir&quot;,&quot;id&quot;:&quot;Elixir&quot;},{&quot;name&quot;:&quot;Elm&quot;,&quot;id&quot;:&quot;Elm&quot;},{&quot;name&quot;:&quot;Erlang&quot;,&quot;id&quot;:&quot;Erlang&quot;},{&quot;name&quot;:&quot;ExpressionEngine&quot;,&quot;id&quot;:&quot;ExpressionEngine&quot;},{&quot;name&quot;:&quot;ExtJs&quot;,&quot;id&quot;:&quot;ExtJs&quot;},{&quot;name&quot;:&quot;Fancy&quot;,&quot;id&quot;:&quot;Fancy&quot;},{&quot;name&quot;:&quot;Finale&quot;,&quot;id&quot;:&quot;Finale&quot;},{&quot;name&quot;:&quot;ForceDotCom&quot;,&quot;id&quot;:&quot;ForceDotCom&quot;},{&quot;name&quot;:&quot;Fortran&quot;,&quot;id&quot;:&quot;Fortran&quot;},{&quot;name&quot;:&quot;FuelPHP&quot;,&quot;id&quot;:&quot;FuelPHP&quot;},{&quot;name&quot;:&quot;GWT&quot;,&quot;id&quot;:&quot;GWT&quot;},{&quot;name&quot;:&quot;Gcov&quot;,&quot;id&quot;:&quot;Gcov&quot;},{&quot;name&quot;:&quot;GitBook&quot;,&quot;id&quot;:&quot;GitBook&quot;},{&quot;name&quot;:&quot;Go&quot;,&quot;id&quot;:&quot;Go&quot;},{&quot;name&quot;:&quot;Godot&quot;,&quot;id&quot;:&quot;Godot&quot;},{&quot;name&quot;:&quot;Gradle&quot;,&quot;id&quot;:&quot;Gradle&quot;},{&quot;name&quot;:&quot;Grails&quot;,&quot;id&quot;:&quot;Grails&quot;},{&quot;name&quot;:&quot;Haskell&quot;,&quot;id&quot;:&quot;Haskell&quot;},{&quot;name&quot;:&quot;IGORPro&quot;,&quot;id&quot;:&quot;IGORPro&quot;},{&quot;name&quot;:&quot;Idris&quot;,&quot;id&quot;:&quot;Idris&quot;},{&quot;name&quot;:&quot;Java&quot;,&quot;id&quot;:&quot;Java&quot;},{&quot;name&quot;:&quot;Jboss&quot;,&quot;id&quot;:&quot;Jboss&quot;},{&quot;name&quot;:&quot;Jekyll&quot;,&quot;id&quot;:&quot;Jekyll&quot;},{&quot;name&quot;:&quot;Joomla&quot;,&quot;id&quot;:&quot;Joomla&quot;},{&quot;name&quot;:&quot;Julia&quot;,&quot;id&quot;:&quot;Julia&quot;},{&quot;name&quot;:&quot;KiCad&quot;,&quot;id&quot;:&quot;KiCad&quot;},{&quot;name&quot;:&quot;Kohana&quot;,&quot;id&quot;:&quot;Kohana&quot;},{&quot;name&quot;:&quot;Kotlin&quot;,&quot;id&quot;:&quot;Kotlin&quot;},{&quot;name&quot;:&quot;LabVIEW&quot;,&quot;id&quot;:&quot;LabVIEW&quot;},{&quot;name&quot;:&quot;Laravel&quot;,&quot;id&quot;:&quot;Laravel&quot;},{&quot;name&quot;:&quot;Leiningen&quot;,&quot;id&quot;:&quot;Leiningen&quot;},{&quot;name&quot;:&quot;LemonStand&quot;,&quot;id&quot;:&quot;LemonStand&quot;},{&quot;name&quot;:&quot;Lilypond&quot;,&quot;id&quot;:&quot;Lilypond&quot;},{&quot;name&quot;:&quot;Lithium&quot;,&quot;id&quot;:&quot;Lithium&quot;},{&quot;name&quot;:&quot;Lua&quot;,&quot;id&quot;:&quot;Lua&quot;},{&quot;name&quot;:&quot;Magento&quot;,&quot;id&quot;:&quot;Magento&quot;},{&quot;name&quot;:&quot;Maven&quot;,&quot;id&quot;:&quot;Maven&quot;},{&quot;name&quot;:&quot;Mercury&quot;,&quot;id&quot;:&quot;Mercury&quot;},{&quot;name&quot;:&quot;MetaProgrammingSystem&quot;,&quot;id&quot;:&quot;MetaProgrammingSystem&quot;},{&quot;name&quot;:&quot;Nanoc&quot;,&quot;id&quot;:&quot;Nanoc&quot;},{&quot;name&quot;:&quot;Nim&quot;,&quot;id&quot;:&quot;Nim&quot;},{&quot;name&quot;:&quot;Node&quot;,&quot;id&quot;:&quot;Node&quot;},{&quot;name&quot;:&quot;OCaml&quot;,&quot;id&quot;:&quot;OCaml&quot;},{&quot;name&quot;:&quot;Objective-C&quot;,&quot;id&quot;:&quot;Objective-C&quot;},{&quot;name&quot;:&quot;Opa&quot;,&quot;id&quot;:&quot;Opa&quot;},{&quot;name&quot;:&quot;OpenCart&quot;,&quot;id&quot;:&quot;OpenCart&quot;},{&quot;name&quot;:&quot;OracleForms&quot;,&quot;id&quot;:&quot;OracleForms&quot;},{&quot;name&quot;:&quot;Packer&quot;,&quot;id&quot;:&quot;Packer&quot;},{&quot;name&quot;:&quot;Perl&quot;,&quot;id&quot;:&quot;Perl&quot;},{&quot;name&quot;:&quot;Perl6&quot;,&quot;id&quot;:&quot;Perl6&quot;},{&quot;name&quot;:&quot;Phalcon&quot;,&quot;id&quot;:&quot;Phalcon&quot;},{&quot;name&quot;:&quot;PlayFramework&quot;,&quot;id&quot;:&quot;PlayFramework&quot;},{&quot;name&quot;:&quot;Plone&quot;,&quot;id&quot;:&quot;Plone&quot;},{&quot;name&quot;:&quot;Prestashop&quot;,&quot;id&quot;:&quot;Prestashop&quot;},{&quot;name&quot;:&quot;Processing&quot;,&quot;id&quot;:&quot;Processing&quot;},{&quot;name&quot;:&quot;PureScript&quot;,&quot;id&quot;:&quot;PureScript&quot;},{&quot;name&quot;:&quot;Python&quot;,&quot;id&quot;:&quot;Python&quot;},{&quot;name&quot;:&quot;Qooxdoo&quot;,&quot;id&quot;:&quot;Qooxdoo&quot;},{&quot;name&quot;:&quot;Qt&quot;,&quot;id&quot;:&quot;Qt&quot;},{&quot;name&quot;:&quot;R&quot;,&quot;id&quot;:&quot;R&quot;},{&quot;name&quot;:&quot;ROS&quot;,&quot;id&quot;:&quot;ROS&quot;},{&quot;name&quot;:&quot;Rails&quot;,&quot;id&quot;:&quot;Rails&quot;},{&quot;name&quot;:&quot;RhodesRhomobile&quot;,&quot;id&quot;:&quot;RhodesRhomobile&quot;},{&quot;name&quot;:&quot;Ruby&quot;,&quot;id&quot;:&quot;Ruby&quot;},{&quot;name&quot;:&quot;Rust&quot;,&quot;id&quot;:&quot;Rust&quot;},{&quot;name&quot;:&quot;SCons&quot;,&quot;id&quot;:&quot;SCons&quot;},{&quot;name&quot;:&quot;Sass&quot;,&quot;id&quot;:&quot;Sass&quot;},{&quot;name&quot;:&quot;Scala&quot;,&quot;id&quot;:&quot;Scala&quot;},{&quot;name&quot;:&quot;Scheme&quot;,&quot;id&quot;:&quot;Scheme&quot;},{&quot;name&quot;:&quot;Scrivener&quot;,&quot;id&quot;:&quot;Scrivener&quot;},{&quot;name&quot;:&quot;Sdcc&quot;,&quot;id&quot;:&quot;Sdcc&quot;},{&quot;name&quot;:&quot;SeamGen&quot;,&quot;id&quot;:&quot;SeamGen&quot;},{&quot;name&quot;:&quot;SketchUp&quot;,&quot;id&quot;:&quot;SketchUp&quot;},{&quot;name&quot;:&quot;Smalltalk&quot;,&quot;id&quot;:&quot;Smalltalk&quot;},{&quot;name&quot;:&quot;Stella&quot;,&quot;id&quot;:&quot;Stella&quot;},{&quot;name&quot;:&quot;SugarCRM&quot;,&quot;id&quot;:&quot;SugarCRM&quot;},{&quot;name&quot;:&quot;Swift&quot;,&quot;id&quot;:&quot;Swift&quot;},{&quot;name&quot;:&quot;Symfony&quot;,&quot;id&quot;:&quot;Symfony&quot;},{&quot;name&quot;:&quot;SymphonyCMS&quot;,&quot;id&quot;:&quot;SymphonyCMS&quot;},{&quot;name&quot;:&quot;TeX&quot;,&quot;id&quot;:&quot;TeX&quot;},{&quot;name&quot;:&quot;Terraform&quot;,&quot;id&quot;:&quot;Terraform&quot;},{&quot;name&quot;:&quot;Textpattern&quot;,&quot;id&quot;:&quot;Textpattern&quot;},{&quot;name&quot;:&quot;TurboGears2&quot;,&quot;id&quot;:&quot;TurboGears2&quot;},{&quot;name&quot;:&quot;Typo3&quot;,&quot;id&quot;:&quot;Typo3&quot;},{&quot;name&quot;:&quot;Umbraco&quot;,&quot;id&quot;:&quot;Umbraco&quot;},{&quot;name&quot;:&quot;Unity&quot;,&quot;id&quot;:&quot;Unity&quot;},{&quot;name&quot;:&quot;UnrealEngine&quot;,&quot;id&quot;:&quot;UnrealEngine&quot;},{&quot;name&quot;:&quot;VVVV&quot;,&quot;id&quot;:&quot;VVVV&quot;},{&quot;name&quot;:&quot;VisualStudio&quot;,&quot;id&quot;:&quot;VisualStudio&quot;},{&quot;name&quot;:&quot;Waf&quot;,&quot;id&quot;:&quot;Waf&quot;},{&quot;name&quot;:&quot;WordPress&quot;,&quot;id&quot;:&quot;WordPress&quot;},{&quot;name&quot;:&quot;Xojo&quot;,&quot;id&quot;:&quot;Xojo&quot;},{&quot;name&quot;:&quot;Yeoman&quot;,&quot;id&quot;:&quot;Yeoman&quot;},{&quot;name&quot;:&quot;Yii&quot;,&quot;id&quot;:&quot;Yii&quot;},{&quot;name&quot;:&quot;ZendFramework&quot;,&quot;id&quot;:&quot;ZendFramework&quot;},{&quot;name&quot;:&quot;Zephir&quot;,&quot;id&quot;:&quot;Zephir&quot;}],&quot;Global&quot;:[{&quot;name&quot;:&quot;Anjuta&quot;,&quot;id&quot;:&quot;Anjuta&quot;},{&quot;name&quot;:&quot;Ansible&quot;,&quot;id&quot;:&quot;Ansible&quot;},{&quot;name&quot;:&quot;Archives&quot;,&quot;id&quot;:&quot;Archives&quot;},{&quot;name&quot;:&quot;Backup&quot;,&quot;id&quot;:&quot;Backup&quot;},{&quot;name&quot;:&quot;Bazaar&quot;,&quot;id&quot;:&quot;Bazaar&quot;},{&quot;name&quot;:&quot;BricxCC&quot;,&quot;id&quot;:&quot;BricxCC&quot;},{&quot;name&quot;:&quot;CVS&quot;,&quot;id&quot;:&quot;CVS&quot;},{&quot;name&quot;:&quot;Calabash&quot;,&quot;id&quot;:&quot;Calabash&quot;},{&quot;name&quot;:&quot;Cloud9&quot;,&quot;id&quot;:&quot;Cloud9&quot;},{&quot;name&quot;:&quot;CodeKit&quot;,&quot;id&quot;:&quot;CodeKit&quot;},{&quot;name&quot;:&quot;DartEditor&quot;,&quot;id&quot;:&quot;DartEditor&quot;},{&quot;name&quot;:&quot;Diff&quot;,&quot;id&quot;:&quot;Diff&quot;},{&quot;name&quot;:&quot;Dreamweaver&quot;,&quot;id&quot;:&quot;Dreamweaver&quot;},{&quot;name&quot;:&quot;Dropbox&quot;,&quot;id&quot;:&quot;Dropbox&quot;},{&quot;name&quot;:&quot;Eclipse&quot;,&quot;id&quot;:&quot;Eclipse&quot;},{&quot;name&quot;:&quot;EiffelStudio&quot;,&quot;id&quot;:&quot;EiffelStudio&quot;},{&quot;name&quot;:&quot;Emacs&quot;,&quot;id&quot;:&quot;Emacs&quot;},{&quot;name&quot;:&quot;Ensime&quot;,&quot;id&quot;:&quot;Ensime&quot;},{&quot;name&quot;:&quot;Espresso&quot;,&quot;id&quot;:&quot;Espresso&quot;},{&quot;name&quot;:&quot;FlexBuilder&quot;,&quot;id&quot;:&quot;FlexBuilder&quot;},{&quot;name&quot;:&quot;GPG&quot;,&quot;id&quot;:&quot;GPG&quot;},{&quot;name&quot;:&quot;Images&quot;,&quot;id&quot;:&quot;Images&quot;},{&quot;name&quot;:&quot;JDeveloper&quot;,&quot;id&quot;:&quot;JDeveloper&quot;},{&quot;name&quot;:&quot;JEnv&quot;,&quot;id&quot;:&quot;JEnv&quot;},{&quot;name&quot;:&quot;JetBrains&quot;,&quot;id&quot;:&quot;JetBrains&quot;},{&quot;name&quot;:&quot;KDevelop4&quot;,&quot;id&quot;:&quot;KDevelop4&quot;},{&quot;name&quot;:&quot;Kate&quot;,&quot;id&quot;:&quot;Kate&quot;},{&quot;name&quot;:&quot;Lazarus&quot;,&quot;id&quot;:&quot;Lazarus&quot;},{&quot;name&quot;:&quot;LibreOffice&quot;,&quot;id&quot;:&quot;LibreOffice&quot;},{&quot;name&quot;:&quot;Linux&quot;,&quot;id&quot;:&quot;Linux&quot;},{&quot;name&quot;:&quot;LyX&quot;,&quot;id&quot;:&quot;LyX&quot;},{&quot;name&quot;:&quot;Matlab&quot;,&quot;id&quot;:&quot;Matlab&quot;},{&quot;name&quot;:&quot;Mercurial&quot;,&quot;id&quot;:&quot;Mercurial&quot;},{&quot;name&quot;:&quot;MicrosoftOffice&quot;,&quot;id&quot;:&quot;MicrosoftOffice&quot;},{&quot;name&quot;:&quot;ModelSim&quot;,&quot;id&quot;:&quot;ModelSim&quot;},{&quot;name&quot;:&quot;Momentics&quot;,&quot;id&quot;:&quot;Momentics&quot;},{&quot;name&quot;:&quot;MonoDevelop&quot;,&quot;id&quot;:&quot;MonoDevelop&quot;},{&quot;name&quot;:&quot;NetBeans&quot;,&quot;id&quot;:&quot;NetBeans&quot;},{&quot;name&quot;:&quot;Ninja&quot;,&quot;id&quot;:&quot;Ninja&quot;},{&quot;name&quot;:&quot;NotepadPP&quot;,&quot;id&quot;:&quot;NotepadPP&quot;},{&quot;name&quot;:&quot;Otto&quot;,&quot;id&quot;:&quot;Otto&quot;},{&quot;name&quot;:&quot;PSoCCreator&quot;,&quot;id&quot;:&quot;PSoCCreator&quot;},{&quot;name&quot;:&quot;Patch&quot;,&quot;id&quot;:&quot;Patch&quot;},{&quot;name&quot;:&quot;PuTTY&quot;,&quot;id&quot;:&quot;PuTTY&quot;},{&quot;name&quot;:&quot;Redcar&quot;,&quot;id&quot;:&quot;Redcar&quot;},{&quot;name&quot;:&quot;Redis&quot;,&quot;id&quot;:&quot;Redis&quot;},{&quot;name&quot;:&quot;SBT&quot;,&quot;id&quot;:&quot;SBT&quot;},{&quot;name&quot;:&quot;SVN&quot;,&quot;id&quot;:&quot;SVN&quot;},{&quot;name&quot;:&quot;SlickEdit&quot;,&quot;id&quot;:&quot;SlickEdit&quot;},{&quot;name&quot;:&quot;Stata&quot;,&quot;id&quot;:&quot;Stata&quot;},{&quot;name&quot;:&quot;SublimeText&quot;,&quot;id&quot;:&quot;SublimeText&quot;},{&quot;name&quot;:&quot;SynopsysVCS&quot;,&quot;id&quot;:&quot;SynopsysVCS&quot;},{&quot;name&quot;:&quot;Tags&quot;,&quot;id&quot;:&quot;Tags&quot;},{&quot;name&quot;:&quot;TextMate&quot;,&quot;id&quot;:&quot;TextMate&quot;},{&quot;name&quot;:&quot;TortoiseGit&quot;,&quot;id&quot;:&quot;TortoiseGit&quot;},{&quot;name&quot;:&quot;Vagrant&quot;,&quot;id&quot;:&quot;Vagrant&quot;},{&quot;name&quot;:&quot;Vim&quot;,&quot;id&quot;:&quot;Vim&quot;},{&quot;name&quot;:&quot;VirtualEnv&quot;,&quot;id&quot;:&quot;VirtualEnv&quot;},{&quot;name&quot;:&quot;Virtuoso&quot;,&quot;id&quot;:&quot;Virtuoso&quot;},{&quot;name&quot;:&quot;VisualStudioCode&quot;,&quot;id&quot;:&quot;VisualStudioCode&quot;},{&quot;name&quot;:&quot;WebMethods&quot;,&quot;id&quot;:&quot;WebMethods&quot;},{&quot;name&quot;:&quot;Windows&quot;,&quot;id&quot;:&quot;Windows&quot;},{&quot;name&quot;:&quot;Xcode&quot;,&quot;id&quot;:&quot;Xcode&quot;},{&quot;name&quot;:&quot;XilinxISE&quot;,&quot;id&quot;:&quot;XilinxISE&quot;},{&quot;name&quot;:&quot;macOS&quot;,&quot;id&quot;:&quot;macOS&quot;}]}" data-toggle="dropdown"><span class="dropdown-toggle-text ">Apply a template</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-input"><input type="search" id="" class="dropdown-input-field qa-dropdown-input-field" placeholder="Filter" autocomplete="off"><i aria-hidden="true" data-hidden="true" class="fa fa-search dropdown-input-search"></i><i aria-hidden="true" data-hidden="true" role="button" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div><div class="dropdown-content "></div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div></div></div>
</div>
<div class="metrics-dashboard-selector js-metrics-dashboard-selector-wrap js-template-selector-wrap hidden">
<div class="dropdown "><button class="dropdown-menu-toggle js-metrics-dashboard-selector qa-metrics-dashboard-dropdown" type="button" data-data="{&quot;General&quot;:[{&quot;name&quot;:&quot;Area&quot;,&quot;id&quot;:&quot;Area&quot;},{&quot;name&quot;:&quot;Default&quot;,&quot;id&quot;:&quot;Default&quot;},{&quot;name&quot;:&quot;gauge&quot;,&quot;id&quot;:&quot;gauge&quot;},{&quot;name&quot;:&quot;k8s_area&quot;,&quot;id&quot;:&quot;k8s_area&quot;},{&quot;name&quot;:&quot;k8s_gauge&quot;,&quot;id&quot;:&quot;k8s_gauge&quot;},{&quot;name&quot;:&quot;k8s_single-stat&quot;,&quot;id&quot;:&quot;k8s_single-stat&quot;},{&quot;name&quot;:&quot;single-stat&quot;,&quot;id&quot;:&quot;single-stat&quot;}]}" data-toggle="dropdown"><span class="dropdown-toggle-text ">Apply a template</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-input"><input type="search" id="" class="dropdown-input-field qa-dropdown-input-field" placeholder="Filter" autocomplete="off"><i aria-hidden="true" data-hidden="true" class="fa fa-search dropdown-input-search"></i><i aria-hidden="true" data-hidden="true" role="button" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div><div class="dropdown-content "></div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div></div></div>
</div>
<div class="gitlab-ci-yml-selector js-gitlab-ci-yml-selector-wrap js-template-selector-wrap hidden" id="gitlab-ci-yml-selector">
<div class="dropdown "><button class="dropdown-menu-toggle js-gitlab-ci-yml-selector qa-gitlab-ci-yml-dropdown" type="button" data-data="{&quot;General&quot;:[{&quot;name&quot;:&quot;Android&quot;,&quot;id&quot;:&quot;Android&quot;},{&quot;name&quot;:&quot;Android-Fastlane&quot;,&quot;id&quot;:&quot;Android-Fastlane&quot;},{&quot;name&quot;:&quot;Auto-DevOps&quot;,&quot;id&quot;:&quot;Auto-DevOps&quot;},{&quot;name&quot;:&quot;Bash&quot;,&quot;id&quot;:&quot;Bash&quot;},{&quot;name&quot;:&quot;C++&quot;,&quot;id&quot;:&quot;C++&quot;},{&quot;name&quot;:&quot;Chef&quot;,&quot;id&quot;:&quot;Chef&quot;},{&quot;name&quot;:&quot;Clojure&quot;,&quot;id&quot;:&quot;Clojure&quot;},{&quot;name&quot;:&quot;Code-Quality&quot;,&quot;id&quot;:&quot;Code-Quality&quot;},{&quot;name&quot;:&quot;Composer&quot;,&quot;id&quot;:&quot;Composer&quot;},{&quot;name&quot;:&quot;Crystal&quot;,&quot;id&quot;:&quot;Crystal&quot;},{&quot;name&quot;:&quot;Dart&quot;,&quot;id&quot;:&quot;Dart&quot;},{&quot;name&quot;:&quot;Deploy-ECS&quot;,&quot;id&quot;:&quot;Deploy-ECS&quot;},{&quot;name&quot;:&quot;Django&quot;,&quot;id&quot;:&quot;Django&quot;},{&quot;name&quot;:&quot;Docker&quot;,&quot;id&quot;:&quot;Docker&quot;},{&quot;name&quot;:&quot;Elixir&quot;,&quot;id&quot;:&quot;Elixir&quot;},{&quot;name&quot;:&quot;Go&quot;,&quot;id&quot;:&quot;Go&quot;},{&quot;name&quot;:&quot;Gradle&quot;,&quot;id&quot;:&quot;Gradle&quot;},{&quot;name&quot;:&quot;Grails&quot;,&quot;id&quot;:&quot;Grails&quot;},{&quot;name&quot;:&quot;Julia&quot;,&quot;id&quot;:&quot;Julia&quot;},{&quot;name&quot;:&quot;LaTeX&quot;,&quot;id&quot;:&quot;LaTeX&quot;},{&quot;name&quot;:&quot;Laravel&quot;,&quot;id&quot;:&quot;Laravel&quot;},{&quot;name&quot;:&quot;Managed-Cluster-Applications&quot;,&quot;id&quot;:&quot;Managed-Cluster-Applications&quot;},{&quot;name&quot;:&quot;Maven&quot;,&quot;id&quot;:&quot;Maven&quot;},{&quot;name&quot;:&quot;Mono&quot;,&quot;id&quot;:&quot;Mono&quot;},{&quot;name&quot;:&quot;Nodejs&quot;,&quot;id&quot;:&quot;Nodejs&quot;},{&quot;name&quot;:&quot;OpenShift&quot;,&quot;id&quot;:&quot;OpenShift&quot;},{&quot;name&quot;:&quot;PHP&quot;,&quot;id&quot;:&quot;PHP&quot;},{&quot;name&quot;:&quot;Packer&quot;,&quot;id&quot;:&quot;Packer&quot;},{&quot;name&quot;:&quot;Python&quot;,&quot;id&quot;:&quot;Python&quot;},{&quot;name&quot;:&quot;Ruby&quot;,&quot;id&quot;:&quot;Ruby&quot;},{&quot;name&quot;:&quot;Rust&quot;,&quot;id&quot;:&quot;Rust&quot;},{&quot;name&quot;:&quot;Scala&quot;,&quot;id&quot;:&quot;Scala&quot;},{&quot;name&quot;:&quot;Serverless&quot;,&quot;id&quot;:&quot;Serverless&quot;},{&quot;name&quot;:&quot;Swift&quot;,&quot;id&quot;:&quot;Swift&quot;},{&quot;name&quot;:&quot;Terraform&quot;,&quot;id&quot;:&quot;Terraform&quot;},{&quot;name&quot;:&quot;dotNET&quot;,&quot;id&quot;:&quot;dotNET&quot;},{&quot;name&quot;:&quot;iOS-Fastlane&quot;,&quot;id&quot;:&quot;iOS-Fastlane&quot;},{&quot;name&quot;:&quot;npm&quot;,&quot;id&quot;:&quot;npm&quot;}],&quot;Pages&quot;:[{&quot;name&quot;:&quot;Brunch&quot;,&quot;id&quot;:&quot;Brunch&quot;},{&quot;name&quot;:&quot;Doxygen&quot;,&quot;id&quot;:&quot;Doxygen&quot;},{&quot;name&quot;:&quot;Gatsby&quot;,&quot;id&quot;:&quot;Gatsby&quot;},{&quot;name&quot;:&quot;HTML&quot;,&quot;id&quot;:&quot;HTML&quot;},{&quot;name&quot;:&quot;Harp&quot;,&quot;id&quot;:&quot;Harp&quot;},{&quot;name&quot;:&quot;Hexo&quot;,&quot;id&quot;:&quot;Hexo&quot;},{&quot;name&quot;:&quot;Hugo&quot;,&quot;id&quot;:&quot;Hugo&quot;},{&quot;name&quot;:&quot;Hyde&quot;,&quot;id&quot;:&quot;Hyde&quot;},{&quot;name&quot;:&quot;JBake&quot;,&quot;id&quot;:&quot;JBake&quot;},{&quot;name&quot;:&quot;Jekyll&quot;,&quot;id&quot;:&quot;Jekyll&quot;},{&quot;name&quot;:&quot;Jigsaw&quot;,&quot;id&quot;:&quot;Jigsaw&quot;},{&quot;name&quot;:&quot;Lektor&quot;,&quot;id&quot;:&quot;Lektor&quot;},{&quot;name&quot;:&quot;Metalsmith&quot;,&quot;id&quot;:&quot;Metalsmith&quot;},{&quot;name&quot;:&quot;Middleman&quot;,&quot;id&quot;:&quot;Middleman&quot;},{&quot;name&quot;:&quot;Nanoc&quot;,&quot;id&quot;:&quot;Nanoc&quot;},{&quot;name&quot;:&quot;Octopress&quot;,&quot;id&quot;:&quot;Octopress&quot;},{&quot;name&quot;:&quot;Pelican&quot;,&quot;id&quot;:&quot;Pelican&quot;},{&quot;name&quot;:&quot;SwaggerUI&quot;,&quot;id&quot;:&quot;SwaggerUI&quot;}],&quot;Verify&quot;:[{&quot;name&quot;:&quot;Accessibility&quot;,&quot;id&quot;:&quot;Accessibility&quot;},{&quot;name&quot;:&quot;Browser-Performance&quot;,&quot;id&quot;:&quot;Browser-Performance&quot;},{&quot;name&quot;:&quot;FailFast&quot;,&quot;id&quot;:&quot;FailFast&quot;},{&quot;name&quot;:&quot;Load-Performance-Testing&quot;,&quot;id&quot;:&quot;Load-Performance-Testing&quot;}],&quot;Security&quot;:[{&quot;name&quot;:&quot;API-Fuzzing&quot;,&quot;id&quot;:&quot;API-Fuzzing&quot;},{&quot;name&quot;:&quot;Container-Scanning&quot;,&quot;id&quot;:&quot;Container-Scanning&quot;},{&quot;name&quot;:&quot;Coverage-Fuzzing&quot;,&quot;id&quot;:&quot;Coverage-Fuzzing&quot;},{&quot;name&quot;:&quot;DAST&quot;,&quot;id&quot;:&quot;DAST&quot;},{&quot;name&quot;:&quot;Dependency-Scanning&quot;,&quot;id&quot;:&quot;Dependency-Scanning&quot;},{&quot;name&quot;:&quot;License-Management&quot;,&quot;id&quot;:&quot;License-Management&quot;},{&quot;name&quot;:&quot;License-Scanning&quot;,&quot;id&quot;:&quot;License-Scanning&quot;},{&quot;name&quot;:&quot;SAST&quot;,&quot;id&quot;:&quot;SAST&quot;},{&quot;name&quot;:&quot;Secret-Detection&quot;,&quot;id&quot;:&quot;Secret-Detection&quot;},{&quot;name&quot;:&quot;Secure-Binaries&quot;,&quot;id&quot;:&quot;Secure-Binaries&quot;}]}" data-toggle="dropdown"><span class="dropdown-toggle-text ">Apply a template</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-input"><input type="search" id="" class="dropdown-input-field qa-dropdown-input-field" placeholder="Filter" autocomplete="off"><i aria-hidden="true" data-hidden="true" class="fa fa-search dropdown-input-search"></i><i aria-hidden="true" data-hidden="true" role="button" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div><div class="dropdown-content "></div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div></div></div>
</div>
<div class="dockerfile-selector js-dockerfile-selector-wrap js-template-selector-wrap hidden">
<div class="dropdown "><button class="dropdown-menu-toggle js-dockerfile-selector qa-dockerfile-dropdown" type="button" data-data="{&quot;General&quot;:[{&quot;name&quot;:&quot;Binary&quot;,&quot;id&quot;:&quot;Binary&quot;},{&quot;name&quot;:&quot;Binary-alpine&quot;,&quot;id&quot;:&quot;Binary-alpine&quot;},{&quot;name&quot;:&quot;Binary-scratch&quot;,&quot;id&quot;:&quot;Binary-scratch&quot;},{&quot;name&quot;:&quot;Golang&quot;,&quot;id&quot;:&quot;Golang&quot;},{&quot;name&quot;:&quot;Golang-alpine&quot;,&quot;id&quot;:&quot;Golang-alpine&quot;},{&quot;name&quot;:&quot;Golang-scratch&quot;,&quot;id&quot;:&quot;Golang-scratch&quot;},{&quot;name&quot;:&quot;HTTPd&quot;,&quot;id&quot;:&quot;HTTPd&quot;},{&quot;name&quot;:&quot;Node&quot;,&quot;id&quot;:&quot;Node&quot;},{&quot;name&quot;:&quot;Node-alpine&quot;,&quot;id&quot;:&quot;Node-alpine&quot;},{&quot;name&quot;:&quot;OpenJDK&quot;,&quot;id&quot;:&quot;OpenJDK&quot;},{&quot;name&quot;:&quot;OpenJDK-alpine&quot;,&quot;id&quot;:&quot;OpenJDK-alpine&quot;},{&quot;name&quot;:&quot;PHP&quot;,&quot;id&quot;:&quot;PHP&quot;},{&quot;name&quot;:&quot;Python&quot;,&quot;id&quot;:&quot;Python&quot;},{&quot;name&quot;:&quot;Python-alpine&quot;,&quot;id&quot;:&quot;Python-alpine&quot;},{&quot;name&quot;:&quot;Python2&quot;,&quot;id&quot;:&quot;Python2&quot;},{&quot;name&quot;:&quot;Ruby&quot;,&quot;id&quot;:&quot;Ruby&quot;},{&quot;name&quot;:&quot;Ruby-alpine&quot;,&quot;id&quot;:&quot;Ruby-alpine&quot;},{&quot;name&quot;:&quot;Rust&quot;,&quot;id&quot;:&quot;Rust&quot;},{&quot;name&quot;:&quot;Swift&quot;,&quot;id&quot;:&quot;Swift&quot;}]}" data-toggle="dropdown"><span class="dropdown-toggle-text ">Apply a template</span><i aria-hidden="true" data-hidden="true" class="fa fa-chevron-down"></i></button><div class="dropdown-menu dropdown-select dropdown-menu-selectable"><div class="dropdown-input"><input type="search" id="" class="dropdown-input-field qa-dropdown-input-field" placeholder="Filter" autocomplete="off"><i aria-hidden="true" data-hidden="true" class="fa fa-search dropdown-input-search"></i><i aria-hidden="true" data-hidden="true" role="button" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div><div class="dropdown-content "></div><div class="dropdown-loading"><i aria-hidden="true" data-hidden="true" class="fa fa-spinner fa-spin"></i></div></div></div>
</div>
</div>
</div>

<div class="file-buttons">
<button name="button" type="button" class="soft-wrap-toggle btn soft-wrap-active" tabindex="-1"><span class="no-wrap">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="m6 11h-4.509c-.263 0-.491.226-.491.505v.991c0 .291.22.505.491.505h4.509v.679c0 .301.194.413.454.236l2.355-1.607c.251-.171.259-.442 0-.619l-2.355-1.607c-.251-.171-.454-.07-.454.236v.681m-5-7.495c0-.279.22-.505.498-.505h13c.275 0 .498.214.498.505v.991c0 .279-.22.505-.498.505h-13c-.275 0-.498-.214-.498-.505v-.991m10 8c0-.279.215-.505.49-.505h3.02c.271 0 .49.214.49.505v.991c0 .279-.215.505-.49.505h-3.02c-.271 0-.49-.214-.49-.505v-.991m-10-4c0-.279.22-.505.498-.505h13c.275 0 .498.214.498.505v.991c0 .279-.22.505-.498.505h-13c-.275 0-.498-.214-.498-.505v-.991"></path>
</svg>

No wrap
</span>
<span class="soft-wrap">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="m12 11h-2v-.681c0-.307-.203-.407-.454-.236l-2.355 1.607c-.259.177-.251.448 0 .619l2.355 1.607c.259.177.454.065.454-.236v-.679h2c0 0 0 0 0 0 1.657 0 3-1.343 3-3 0-.828-.336-1.578-.879-2.121-.543-.543-1.293-.879-2.121-.879-.001 0-.002 0-.002 0h-10.497c-.271 0-.5.226-.5.505v.991c0 .291.224.505.5.505h10.497c.001 0 .002 0 .002 0 .552 0 1 .448 1 1 0 .276-.112.526-.293.707-.181.181-.431.293-.707.293m-11-7.495c0-.279.22-.505.498-.505h13c.275 0 .498.214.498.505v.991c0 .279-.22.505-.498.505h-13c-.275 0-.498-.214-.498-.505v-.991m0 8c0-.279.215-.505.49-.505h3.02c.271 0 .49.214.49.505v.991c0 .279-.215.505-.49.505h-3.02c-.271 0-.49-.214-.49-.505v-.991"></path>
</svg>

Soft wrap
</span>
</button><div class="encoding-selector">
<div class="select2-container select2" id="s2id_encoding" style="width: 82.4333px;"><a href="javascript:void(0)" class="select2-choice" tabindex="-1">   <span class="select2-chosen" id="select2-chosen-1">text</span><abbr class="select2-search-choice-close"></abbr>   <span class="select2-arrow" role="presentation"><b role="presentation"></b></span></a><label for="s2id_autogen1" class="select2-offscreen"></label><input class="select2-focusser select2-offscreen" type="text" aria-haspopup="true" role="button" aria-labelledby="select2-chosen-1" id="s2id_autogen1" tabindex="-1"><div class="select2-drop select2-display-none select2-with-searchbox">   <div class="select2-search">       <label for="s2id_autogen1_search" class="select2-offscreen"></label>       <input type="text" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" class="select2-input" role="combobox" aria-expanded="true" aria-autocomplete="list" aria-owns="select2-results-1" id="s2id_autogen1_search" placeholder="">   </div>   <ul class="select2-results" role="listbox" id="select2-results-1">   </ul></div></div><select name="encoding" id="encoding" class="select2" tabindex="-1" title="" style="display: none;"><option value="base64">base64</option>
<option selected="selected" value="text">text</option></select>
</div>
</div>
</div>
<div class="file-editor code">
<div class="js-edit-mode-pane qa-editor" id="editor" data-keybinding-context="1" data-mode-id="python"><div class="monaco-editor gl-editor-lite no-user-select  showUnused vs focused" style="width: 947px; height: 500px;" data-uri="file:///gitlab/src/notes/oneNote/msGraphAPI.py"><div data-mprt="3" class="overflow-guard" style="width: 947px; height: 500px;"><div class="margin" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; height: 2261px; width: 68px;" role="presentation" aria-hidden="true"><div class="glyph-margin" style="left: 0px; width: 0px; height: 2261px;"></div><div class="margin-view-zones" style="position: absolute;" role="presentation" aria-hidden="true"></div><div class="margin-view-overlays focused" style="position: absolute; width: 68px; font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; height: 2261px;" role="presentation" aria-hidden="true"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">1</div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">2</div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">3</div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">4</div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">5</div></div><div style="position:absolute;top:95px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">6</div></div><div style="position:absolute;top:114px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">7</div></div><div style="position:absolute;top:133px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">8</div></div><div style="position:absolute;top:152px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">9</div></div><div style="position:absolute;top:171px;width:100%;height:19px;"><div class="cldr codicon codicon-chevron-down" style="left:42px;width:26px;"></div><div class="line-numbers lh-odd" style="left:0px;width:42px;">10</div></div><div style="position:absolute;top:190px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">11</div></div><div style="position:absolute;top:209px;width:100%;height:19px;"><div class="cldr codicon codicon-chevron-down" style="left:42px;width:26px;"></div><div class="line-numbers lh-odd" style="left:0px;width:42px;">12</div></div><div style="position:absolute;top:228px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">13</div></div><div style="position:absolute;top:247px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">14</div></div><div style="position:absolute;top:266px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">15</div></div><div style="position:absolute;top:285px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">16</div></div><div style="position:absolute;top:304px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">17</div></div><div style="position:absolute;top:323px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">18</div></div><div style="position:absolute;top:342px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">19</div></div><div style="position:absolute;top:361px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">20</div></div><div style="position:absolute;top:380px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">21</div></div><div style="position:absolute;top:399px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">22</div></div><div style="position:absolute;top:418px;width:100%;height:19px;"><div class="cldr codicon codicon-chevron-down" style="left:42px;width:26px;"></div><div class="line-numbers lh-odd" style="left:0px;width:42px;">23</div></div><div style="position:absolute;top:437px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">24</div></div><div style="position:absolute;top:456px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">25</div></div><div style="position:absolute;top:475px;width:100%;height:19px;"><div class="line-numbers lh-odd" style="left:0px;width:42px;">26</div></div><div style="position:absolute;top:494px;width:100%;height:19px;"><div class="cldr codicon codicon-chevron-down" style="left:42px;width:26px;"></div><div class="line-numbers lh-odd" style="left:0px;width:42px;">27</div></div></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" style="position: absolute; overflow: hidden; left: 68px; width: 879px; height: 500px;" data-mprt="5"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1000000px; height: 1000000px; touch-action: none; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; left: 0px;"><div class="view-overlays focused" style="position: absolute; height: 0px; width: 879px;" role="presentation" aria-hidden="true"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:92.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:92.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text top-left-radius top-right-radius" style="top:0px;left:0px;width:92.43359375px;height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:497.43359375px;height:19px;"></div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:168.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:168.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:168.43359375px;height:19px;"></div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:151.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:151.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:151.43359375px;height:19px;"></div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:135.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:135.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:135.43359375px;height:19px;"></div></div><div style="position:absolute;top:95px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:345.43359375px;height:19px;"></div></div><div style="position:absolute;top:114px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8.43359375px;height:19px;"></div></div><div style="position:absolute;top:133px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:143.43359375px;height:19px;"></div></div><div style="position:absolute;top:152px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8.43359375px;height:19px;"></div></div><div style="position:absolute;top:171px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:472.43359375px;height:19px;"></div></div><div style="position:absolute;top:190px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:8.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:8.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:8.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:209px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:185.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background bottom-left-radius" style="top:0px;left:185.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text top-right-radius" style="top:0px;left:0px;width:185.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:228px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:269.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div><div class="cigr" style="left:33.734375px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:247px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:227.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:227.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:227.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div><div class="cigr" style="left:33.734375px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:266px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:371.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div><div class="cigr" style="left:33.734375px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:285px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:269.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:269.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:269.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div><div class="cigr" style="left:33.734375px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:304px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:185.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:185.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:185.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div><div class="cigr" style="left:33.734375px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:323px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:269.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div><div class="cigr" style="left:33.734375px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:342px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:185.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:185.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:185.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div><div class="cigr" style="left:33.734375px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:361px;width:100%;height:19px;"><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:185.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div><div class="cigr" style="left:33.734375px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:380px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:75.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:75.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:75.43359375px;height:19px;"></div></div><div style="position:absolute;top:399px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:581.43359375px;height:19px;"></div></div><div style="position:absolute;top:418px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:143.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:143.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:143.43359375px;height:19px;"></div></div><div style="position:absolute;top:437px;width:100%;height:19px;"><div class="cslr selected-text top-right-radius bottom-right-radius" style="top:0px;left:0px;width:295.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:456px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:227.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius" style="top:0px;left:227.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text bottom-right-radius" style="top:0px;left:0px;width:227.43359375px;height:19px;"></div><div class="cigr" style="left:0px;height:19px;width:33.734375px"></div></div><div style="position:absolute;top:475px;width:100%;height:19px;"><div class="cslr selected-text" style="top:0px;left:42.43359375px;width:10px;height:19px;"></div><div class="cslr monaco-editor-background top-left-radius bottom-left-radius" style="top:0px;left:42.43359375px;width:10px;height:19px;"></div><div class="cslr selected-text" style="top:0px;left:0px;width:42.43359375px;height:19px;"></div></div><div style="position:absolute;top:494px;width:100%;height:19px;"><div class="cslr selected-text bottom-left-radius top-right-radius bottom-right-radius" style="top:0px;left:0px;width:160.43359375px;height:19px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"></div><div class="view-zones" style="position: absolute;" role="presentation" aria-hidden="true"></div><div class="view-lines" style="position: absolute; font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; width: 879px; height: 2261px;" role="presentation" aria-hidden="true" data-mprt="7"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk1 mtkb">import</span><span class="mtk1">&nbsp;sys</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk1 mtkb">from</span><span class="mtk1">&nbsp;http.server&nbsp;</span><span class="mtk1 mtkb">import</span><span class="mtk1">&nbsp;HTTPServer,&nbsp;BaseHTTPRequestHandler</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk1 mtkb">import</span><span class="mtk1">&nbsp;socketserver</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk1 mtkb">import</span><span class="mtk1">&nbsp;webbrowser</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk1 mtkb">import</span><span class="mtk1">&nbsp;requests</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk1 mtkb">from</span><span class="mtk1">&nbsp;microsoftgraph.client&nbsp;</span><span class="mtk1 mtkb">import</span><span class="mtk1">&nbsp;Client</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span>&nbsp;</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk1">answer&nbsp;=&nbsp;</span><span class="mtk4">"Empty"</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span>&nbsp;</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1 mtkb">class</span><span class="mtk1">&nbsp;SimpleHTTPRequestHandler(BaseHTTPRequestHandler):</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span>&nbsp;</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 mtkb">def</span><span class="mtk1">&nbsp;do_GET(</span><span class="mtk1 mtkb">self</span><span class="mtk1">):</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 mtkb">self</span><span class="mtk1">.send_response(</span><span class="mtk7">200</span><span class="mtk1">)</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 mtkb">self</span><span class="mtk1">.end_headers()</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8 mtki">#self.wfile.write(b'Hello,&nbsp;world!')</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 mtkb">print</span><span class="mtk1">(</span><span class="mtk1 mtkb">self</span><span class="mtk1">.requestline)</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 mtkb">global</span><span class="mtk1">&nbsp;answer</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;test&nbsp;=&nbsp;</span><span class="mtk1 mtkb">self</span><span class="mtk1">.requestline</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;answer&nbsp;=&nbsp;test</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 mtkb">print</span><span class="mtk1">(answer)</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk1">httpd&nbsp;=&nbsp;socketserver.TCPServer((</span><span class="mtk4">""</span><span class="mtk1">,&nbsp;</span><span class="mtk7">5000</span><span class="mtk1">),&nbsp;SimpleHTTPRequestHandler)</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk1 mtkb">def</span><span class="mtk1">&nbsp;getAnwser():</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk1 mtkb">print</span><span class="mtk1">(</span><span class="mtk4">"serving&nbsp;at&nbsp;port"</span><span class="mtk1">,&nbsp;</span><span class="mtk7">5000</span><span class="mtk1">)</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;httpd.handle_request()</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk1 mtkb">def</span><span class="mtk1">&nbsp;extractCode():</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer has-selection cursor-line-style cursor-solid"><div class="cursor " style="height: 19px; top: 133px; left: 134px; font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; display: none; visibility: inherit; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 865px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; width: 865px;"></div></div><canvas class="decorationsOverviewRuler" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 500px;" aria-hidden="true" width="14" height="500"></canvas><div role="presentation" aria-hidden="true" class="visible scrollbar vertical" style="position: absolute; width: 14px; height: 500px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; height: 110px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 947px;"></div><textarea data-mprt="6" class="inputarea" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." role="textbox" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; line-height: 19px; letter-spacing: 0px; top: 0px; left: 0px; width: 0px; height: 0px;" wrap="off">import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import webbrowser
import requests
from microsoftgraph.client import Client

answer = "Empty"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
…                else:
                    print(keyIntern, ": ", item[keyIntern])
            print()
    else:
        print(pages[key])
    print()
print("-----------------------------------------------------------")

print("listed notebooks")</textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 947px;"><div class="accessibilityHelpWidget" style="display: none; position: absolute;" role="dialog" aria-hidden="true" widgetid="editor.contrib.accessibilityHelpWidget"><div role="document"></div></div><div class="monaco-editor-hover hidden" aria-hidden="true" role="presentation" style="position: absolute;" widgetid="editor.contrib.modesGlyphHoverWidget"></div></div><div data-mprt="8" class="minimap slider-mouseover" style="position: absolute; left: 0px; width: 0px; height: 500px;" role="presentation" aria-hidden="true"><div class="minimap-shadow-hidden" style="height: 500px;"></div><canvas style="position: absolute; left: 0px; width: 0px; height: 500px;" width="0" height="500"></canvas><canvas style="position: absolute; left: 0px; width: 0px; height: 500px;" class="minimap-decorations-layer" width="0" height="500"></canvas><div style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px;" class="minimap-slider"><div style="position: absolute; width: 0px; height: 0px;" class="minimap-slider-horizontal"></div></div></div></div><div data-mprt="2" class="overflowingContentWidgets"><div class="monaco-editor-hover hidden" tabindex="0" style="position: absolute; visibility: hidden; max-width: 1213px;" widgetid="editor.contrib.modesContentHoverWidget"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-editor-hover-content" style="overflow: hidden; font-size: 14px; line-height: 19px; max-height: 250px; max-width: 625.02px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow top-left-corner"></div></div></div><div class="monaco-editor rename-box" style="background-color: rgb(243, 243, 243); box-shadow: rgb(168, 168, 168) 0px 2px 8px; color: rgb(97, 97, 97); position: absolute; visibility: hidden; max-width: 1213px;" widgetid="__renameInputWidget"><input class="rename-input" type="text" aria-label="Rename input. Type new name and press Enter to commit." style="font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;; font-weight: normal; font-size: 14px; background-color: rgb(255, 255, 255); border-width: 0px; border-style: none;"><div class="rename-label" style="font-size: 11.2px;">Enter to Rename, Shift+Enter to Preview</div></div><div class="editor-widget suggest-widget" style="position: absolute; visibility: inherit; max-width: 1213px; top: 19px; left: 68px;" widgetid="editor.widget.suggestWidget" monaco-visible-content-widget="true"><div class="message" style="display: none; background-color: rgb(243, 243, 243); border-color: rgb(200, 200, 200);" aria-hidden="true"></div><div class="tree" style="display: none; background-color: rgb(243, 243, 243); border-color: rgb(200, 200, 200);" aria-hidden="true"><div class="monaco-list list_id_1" tabindex="0" role="tree"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-list-rows" style="transform: translate3d(0px, 0px, 0px); overflow: hidden;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div></div><style type="text/css" media="screen">.monaco-list.list_id_1:focus .monaco-list-row.focused { background-color: #d6ebff; }
.monaco-list.list_id_1:focus .monaco-list-row.focused:hover { background-color: #d6ebff; }
.monaco-list.list_id_1:focus .monaco-list-row.selected { background-color: #0069d1; }
.monaco-list.list_id_1:focus .monaco-list-row.selected:hover { background-color: #0069d1; }
.monaco-list.list_id_1:focus .monaco-list-row.selected { color: #ffffff; }

				.monaco-drag-image,
				.monaco-list.list_id_1:focus .monaco-list-row.selected.focused { background-color: #0074e8; }
			

				.monaco-drag-image,
				.monaco-list.list_id_1:focus .monaco-list-row.selected.focused { color: #ffffff; }
			
.monaco-list.list_id_1 .monaco-list-row.focused { background-color:  #d6ebff; }
.monaco-list.list_id_1 .monaco-list-row.focused:hover { background-color:  #d6ebff; }
.monaco-list.list_id_1 .monaco-list-row.selected { background-color:  #e4e6f1; }
.monaco-list.list_id_1 .monaco-list-row.selected:hover { background-color:  #e4e6f1; }
.monaco-list.list_id_1:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color:  #f0f0f0; }

				.monaco-list.list_id_1.drop-target,
				.monaco-list.list_id_1 .monaco-list-rows.drop-target,
				.monaco-list.list_id_1 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; }
			
.monaco-list-type-filter { background-color: #efc1ad }
.monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); }
.monaco-list-type-filter.no-matches { border: 1px solid #be1100; }
.monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }</style></div></div><div class="suggest-status-bar" style="display: none; background-color: rgb(243, 243, 243); border-color: rgb(200, 200, 200);" aria-hidden="true"><span></span><span></span></div><div class="details" style="font-size: 14px; font-weight: normal; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; display: none; background-color: rgb(243, 243, 243); border-color: rgb(200, 200, 200);" aria-hidden="true"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="body" style="overflow: hidden;"><div class="header"><span class="codicon codicon-close" title="Read less...Ctrl+Space" style="height: 19px; width: 19px;"></span><p class="type" style="font-family: &quot;Droid Sans Mono&quot;, &quot;monospace&quot;, monospace, &quot;Droid Sans Fallback&quot;;"></p></div><p class="docs"></p></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow top-left-corner"></div></div></div></div></div><div class="context-view" style="display: none;" aria-hidden="true"></div></div></div>
<div class="js-edit-mode-pane hide" id="preview">
<div class="center">
<h2>
<i class="icon-spinner icon-spin"></i>
</h2>
</div>
</div>
</div>
</div>

<div class="form-group row commit_message-group">
<label class="col-form-label col-sm-2" for="commit_message-023d3d830bbbe3963153a78ada861764">Commit message
</label><div class="col-sm-10">
<div class="commit-message-container">
<div class="max-width-marker"></div>
<textarea name="commit_message" id="commit_message-023d3d830bbbe3963153a78ada861764" class="form-control js-commit-message" placeholder="Update msGraphAPI.py" required="required" rows="3">Update msGraphAPI.py</textarea>
</div>
</div>
</div>

<div class="form-group row branch">
<label class="col-form-label col-sm-2" for="branch_name">Target Branch</label>
<div class="col-sm-10">
<input type="text" name="branch_name" id="branch_name" value="master" required="required" class="form-control js-branch-name ref-name">
<div class="js-create-merge-request-container" style="display: none;">
<div class="form-check gl-mt-3">
<input type="checkbox" name="create_merge_request" id="create_merge_request-cadb6e0164258397ce028ad90bf69b42" value="1" class="js-create-merge-request form-check-input">
<label class="form-check-label" for="create_merge_request-cadb6e0164258397ce028ad90bf69b42">Start a <strong>new merge request</strong> with these changes
</label></div>

</div>
</div>
</div>
<input type="hidden" name="original_branch" id="original_branch" value="master" class="js-original-branch">

<input type="hidden" name="last_commit_sha" id="last_commit_sha" value="c6ba2fa51835521b71d24e594130ea262ffe1abc">
<input type="hidden" name="content" id="file-content" value="">
<input type="hidden" name="from_merge_request_iid" id="from_merge_request_iid">
<div class="form-actions">
<button name="button" type="submit" id="commit-changes" class="btn commit-btn js-commit-button btn-success qa-commit-button">Commit changes</button>
<a class="btn btn-cancel" data-confirm="Leave edit mode? All unsaved changes will be lost." href="https://gitlab.oth-regensburg.de/hos47096/hsp-ss20-schildgen-saas/-/blob/master/src/notes/oneNote/msGraphAPI.py">Cancel</a>

</div>

</form></div>

</div>
</div>
</div>
</div>

<div class="footer-message" style="background-color: #ffffff;color: #000000"><p><a href="https://www.oth-regensburg.de/datenschutz.html" rel="nofollow noreferrer noopener" target="_blank">Datenschutz</a> <a href="https://www.oth-regensburg.de/impressum.html" rel="nofollow noreferrer noopener" target="_blank">Impressum</a></p></div>
<script>
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded', 'qa-js-lazy-loaded');
  });
}

//]]>
</script>




<span role="status" aria-live="polite" class="select2-hidden-accessible"></span><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="status" aria-atomic="true"></div></div></body></html>