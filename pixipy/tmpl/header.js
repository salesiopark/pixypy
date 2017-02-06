// contents in header file ================================
class Text {
    constructor(text, x, y, font_size) {
        let style = new PIXI.TextStyle({
            fontFamily: 'Arial',
            fontSize: font_size,
            fontStyle: 'normal',//'normal', 'italic' or 'oblique'
            fontWeight: 'normal',//'normal', 'bold', 'bolder', 'lighter'
            fill: ['#ffffff', '#ccff99'], // gradient
            //stroke: '#FFFFFF',
            //strokeThickness: 1,
        });

        this.body = new PIXI.Text(text, style);
        this.body.x = x;
        this.body.y = y;
        this.body.anchor.set(0.5);//중심점을 원점으로
        
        app.stage.addChild(this.body);
    }

    get x() {return this.body.x;}
    set x(v) {this.body.x=v;}

    get y() {return this.body.y;}
    set y(v) {this.body.y=v;}

    get text() {return this.body.text;}
    set text(v) {this.body.text=v;}

    get font_size() {return this.body.style.fontSize;}
    set font_size(v) {this.body.style.fontSize=v;}
}
//======================================================================
class Button {
    constructor(name, text, x, y, width, height, font_size) {
        this.name = name;
        
        this.body = new PIXI.Container();
        this.body.x = x;
        this.body.y = y;
        //사각형 그리기
        this.box = new PIXI.Graphics();
        this.box.lineStyle(2, 0xbbff33, 1);//외곽선 스타일
        this.box.beginFill(0x99e600, 1);//채우기
        this.box.drawRoundedRect(-width/2, -height/2, width, height, 10);
        this.box.endFill();
        this.body.addChild(this.box);
        // 라벨 쓰기
        let textStyle = new PIXI.TextStyle({
            fontFamily: 'Arial',
            fontSize: font_size,
            fill: '#ffffff', // gradient
            //stroke: '#FF0000',
            //strokeThickness: 1,
        });
        this.label = new PIXI.Text(text, textStyle);
        this.label.anchor.set(0.5);
        this.body.addChild(this.label);

        //onClick, onRelease 함수 내에서는 this 가 인식이 안된다.(왜지?)
        //그래서 self라는 변수에 따로 this를 저장하면 이건 인식이 됨.
        let self = this;
        let onClick = function() {
            console.log(text+' down');
            self.body.scale.x = 0.97;
            self.body.scale.y = 0.97;
            $.getJSON($SCRIPT_ROOT+'/event',
                {obj:self.name},
                function(data) {
                  console.log(data);
                }
            )
        }
        
        let onRelease = function() {
          console.log(text+' up');
          self.body.scale.x = 1;
          self.body.scale.y = 1;
        }
        //touch 나 mouseclick 둘 다에 반응함
        this.body.interactive = true;// Opt-in to interactivity
        this.body.on('pointerdown', onClick);
        this.body.on('pointerup', onRelease);
        this.body.on('pointerupoutside', onRelease);

        app.stage.addChild(this.body);
    }//constructor()

    get x() {return this.body.x;}
    set x(v) {this.body.x=v;}

    get y() {return this.body.y;}
    set y(v) {this.body.y=v;}

    get text() {return this.label.text;}
    set text(v) {this.label.text=v;}
}// class Button

// end of header file ======================================
