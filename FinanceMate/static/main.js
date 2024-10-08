function leftScroll() {
    var w = window.innerWidth;
    var left = document.querySelector(".courese-cards");
    if(w<576){
      left.scrollBy(-290, 0);
    }
    else{
      left.scrollBy(-369, 0);
    }
  }
  function rightScroll() {
    var w = window.innerWidth;
    var left = document.querySelector(".courese-cards");
    if(w<576){
      left.scrollBy(290, 0);
    }
    else{
      left.scrollBy(369, 0);
    }
  }
  function leftScroll2() {
    const left = document.querySelector(".student-container");
    left.scrollBy(-265, 0);
  }
  function rightScroll2() {
    const right = document.querySelector(".student-container");
    right.scrollBy(265, 0);
  }

  function toggle(){
    const listtoggele=document.getElementById('list');
    const close=document.getElementById('close');
    listtoggele.style.right='0%';
    close.style.display='inline-block';
    listtoggele.style.display='flex';
    listtoggele.style.position='fixed';
  }
  function untoggle(){
    const listtoggele=document.getElementById('list');
    listtoggele.style.right='-110%';

  }

  ScrollReveal({ reset: true });

  ScrollReveal().reveal('.page1', { delay: 250,origin:'bottom',distance:'100px' });