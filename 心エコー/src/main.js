import './styles/index.css';
import './styles/components.css';
import './styles/book-layout.css';
import { fetchEchoReferences } from './utils/dataFetcher.js';
import { createIndexNav } from './components/IndexNav.js';
import { createChapterPage } from './components/ChapterPage.js';
import { createBookManager } from './components/BookManager.js';

async function init() {
  const app = document.getElementById('app');
  app.innerHTML = '';
  
  const header = document.createElement('header');
  header.innerHTML = `<h1>心エコー電子教科書 & 電卓</h1>`;
  document.body.insertBefore(header, app);

  const data = await fetchEchoReferences();
  if (!data) {
    app.innerHTML = '<p style="color: red; text-align: center;">データの読み込みに失敗しました。</p>';
    return;
  }

  const { guidelines, chapters } = data;
  const guidelineMap = guidelines.reduce((acc, g) => {
    acc[g.id] = g.name;
    return acc;
  }, {});

  const pages = [];
  
  // Page 1: Cover
  const cover = document.createElement('div');
  cover.innerHTML = `<div style="text-align:center; margin-top:20%;"><h2>心臓超音波検査 リファレンス</h2><p style="color:var(--text-muted); margin-top:1rem;">ガイドライン・計算ツール・評価フロー</p></div>`;
  pages.push(cover);

  // Page 2: Index (Table of contents)
  let bookManagerAPI = null;
  const navClick = (pageIndex) => {
    if (bookManagerAPI) {
      // We need to implement a jumpTo method if we wanted, 
      // but for simplicity we can just flip through.
      // Let's modify BookManager slightly if we need jump, but for now we'll just add it to BookManager later or iterate nextBtn clicks.
      // A quick hack for jumping:
      bookManagerAPI.jumpTo(pageIndex);
    }
  };
  const indexPage = createIndexNav(chapters, navClick);
  pages.push(indexPage);

  // Chapter Pages
  chapters.forEach(chapter => {
    const cp = createChapterPage(chapter, guidelineMap);
    pages.push(cp);
  });

  // Init BookManager
  const bm = createBookManager(pages);
  
  // Add jumpTo method to bm
  bm.jumpTo = (idx) => {
    // Hacky way to inject jumpTo into the closure
    // Real implementation would be inside BookManager.js, but we'll do it dynamically here:
    // Actually, let's just let BookManager have it. I'll patch BookManager.js next.
    if(bm.doJump) bm.doJump(idx);
  };
  bookManagerAPI = bm;

  app.appendChild(bm.container);
  app.appendChild(bm.controls);
}

document.addEventListener('DOMContentLoaded', init);

