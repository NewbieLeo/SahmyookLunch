const axios = require('axios');
const cheerio = require('cheerio');

async function main() {
  // 완전히 불러온 후 실행하기 위해 await 사용
  const resp = await axios.get(
    'https://school.gyo6.net/yn36ms/070501/food'
  );

  const $ = cheerio.load(resp.data); // HTML 파싱 과정
  const elements = $('.diet_box .menu'); // CSS 선택자 사용

  elements.each((i, e) => {
    let menu = $(e).html().split('<br>');
    // $(e).html() format -> 'menu1<br>menu2<br>menu3 ...', 따라서 split 함수 사용

    menu.forEach((v, i) => {
      console.log(v.replaceAll('&amp;', '&').replaceAll('  ', ' ')); // 출력 정제
    }); 
    console.log(i, '-----------------') // debug
  });
}

main();