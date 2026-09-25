from flask import Flask

app = Flask(__name__)


heart_text = "I love you"

# 💌 А здесь пиши свой текст
my_text = """
Алиса, я очень тебя люблю!!!!!
Спасибо тебе за эти прекрасные полгода ❤️
Ты - лучшая девушка на свете, я никогда не перестану это повторять на сколько мне с тобой повезло. Я тебя обожаю!
Я хочу делать с тобой все, и смеяться и плакать. Прости если тебя где-то обидел, то я не со зла.
Я правда тебя очень очень очень сильно люблю, моя хорошая!!
Лучше тебя никого нет, я каждый раз радуюсь как в первый раз когда тебя вижу!!
Любовь моя, хочу провести с тобой еще пол года до года, а потом еще вечность(/≧▽≦)/
"""

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Для Алисы ❤️</title>

    <style>
        body {
            margin: 0;
            min-height: 100vh;
            background: linear-gradient(135deg, #1a1025, #3b183d);
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            overflow: hidden;
        }

        #heart {
            position: relative;
            width: 500px;
            height: 400px;
        }

        .word {
            position: absolute;
            color: #d6336c;
            font-size: 18px;
            font-weight: bold;
            opacity: 0;
            animation: appear 0.8s forwards;
            white-space: nowrap;
        }

        @keyframes appear {
            from {
                opacity: 0;
                transform: scale(0);
            }

            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        #text {
            max-width: 700px;
            text-align: center;
            color: #8b3a52;
            font-size: 23px;
            line-height: 1.6;
            white-space: pre-line;
            margin-top: 20px;
            opacity: 0;
            animation: textAppear 2s forwards;
            animation-delay: 7s;
        }

        @keyframes textAppear {
            from {
                opacity: 0;
            }

            to {
                opacity: 1;
            }
        }
    </style>
</head>

<body>

    <div id="heart"></div>

    <div id="text"></div>

    <script>
        const heart = document.getElementById("heart");
        const text = document.getElementById("text");

        const words = "HEART_TEXT";
        const myText = `MY_TEXT`;

        text.innerText = myText;

        const points = [];

        for (let i = 0; i < 180; i++) {

            let t = Math.PI * 2 * i / 180;

            let x = 16 * Math.pow(Math.sin(t), 3);

            let y = 13 * Math.cos(t)
                  - 5 * Math.cos(2 * t)
                  - 2 * Math.cos(3 * t)
                  - Math.cos(4 * t);

            x = x * 13 + 250;
            y = -y * 13 + 190;

            points.push([x, y]);
        }

        let delay = 0;

        for (let i = 0; i < 180; i++) {

            const word = document.createElement("div");

            word.className = "word";
            word.innerText = words;

            word.style.left = points[i][0] + "px";
            word.style.top = points[i][1] + "px";
            word.style.animationDelay = delay + "s";

            heart.appendChild(word);

            delay += 0.035;
        }
    </script>

</body>
</html>
""".replace("HEART_TEXT", heart_text).replace("MY_TEXT", my_text)


app.run(host="0.0.0.0", port=5000)
