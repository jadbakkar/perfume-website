import re

content = """1: <!DOCTYPE html>
2: <html lang="en">
3: 
4: <head>
5:     <meta charset="UTF-8">
6:     <meta name="viewport" content="width=device-width, initial-scale=1.0">
7:     <meta name="description"
8:         content="Velmora Fragrancias — Inspired by the world's greatest perfume houses. We craft high-concentration luxury oil perfumes with our signature presentation. Discover your perfect scent in Lebanon.">
9:     <meta name="keywords" content="perfume, fragrance, luxury scents, inspired perfume, concentrated perfume oil, Lebanon perfume, Velmora Fragrancias, custom packaging">
10:     <meta name="author" content="Velmora Fragrancias">
11:     
12:     <!-- Open Graph for social sharing -->
13:     <meta property="og:title" content="Velmora Fragrancias | Luxury Inspired Scents">
14:     <meta property="og:description" content="Choose the big-brand perfume that speaks to you. We recreate it with our own exclusive packaging and high-concentration oils for 12+ hours of lasting sillage.">
15:     <meta property="og:image" content="photo/hero.jpg">
16:     <meta property="og:type" content="website">
17: 
18:     <title>Velmora Fragrancias | Luxury Inspired Scents</title>
19: 
20:     <!-- Google Fonts -->
21:     <link rel="preconnect" href="https://fonts.googleapis.com">
22:     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
23:     <link
24:         href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600&family=Outfit:wght@300;400;500;600;700&display=swap"
25:         rel="stylesheet">
26: 
27:     <!-- FontAwesome -->
28:     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
29: 
30: 
31:     <link rel="stylesheet" href="index.css">
32: </head>
33: 
34: <body>
35: 
36:     <!-- ===================== 1. HEADER SECTION ===================== -->
37:     <header class="header" id="mainHeader" style="flex-direction: column; padding: 0;">
38:         <div class="ticker-ribbon" style="width: 100%; background: var(--champagne-gold); color: var(--velmora-navy); font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; padding: 6px 0; text-align: center; white-space: nowrap; overflow: hidden;">
39:             <marquee scrollamount="6" scrolldelay="0" style="width: 100%;">
40:                 ✨ SPECIAL OFFER: Get a FREE Discovery Set with any 100ml purchase • 🚚 Nationwide Delivery across Lebanon • 💧 Pure Concentrated Oil — 12+ Hours Lasting Sillage ✨
41:             </marquee>
42:         </div>
43:         <div style="display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 14px 40px;" class="header-inner">
44:         <a href="#" class="logo-wrap">
45:             <img src="photo/logo.jpeg" alt="Velmora Fragrancias Logo" class="logo-img">
46:             <span class="logo-text" style="color: var(--velmora-navy)">vELMORa</span>
47:         </a>
48: 
49:         <nav class="nav" id="mainNav">
50:             <a href="#hero" class="nav-link active" id="nl-home">Home</a>
51:             <a href="#library" class="nav-link" id="nl-library">Library</a>
52:             <a href="#about" class="nav-link" id="nl-about">About Us</a>
53:             <a href="#tips" class="nav-link" id="nl-tips">Tips</a>
54:             <a href="#packaging" class="nav-link" id="nl-pack">Our Packaging</a>
55:             <a href="#reviews" class="nav-link" id="nl-reviews">Reviews</a>
56:         </nav>
57: 
58:         <div class="header-right">
59:             <button class="icon-btn profile-btn" id="headerProfileBtn" aria-label="Profile">
60:                 <i class="fa-solid fa-user"></i>
61:             </button>
62:             <button class="icon-btn hamburger" id="hamburgerBtn" aria-label="Menu">
63:                 <i class="fa-solid fa-bars"></i>
64:             </button>
65:         </div>
66:         </div>
67:     </header>
68: 
69:     <!-- ===================== 2. MOBILE DRAWER SECTION ===================== -->
70:     <div class="mobile-drawer-overlay" id="drawerOverlay"></div>
71:     <div class="mobile-drawer" id="mobileDrawer">
72:         <div class="drawer-header">
73:             <span class="drawer-logo">vELMORa</span>
74:             <button class="drawer-close" id="drawerCloseBtn" aria-label="Close menu">
75:                 <i class="fa-solid fa-xmark"></i>
76:             </button>
77:         </div>
78:         <nav class="drawer-nav">
79:             <a href="#hero" class="drawer-nav-link" id="dn-home">
80:                 <i class="fa-solid fa-house"></i> Home
81:             </a>
82:             <a href="#library" class="drawer-nav-link" id="dn-library">
83:                 <i class="fa-solid fa-bottle-droplet"></i> Scent Library
84:             </a>
85:             <a href="#about" class="drawer-nav-link" id="dn-about">
86:                 <i class="fa-solid fa-book-open"></i> About Us
87:             </a>
88:             <a href="#tips" class="drawer-nav-link" id="dn-tips">
89:                 <i class="fa-solid fa-lightbulb"></i> Tips
90:             </a>
91:             <a href="#packaging" class="drawer-nav-link" id="dn-pack">
92:                 <i class="fa-solid fa-box-open"></i> Our Packaging
93:             </a>
94:             <a href="#reviews" class="drawer-nav-link" id="dn-reviews">
95:                 <i class="fa-solid fa-star"></i> Reviews
96:             </a>
97:         </nav>
98:         <div class="drawer-footer">
99:             <button class="btn-wa-lg" id="drawerProfileBtn" style="width: 100%; margin-bottom: 20px; background: rgba(255,255,255,0.1); color: var(--champagne-gold); border: 1px solid rgba(201,168,76,0.5); box-shadow: none;">
100:                 <i class="fa-solid fa-user"></i> My Profile
101:             </button>
102:             <div class="drawer-social" style="margin-top:0">
103:                 <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
104:                 <a href="#" aria-label="TikTok"><i class="fa-brands fa-tiktok"></i></a>
105:                 <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
106:                 <a href="https://wa.me/96170917681" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
107:             </div>
108:         </div>
109:     </div>
110: 
111:     <!-- ===================== 3. HERO SECTION ===================== -->
112:     <section class="hero" id="hero">
113:         <div class="hero-bg" id="heroBg"></div>
114: 
115:         <!-- Floating particles -->
116:         <div class="particles" id="particles"></div>
117: 
118:         <div class="hero-content">
119:             <div class="hero-eyebrow">Inspired by Luxury · Crafted by Velmora</div>
120: 
121:             <h1 class="hero-title">Your Favourite Scent.<br><em>Our Signature.</em></h1>
122: 
123:             <p class="hero-sub">
124:                 Choose the big-brand perfume that speaks to you.<br>
125:                 We recreate it — with our own exclusive packaging and quality.
126:             </p>
127: 
128:             <!-- ── BRAND SEARCH BAR ── -->
129:             <div class="brand-search-wrap">
130:                 <div class="brand-search-glass">
131:                     <div class="search-icon-wrap">
132:                         <i class="fa-solid fa-magnifying-glass"></i>
133:                     </div>
134:                     <input type="text" class="brand-search-input" id="heroSearchInput"
135:                         placeholder="Search Chanel, Dior, Creed…" autocomplete="off" aria-label="Search brand">
136:                     <button class="search-clear-btn" id="searchClearBtn" aria-label="Clear search">
137:                         <i class="fa-solid fa-xmark"></i>
138:                     </button>
139:                 </div>
140:                 <div class="brand-dropdown" id="brandDropdown">
141:                     <!-- populated by JS -->
142:                 </div>
143:             </div>
144: 
145:             <!-- Brand Chips -->
146:             <div class="brand-chips" id="brandChips">
147:                 <!-- populated by JS -->
148:             </div>
149: 
150:             <!-- Quiz CTA -->
151:             <div style="margin-top: 36px;">
152:                 <button class="btn-wa-lg glow-btn" id="quizLaunchBtn" style="background: var(--turquoise); color: var(--pure-white); box-shadow: 0 8px 32px rgba(21,157,154,.3); max-width: 320px; margin: 0 auto; border: none;">
153:                     <i class="fa-solid fa-wand-magic-sparkles"></i>
154:                     Find My Perfect Scent
155:                 </button>
156:             </div>
157:         </div>
158: 
159:         <div class="scroll-hint">
160:             <i class="fa-solid fa-chevron-down"></i>
161:         </div>
162:     </section>
163: 
164:     <!-- ===================== 4. BRAND MARQUEE SECTION ===================== -->
165:     <div class="brand-strip">
166:         <div class="brand-strip-inner" id="brandStrip">
167:             <!-- duplicated by JS for infinite loop -->
168:         </div>
169:     </div>
170: 
171:     <!-- ===================== 5. ABOUT US ===================== -->
172:     <section id="about" class="section-full">
173:         <div class="packaging-grid" style="max-width:var(--max-w);margin:0 auto;">
174:             <div class="packaging-img-side">
175:                 <img src="photo/about-us.jpg" alt="Velmora Heritage" style="border-radius: var(--r-md); box-shadow: 0 20px 60px rgba(0,0,0,0.1); width: 100%; object-fit: cover; aspect-ratio: 4/5;">
176:             </div>
177:             <div class="packaging-content-side">
178:                 <div class="section-badge">Our Story</div>
179:                 <h2 class="section-title">About <em>Us</em></h2>
180:                 
181:                 <div class="about-grid" style="display: grid; grid-template-columns: 1fr; gap: 32px; margin-top: 40px;">
182:                     <div class="glass-card" style="padding: 24px; text-align: left;">
183:                         <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 24px; color: var(--champagne-gold); margin-bottom: 12px;">Who We Are</h3>
184:                         <p style="color: rgba(17,38,63,0.7); font-size: 14.5px; line-height: 1.7;">VELMORA is more than a fragrance—it is a presence you feel and an impression that remains. A Lebanese fragrance house created to bring together luxury, quality and distinction through thoughtfully priced scents.</p>
185:                     </div>
186:                     
187:                     <div class="glass-card" style="padding: 24px; text-align: left;">
188:                         <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 24px; color: var(--champagne-gold); margin-bottom: 12px;">Our Quality</h3>
189:                         <p style="color: rgba(17,38,63,0.7); font-size: 14.5px; line-height: 1.7;">We carefully select European fragrance oils to create refined scents with distinctive character, elegant projection and lasting performance. Because true quality does not need an introduction—you experience it from the first spray.</p>
190:                     </div>
191: 
192:                     <div class="glass-card" style="padding: 24px; text-align: left;">
193:                         <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 24px; color: var(--champagne-gold); margin-bottom: 12px;">Our Difference</h3>
194:                         <p style="color: rgba(17,38,63,0.7); font-size: 14.5px; line-height: 1.7;">At VELMORA, we do not simply offer a bottle of perfume. Every order is prepared, bottled and packaged with care—creating a complete experience worthy of the fragrance inside.</p>
195:                     </div>
196: 
197:                     <div class="glass-card" style="padding: 24px; text-align: left;">
198:                         <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 24px; color: var(--champagne-gold); margin-bottom: 12px;">Our Promise</h3>
199:                         <p style="color: rgba(17,38,63,0.7); font-size: 15px; line-height: 1.7;">Quality you can smell. Luxury you can experience. Thoughtful prices without compromising distinction.<br><br>This is more than a statement—it is the VELMORA promise.</p>
200:                     </div>
201:                 </div>
202:             </div>
203:         </div>
204:     </section>
205: 
206:     <div class="divider"></div>
207: 
208:     <!-- ===================== 6. SCENT LIBRARY SECTION ===================== -->
209:     <section id="library">
210:         <div class="section">
211:             <div class="section-head-split">
212:                 <div>
213:                     <div class="section-badge">Scent Collection</div>
214:                     <h2 class="section-title" style="margin-bottom:0">The <em>Library</em></h2>
215:                     <p class="section-sub mb-0" style="margin-top:10px;margin-bottom:0; color: rgba(17,38,63,0.7);">
216:                         Filter by brand or category and tap any item to order.
217:                     </p>
218:                 </div>
219:                 <div class="filter-bar" id="filterBar">
220:                     <button class="filter-btn active" data-filter="all">All</button>
221:                     <button class="filter-btn" data-filter="men">For Him</button>
222:                     <button class="filter-btn" data-filter="women">For Her</button>
223:                     <button class="filter-btn" data-filter="unisex">Unisex</button>
224:                 </div>
225:             </div>
226: 
227:             <!-- Brand sub-filter pills -->
228:             <div id="activeBrandLabel" style="margin-bottom:28px;display:none">
229:                 <span style="font-size:13px;color:rgba(17,38,63,0.6)">Showing results for </span>
230:                 <span id="activeBrandName" style="color:var(--champagne-gold);font-weight:600"></span>
231:                 <button id="clearBrandBtn"
232:                     style="margin-left:10px;font-size:12px;color:rgba(17,38,63,0.4);text-decoration:underline">Clear</button>
233:             </div>
234: 
235:             <div class="library-grid" id="libraryGrid">
236:                 <!-- Populated by JS -->
237:             </div>
238:         </div>
239:     </section>
240: 
241:     <div class="divider"></div>
242: 
243:     <section id="tips" class="section-full">
244:         <div class="packaging-grid" style="max-width:var(--max-w);margin:0 auto;">
245:             <div class="packaging-content-side">
246:                 <div class="section-badge">Expert Advice</div>
247:                 <h2 class="section-title">Fragrance <em>Tips</em></h2>
248:                 
249:                 <div class="steps-grid" style="display: grid; grid-template-columns: 1fr; gap: 32px; margin-top: 40px;">
250:                     <div class="glass-card" style="padding: 24px; text-align: left; display: flex; gap: 20px; align-items: flex-start;">
251:                         <div style="font-size: 28px; color: var(--champagne-gold); flex-shrink: 0;">
252:                             <i class="fa-solid fa-droplet"></i>
253:                         </div>
254:                         <div>
255:                             <h3 style="font-size: 18px; font-weight: 600; margin-bottom: 8px;">Pulse Points</h3>
256:                             <p style="color: rgba(17,38,63,0.7); font-size: 14px; line-height: 1.6;">Apply pure oils to your neck, wrists, and behind the ears where body heat helps diffuse the fragrance.</p>
257:                         </div>
258:                     </div>
259:                     <div class="glass-card" style="padding: 24px; text-align: left; display: flex; gap: 20px; align-items: flex-start;">
260:                         <div style="font-size: 28px; color: var(--champagne-gold); flex-shrink: 0;">
261:                             <i class="fa-solid fa-sun-plant-wilt"></i>
262:                         </div>
263:                         <div>
264:                             <h3 style="font-size: 18px; font-weight: 600; margin-bottom: 8px;">Proper Storage</h3>
265:                             <p style="color: rgba(17,38,63,0.7); font-size: 14px; line-height: 1.6;">Keep your apothecary bottle away from direct sunlight and extreme temperatures to preserve the delicate notes.</p>
266:                         </div>
267:                     </div>
268:                     <div class="glass-card" style="padding: 24px; text-align: left; display: flex; gap: 20px; align-items: flex-start;">
269:                         <div style="font-size: 28px; color: var(--champagne-gold); flex-shrink: 0;">
270:                             <i class="fa-solid fa-layer-group"></i>
271:                         </div>
272:                         <div>
273:                             <h3 style="font-size: 18px; font-weight: 600; margin-bottom: 8px;">Scent Layering</h3>
274:                             <p style="color: rgba(17,38,63,0.7); font-size: 14px; line-height: 1.6;">Mix a drop of fresh citrus with a deeper woody scent to effortlessly create your own signature blend.</p>
275:                         </div>
276:                     </div>
277:                 </div>
278:             </div>
279:             <div class="packaging-img-side">
280:                 <img src="photo/tipbackimg.jpg" alt="Fragrance Tips" style="border-radius: var(--r-md); box-shadow: 0 20px 60px rgba(0,0,0,0.1); width: 100%; object-fit: cover; aspect-ratio: 4/5;">
281:             </div>
282:         </div>
283:     </section>
284: 
285:     <div class="divider"></div>
286: 
287:     <!-- ===================== 7. PACKAGING & GIFT BOX SECTION ===================== -->
288:     <section id="packaging" class="section-full packaging-section">
289:         <div class="packaging-grid" style="max-width:var(--max-w);margin:0 auto">
290:             <div class="packaging-img-side">
291:                 <img src="photo/the-package.jpg" alt="Velmora Signature Packaging and Gift Box">
292:             </div>
293:             <div class="packaging-content-side">
294:                 <div class="section-badge">The Unboxing Experience</div>
295:                 <h2 class="section-title" style="margin-bottom:28px">The Velmora <em>Gift Box</em></h2>
296: 
297:                 <div class="packaging-feature">
298:                     <div class="packaging-feature-icon"><i class="fa-solid fa-box-heart"></i></div>
299:                     <div>
300:                         <h4>Premium Gift-Ready Box</h4>
301:                         <p>Every order arrives in our stunning luxury kraft gift box with shredded fill paper, making it the perfect present for yourself or a loved one.</p>
302:                     </div>
303:                 </div>
304:                 <div class="packaging-feature">
305:                     <div class="packaging-feature-icon"><i class="fa-solid fa-bottle-droplet"></i></div>
306:                     <div>
307:                         <h4>Signature Glass Bottle</h4>
308:                         <p>Each fragrance is poured into our custom apothecary-style glass bottle with a handcrafted wooden cork stopper.</p>
309:                     </div>
310:                 </div>
311:                 <div class="packaging-feature">
312:                     <div class="packaging-feature-icon"><i class="fa-solid fa-tag"></i></div>
313:                     <div>
314:                         <h4>Personalized Detail</h4>
315:                         <p>Every bottle features a custom Velmora label adorned with your bespoke scent profile—your own piece of luxury.</p>
316:                     </div>
317:                 </div>
318:                 <div class="packaging-feature">
319:                     <div class="packaging-feature-icon"><i class="fa-solid fa-flask"></i></div>
320:                     <div>
321:                         <h4>High-Concentration Formula</h4>
322:                         <p>Pure concentrated perfume oil—no alcohol dilution—delivering 12+ hours of lasting sillage and projection right out of the box.</p>
323:                     </div>
324:                 </div>
325:             </div>
326:         </div>
327:     </section>
328: 
329:     <div class="divider"></div>
330: 
331:     <!-- ===================== 8. REVIEWS SECTION ===================== -->
332:     <section id="reviews">
333:         <div class="section">
334:             <div class="text-center" style="margin-bottom:50px">
335:                 <div class="section-badge">Client Reviews</div>
336:                 <h2 class="section-title">What Our Clients <em>Say</em></h2>
337:             </div>
338:             <div class="marquee-wrapper" style="margin-bottom: 20px;">
339:                 <div class="marquee-content reviews-marquee">
340:                     <!-- Review 1 -->
341:                     <div class="review-card glass-card" style="padding: 24px; flex-shrink: 0;">
342:                         <div style="color: var(--champagne-gold); margin-bottom: 12px; font-size: 14px;">
343:                             <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
344:                         </div>
345:                         <p style="font-size: 14px; color: rgba(17,38,63,0.8); line-height: 1.7; font-style: italic; margin-bottom: 16px;">"I ordered the Chanel Chance inspired scent and received it the next day. The packaging alone was worth it — the bottle is stunning and the scent lasts all day!"</p>
346:                         <div style="display: flex; gap: 12px; align-items: center;">
347:                             <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(201,168,76,0.15); color: var(--champagne-gold); display: flex; align-items: center; justify-content: center; font-weight: 600;">LR</div>
348:                             <div>
349:                                 <div style="font-weight: 600; font-size: 14px; color: var(--velmora-navy);">Lara R.</div>
350:                                 <div style="font-size: 12px; color: var(--champagne-gold);">Verified Client</div>
351:                             </div>
352:                         </div>
353:                     </div>
354:                     <!-- Review 2 -->
355:                     <div class="review-card glass-card" style="padding: 24px; flex-shrink: 0;">
356:                         <div style="color: var(--champagne-gold); margin-bottom: 12px; font-size: 14px;">
357:                             <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
358:                         </div>
359:                         <p style="font-size: 14px; color: rgba(17,38,63,0.8); line-height: 1.7; font-style: italic; margin-bottom: 16px;">"Ordered the Creed Aventus inspired version. Honestly better than the original in terms of longevity. The wooden cap is such a classy touch. Will order again!"</p>
360:                         <div style="display: flex; gap: 12px; align-items: center;">
3-62:                             <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(201,168,76,0.15); color: var(--champagne-gold); display: flex; align-items: center; justify-content: center; font-weight: 600;">KM</div>
363:                             <div>
364:                                 <div style="font-weight: 600; font-size: 14px; color: var(--velmora-navy);">Karim M.</div>
365:                                 <div style="font-size: 12px; color: var(--champagne-gold);">Verified Client</div>
366:                             </div>
367:                         </div>
368:                     </div>
369:                     <!-- Review 3 -->
370:                     <div class="review-card glass-card" style="padding: 24px; flex-shrink: 0;">
371:                         <div style="color: var(--champagne-gold); margin-bottom: 12px; font-size: 14px;">
372:                             <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-regular fa-star-half-stroke"></i>
373:                         </div>
374:                         <p style="font-size: 14px; color: rgba(17,38,63,0.8); line-height: 1.7; font-style: italic; margin-bottom: 16px;">"The WhatsApp ordering was so easy and fast. I described what I wanted and they confirmed within minutes. The gift box is perfect for presents!"</p>
375:                         <div style="display: flex; gap: 12px; align-items: center;">
376:                             <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(201,168,76,0.15); color: var(--champagne-gold); display: flex; align-items: center; justify-content: center; font-weight: 600;">NS</div>
377:                             <div>
378:                                 <div style="font-weight: 600; font-size: 14px; color: var(--velmora-navy);">Nour S.</div>
379:                                 <div style="font-size: 12px; color: var(--champagne-gold);">Verified Client</div>
380:                             </div>
381:                         </div>
382:                     </div>
383:                 </div>
384:             </div>
385: 
386:             <!-- ROW 2 MARQUEE (Moves from right to left, same animation but different items) -->
387:             <div class="marquee-wrapper">
388:                 <div class="marquee-content reviews-marquee" style="animation-duration: 35s;"> <!-- slightly different speed for variation -->
389:                     <!-- Review 4 -->
390:                     <div class="review-card glass-card" style="padding: 24px; flex-shrink: 0;">
391:                         <div style="color: var(--champagne-gold); margin-bottom: 12px; font-size: 14px;">
392:                             <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
393:                         </div>
394:                         <p style="font-size: 14px; color: rgba(17,38,63,0.8); line-height: 1.7; font-style: italic; margin-bottom: 16px;">"Absolutely mind-blowing quality. The concentration of the oil means I only need a tiny drop and my whole office smells incredible all day."</p>
395:                         <div style="display: flex; gap: 12px; align-items: center;">
396:                             <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(201,168,76,0.15); color: var(--champagne-gold); display: flex; align-items: center; justify-content: center; font-weight: 600;">EH</div>
397:                             <div>
398:                                 <div style="font-weight: 600; font-size: 14px; color: var(--velmora-navy);">Elie H.</div>
399:                                 <div style="font-size: 12px; color: var(--champagne-gold);">Verified Client</div>
400:                             </div>
401:                         </div>
402:                     </div>
403:                     <!-- Review 5 -->
404:                     <div class="review-card" style="padding: 24px; flex-shrink: 0;">
405:                         <div style="color: var(--champagne-gold); margin-bottom: 12px; font-size: 14px;">
406:                             <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
407:                         </div>
408:                         <p style="font-size: 14px; color: rgba(17,38,63,0.8); line-height: 1.7; font-style: italic; margin-bottom: 16px;">"I've bought from other 'inspired by' places before, but Velmora is different. The presentation feels truly high-end, and the scent notes are perfectly balanced."</p>
409:                         <div style="display: flex; gap: 12px; align-items: center;">
410:                             <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(201,168,76,0.15); color: var(--champagne-gold); display: flex; align-items: center; justify-content: center; font-weight: 600;">SD</div>
411:                             <div>
412:                                 <div style="font-weight: 600; font-size: 14px; color: var(--velmora-navy);">Sarah D.</div>
413:                                 <div style="font-size: 12px; color: var(--champagne-gold);">Verified Client</div>
414:                             </div>
415:                         </div>
416:                     </div>
417:                     <!-- Review 6 -->
418:                     <div class="review-card" style="padding: 24px; flex-shrink: 0;">
419:                         <div style="color: var(--champagne-gold); margin-bottom: 12px; font-size: 14px;">
420:                             <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
421:                         </div>
422:                         <p style="font-size: 14px; color: rgba(17,38,63,0.8); line-height: 1.7; font-style: italic; margin-bottom: 16px;">"My wife loved the Vanilla 28 inspired scent. Delivery to Tripoli took less than 24 hours. Great customer service and an amazing product."</p>
423:                         <div style="display: flex; gap: 12px; align-items: center;">
424:                             <div style="width: 40px; height: 40px; border-radius: 50%; background: rgba(201,168,76,0.15); color: var(--champagne-gold); display: flex; align-items: center; justify-content: center; font-weight: 600;">AK</div>
425:                             <div>
426:                                 <div style="font-weight: 600; font-size: 14px; color: var(--velmora-navy);">Ahmad K.</div>
427:                                 <div style="font-size: 12px; color: var(--champagne-gold);">Verified Client</div>
428:                             </div>
429:                         </div>
430:                     </div>
431:                 </div>
432:             </div>
433:         </div>
434:     </section>
435: 
436:     <!-- ===================== 9. FOOTER SECTION ===================== -->
437:     <footer class="footer">
438:         <div class="footer-grid">
439:             <div>
440:                 <div class="footer-logo-wrap">
441:                     <img src="photo/logo.jpeg" alt="Velmora Logo">
442:                     <span class="footer-brand-name">vELMORa</span>
443:                 </div>
444:                 <p class="footer-desc">
445:                     Velmora Fragrancias crafts luxury-inspired concentrated oil perfumes — your favourite designer
446:                     scents, reimagined in our signature packaging.
447:                 </p>
448:                 <div class="social-links">
449:                     <a href="#" class="social-link" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
450:                     <a href="#" class="social-link" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
451:                     <a href="#" class="social-link" aria-label="TikTok"><i class="fa-brands fa-tiktok"></i></a>
452:                     <a href="https://wa.me/96170917681" class="social-link" aria-label="WhatsApp"><i
453:                             class="fa-brands fa-whatsapp"></i></a>
454:                 </div>
455:             </div>
456: 
457:             <div>
458:                 <div class="footer-col-title">Quick Links</div>
459:                 <div class="footer-links">
460:                     <a href="#library">Shop Collection</a>
461:                     <a href="#how">How It Works</a>
462:                     <a href="#packaging">Our Packaging</a>
463:                     <a href="#reviews">Reviews</a>
464:                 </div>
465:             </div>
466: 
467:             <div>
468:                 <div class="footer-col-title">Categories</div>
469:                 <div class="footer-links" id="footerBrandLinks">
470:                     <!-- populated by JS -->
471:                 </div>
472:             </div>
473: 
474:             <div>
475:                 <div class="footer-col-title">Stay Updated</div>
476:                 <p style="font-size:13.5px;color:rgba(17,38,63,0.7);line-height:1.7;margin-bottom:6px">
477:                     Subscribe for new scent drops and exclusive offers.
478:                 </p>
479:                 <form class="newsletter-form"
480:                     onsubmit="event.preventDefault(); showToast('🎉 Subscribed! Thank you.');">
481:                     <input type="email" class="newsletter-input" placeholder="Your email address" required>
482:                     <button type="submit" class="newsletter-btn">Join</button>
483:                 </form>
484:             </div>
485:         </div>
486:         <div class="footer-bottom">
487:             <p>© 2026 Velmora Fragrancias. All rights reserved.</p>
488:             <p>Made with ♥ for luxury lovers — <a href="https://wa.me/96170917681">Order on WhatsApp</a></p>
489:         </div>
490:     </footer>
491: 
492:     <!-- Floating WA removed -->
493: 
494:     <!-- ===================== 10. ORDER MODAL SECTION ===================== -->
495:     <div class="modal-overlay" id="orderModal">
496:         <div class="modal-box">
497:             <div class="modal-header">
498:                 <h2 class="modal-title">Place Your Order</h2>
499:                 <button class="modal-close" id="modalCloseBtn" aria-label="Close modal">
500:                     <i class="fa-solid fa-xmark"></i>
501:                 </button>
502:             </div>
503: 
504:             <!-- Product preview -->
505:             <div class="modal-product-preview">
506:                 <div class="modal-thumb" id="modalThumb">
507:                     <i class="fa-solid fa-bottle-droplet"></i>
508:                 </div>
509:                 <div>
510:                     <div class="modal-product-brand" id="modalBrand">Brand</div>
511:                     <div class="modal-product-name" id="modalName">Perfume Name</div>
512:                 </div>
513:             </div>
514: 
515:             <div class="modal-form-group">
516:                 <label>Size</label>
517:                 <select id="modalSize">
518:                     <option value="50ml" selected>50 ml</option>
519:                     <option value="100ml">100 ml</option>
520:                 </select>
521:             </div>
522: 
523:             <div class="modal-form-group">
524:                 <label>Your Name</label>
525:                 <input type="text" id="modalClientName" placeholder="Full name">
526:             </div>
527: 
528:             <div class="modal-form-group">
529:                 <label>Your Phone / WhatsApp</label>
530:                 <input type="tel" id="modalClientPhone" placeholder="+961 XX XXX XXX">
531:             </div>
532: 
533:             <div class="modal-form-group">
534:                 <label>Delivery Address</label>
535:                 <input type="text" id="modalClientAddress" placeholder="City, area, building…">
536:             </div>
537: 
538:             <button class="btn-wa-lg" id="modalSendBtn" style="background: var(--turquoise); color: var(--pure-white);">
539:                 <i class="fa-brands fa-whatsapp"></i>
540:                 Send Order on WhatsApp
541:             </button>
542:         </div>
543:     </div>
544: 
545:     <!-- ===================== 11. TOAST NOTIFICATION SECTION ===================== -->
546:     <div id="toastEl" style="
547:         position:fixed; bottom:90px; left:50%; transform:translateX(-50%) translateY(20px);
548:         background:rgba(255,249,240,.95); backdrop-filter:blur(16px);
549:         border:1px solid rgba(17,38,63,.15); border-radius:50px;
550:         padding:12px 24px; color:var(--velmora-navy); font-size:14px; font-weight:500;
551:         box-shadow:0 8px 32px rgba(0,0,0,.15);
552:         opacity:0; pointer-events:none; transition:all .35s;
553:         z-index:2000; white-space:nowrap;
554:     "></div>
555: 
556:     <!-- ===================== 12. SCENT PROFILER QUIZ MODAL ===================== -->
557:     <div class="modal-overlay" id="quizModal">
558:         <div class="modal-box quiz-box">
559:             <button class="modal-close" id="quizCloseBtn" aria-label="Close quiz">
560:                 <i class="fa-solid fa-xmark"></i>
561:             </button>
562: 
563:             <!-- Quiz Screens Container -->
564:             <div id="quizContainer" style="padding-top: 10px;">
565:                 <!-- Start Screen -->
566:                 <div class="quiz-screen active" id="quizStartScreen">
567:                     <div class="quiz-icon-header" style="font-size: 36px; color: var(--champagne-gold); margin-bottom: 20px;"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
568:                     <h2 class="section-title" style="font-size: 36px; margin-bottom: 15px;">Scent <em>Profiler</em></h2>
569:                     <p class="section-sub" style="margin: 0 auto 30px; font-size: 14px; max-width: 80%;">Answer 3 quick questions and let our algorithm select your perfect fragrance match from our luxury library.</p>
570:                     <button class="btn-wa-lg" id="quizStartBtn" style="background: var(--turquoise); color: var(--pure-white); border: none; margin: 0 auto; max-width: 250px;">
571:                         Start Quiz
572:                     </button>
573:                 </div>
574: 
575:                 <!-- Q&A Screen -->
576:                 <div class="quiz-screen" id="quizQnaScreen" style="display: none;">
577:                     <div class="quiz-progress-bar">
578:                         <div class="quiz-progress-fill" id="quizProgressFill"></div>
579:                     </div>
580:                     <div class="quiz-question-tag" id="quizStepText">Question 1 of 3</div>
581:                     <h3 class="quiz-question-title" id="quizQuestionTitle">What is your preference?</h3>
582:                     <div class="quiz-options-grid" id="quizOptionsGrid">
583:                         <!-- Populated by JS -->
584:                     </div>
585:                 </div>
586: 
587:                 <!-- Result Screen -->
588:                 <div class="quiz-screen" id="quizResultScreen" style="display: none;">
589:                     <div class="quiz-icon-header" style="font-size: 40px; color: var(--champagne-gold); margin-bottom: 12px;"><i class="fa-solid fa-award"></i></div>
590:                     <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 28px; margin-bottom: 5px;">Your Perfect Match</h3>
591:                     <p style="color: rgba(17,38,63,0.7); font-size: 14px; margin-bottom: 24px;" id="quizResultReason">Based on your answers, this is the one for you.</p>
592:                     
593:                     <div class="quiz-result-card" id="quizResultCard">
594:                         <!-- Populated by JS -->
595:                     </div>
596: 
597:                     <div style="display: flex; gap: 12px; justify-content: center; margin-top: 24px;">
598:                         <button class="filter-btn" id="quizRetakeBtn" style="background: rgba(17,38,63,0.1); flex: 1;">Retake Quiz</button>
599:                         <button class="btn-wa-lg" id="quizOrderResultBtn" style="flex: 2; padding: 12px 20px; font-size: 14px; background: var(--turquoise); color: var(--pure-white); box-shadow: none; border: none; max-width: none;">Order Match</button>
600:                     </div>
601:                 </div>
602:             </div>
603:         </div>
604:     </div>
605: 
606:     <!-- ===================== 13. PROFILE MODAL ===================== -->
607:     <div class="modal-overlay" id="profileModal">
608:         <div class="modal-box">
609:             <div class="modal-header">
610:                 <h2 class="modal-title">My Profile</h2>
611:                 <button class="modal-close" id="profileCloseBtn" aria-label="Close modal">
612:                     <i class="fa-solid fa-xmark"></i>
613:                 </button>
614:             </div>
615:             
616:             <div style="text-align: center; margin-bottom: 24px; padding-top: 20px;">
617:                 <div style="width: 80px; height: 80px; border-radius: 50%; background: rgba(201,168,76,0.15); border: 2px solid var(--champagne-gold); display: flex; align-items: center; justify-content: center; font-size: 32px; color: var(--champagne-gold); margin: 0 auto 16px;">
618:                     <i class="fa-solid fa-user"></i>
619:                 </div>
620:                 <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 24px;">Guest User</h3>
621:                 <p style="color: rgba(17,38,63,0.7); font-size: 14px;">Welcome to your Velmora Dashboard.</p>
622:             </div>
623: 
624:             <div class="modal-form-group">
625:                 <label>Saved Scent Profile</label>
626:                 <div style="padding: 16px; background: rgba(17,38,63,0.05); border: 1px solid rgba(17,38,63,0.1); border-radius: var(--r-sm); display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
627:                     <i class="fa-solid fa-wand-magic-sparkles" style="color: var(--champagne-gold); font-size: 20px;"></i>
628:                     <div>
629:                         <div style="font-weight: 500; font-size: 14px;">Your Perfect Match</div>
630:                         <div style="font-size: 12px; color: rgba(17,38,63,0.7);">Take the Scent Profiler to uncover your signature scent.</div>
631:                     </div>
632:                 </div>
633:                 <button class="btn-wa-lg" style="width: 100%; background: transparent; border: 1px solid var(--champagne-gold); color: var(--champagne-gold); box-shadow: none;" onclick="document.getElementById('profileCloseBtn').click(); document.getElementById('quizLaunchBtn').click();">
634:                     Retake Scent Quiz
635:                 </button>
636:             </div>
637:             
638:             <div class="modal-form-group" style="margin-top: 20px;">
639:                 <label>Settings</label>
640:                 <div style="font-size: 13px; color: rgba(17,38,63,0.7); text-align: center; padding: 20px; background: rgba(17,38,63,0.05); border-radius: var(--r-sm);">
641:                     Sign in options will be available soon.
642:                 </div>
643:             </div>
644:         </div>
645:     </div>
646: 
647:     <!-- ===================== APP SCRIPT ===================== -->
648: 
649:     <script src="app.js"></script>
650: 
651: </body>
652: 
653: </html>
"""

cleaned = re.sub(r'^\d+:\s', '', content, flags=re.MULTILINE)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(cleaned)
