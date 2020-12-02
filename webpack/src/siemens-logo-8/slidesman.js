import {default as sh} from './stringhelper';

export default class SlidesManager {
    constructor(controlman) {
        this.controlman = controlman;
        this.firstTime = true;
        this.offset = 0;
        this.carousel = $('#slidesCarousel');
        // this.positions = params.positions;
        this.carousel.carousel({
            interval: false, //4500,
            keyboard: true,
            ride: true,
        });
        this.carousel.on('slide.bs.carousel', (e) => {
            const to = e.to + this.offset;
            // console.log(to);
            const position = sh.toVector3(annotations[to].camPosition);
            const target = sh.toVector3(annotations[to].position);          
            this.controlman.setTarget(target);
            this.controlman.setPosition(position);                  
            // TODO: Maybe this breaks in somepoint
            if (this.firstTime){
                this.removeWelcome();
            }           
        });
    }
    prev() {
        this.carousel.carousel('prev');
    }
    next() {
        this.carousel.carousel('next');
    }
    goto(index) {
        const to = index - this.offset;
        this.carousel.carousel(to);
    }
    removeWelcome() {
        document.getElementById('welcome').remove();
        this.firstTime = false;
        this.offset = 1;
    }
}