function isDigit(n) {
    return Boolean([true,true,true,true,true,true,true,true,true,true][n]);
}

class ExprParser{
    constructor(expression) {
        this.count = 0;
        this.expression = expression;
        this.lookahead = this.expression.charAt(0);
        this.postfix = ''
    }

    expr() {
        this.term();
        while(true) {
            if ('+' == this.lookahead) {
                this.match('+');
                this.term();
                this.postfix += '+';
            }   else if('-' == this.lookahead) {
                this.match('-');
                this.term();
                this.postfix += '-';
            }   else {
                return ;
            }
        }
    }

    term() {
        if(isDigit(this.lookahead)) {
            this.postfix += this.lookahead;
            this.match(this.lookahead);
        } else {
            alert("Syntax error, pos: " + this.count);
        }
    }

    match(ch) {
        if(this.lookahead == ch) {
            this.count++;
            this.lookahead = this.expression.charAt(this.count);
        } else {
            alert("Syntax error, pos: " + this.count);
        }
    }
}

class NumParser{
    constructor(expression) {
        this.count = 0;
        this.expression = expression;
        this.lookahead = expression.charAt(0);
        this.isNumber = false;
    }

    /*
        number  ->  op digits
                |   digits
        
        op      ->  + | -
        
        digits  ->  digit digits
                |   digit
        
        digit   ->  0 | 1 | ... | 9
    */

    number() {
        if(this.lookahead == '-' || this.lookahead == '+'){
            this.op();
            this.digits();
        }   else {
            this.digits();
        }
    }

    digits() {
        this.digit();
        while(true) {
            this.digit();
        }
        
    }

    op() {
        if(this.lookahead == '+' || this.lookahead == '-') {
            this.match(this.lookahead);
        } else {
            this.isNumber = false;
            alert("op(): Syntax error, pos: " + this.count);
        }
    }

    digit() {
        if(isDigit(this.lookahead)) {
            this.match(this.lookahead);
        } else {
            this.isNumber = false;
            alert("digit(): Syntax error, pos: " + this.count);
        }
    }
    
    match(ch) {
        if(this.lookahead == ch) {
            this.count++;
            this.lookahead = this.expression.charAt(this.count);
        } else {
            alert("match(): Syntax error, pos: " + this.count);
        }
    }
    
}

function parse() {
    var expr = document.getElementById('exprinput').value;
    var parser = new Parser(expr);
    parser.expr(); 
    document.getElementById('output').innerText = parser.postfix;
}