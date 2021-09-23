function navSlide() {
    const burger = document.querySelector(".burger");
    const nav = document.querySelector(".nav-links");
    const navLinks = document.querySelectorAll(".nav-links li");

    burger.addEventListener("click", () => {
        //Toggle Nav
        nav.classList.toggle("nav-active");

        //Animate Links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ""
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
            }
        });
        //Burger Animation
        burger.classList.toggle("toggle");
    });

}
navSlide();
const navBar = document.querySelector('nav');
window.addEventListener("scroll", () => {
    let value = window.scrollY;
    if (value !== 0) {
        navBar.classList.add('bgColor');
    } else {
        navBar.classList.remove('bgColor');
    }
});

// **************************************************************************

console.clear();

const team = [
{
  rank: 1,
  name: 'Shin Chan',
  username: 'shinchan021',
  score: 95,
  time: '20 min' },
{
  rank: 2,
  name: 'Chota Bhim',
  username: 'laddupower',
  score: 91,
  time: '23 min' },
{
  rank: 3,
  name: 'Sijuka',
  username: 'papakipari',
  score: 91,
  time: '25 min' },
{
  rank: 4,
  name: 'Doremi',
  username: 'its_doremi',
  score: 90,
  time: '25 min' },
{
  rank: 5,
  name: 'Ramta Jogi',
  username: 'jogi_jogi',
  score: 88,
  time: '24 min'},
{
  rank: 6,
  name: 'Pushpa',
  username: 'i_hate_tears',
  score: 86,
  time: '22 min' },
{
  rank: 7,
  name: 'Ben_10',
  username: 'omniverse',
  score: 81,
  time: '21 min'}];




team.forEach(member => {
  let newRow = document.createElement('li');
  newRow.classList = 'c-list__item';
  newRow.innerHTML = `
		<div class="c-list__grid">
			<div class="c-flag c-place u-bg--transparent">${member.rank}</div>
			<div class="c-media">
				<div class="c-media__content">
					<div class="c-media__title">${member.name}</div>
					<span class="c-media__link u-text--small">@${member.username}</span>
				</div>
			</div>
			<div class="u-text--right c-score">
				<div class="u-mt--8">
					<strong>${member.score}</strong>
				</div>
			</div>
            <div class="u-text--right ">
				<div class="u-mt--8">
					<strong>${member.time}</strong>
				</div>
			</div>
		</div>
	`;
  if (member.rank === 1) {
    newRow.querySelector('.c-place').classList.add('u-text--dark');
    newRow.querySelector('.c-place').classList.add('u-bg--neon');
    newRow.querySelector('.c-score').classList.add('u-text--neon');
  } else if (member.rank === 2) {
    newRow.querySelector('.c-place').classList.add('u-text--dark');
    newRow.querySelector('.c-place').classList.add('u-bg--teal');
    newRow.querySelector('.c-score').classList.add('u-text--teal');
  } else if (member.rank === 3) {
    newRow.querySelector('.c-place').classList.add('u-text--dark');
    newRow.querySelector('.c-place').classList.add('u-bg--gold');
    newRow.querySelector('.c-score').classList.add('u-text--gold');
  }
  list.appendChild(newRow);
});



