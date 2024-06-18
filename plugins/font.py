class Fonts:
    def typewriter(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
        )
        return text.translate(trans_table)

    def outline(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 
            "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"
        )
        return text.translate(trans_table)

    def serief(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 
            "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
        )
        return text.translate(trans_table)

    def bold_cool(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁"
        )
        return text.translate(trans_table)

    def cool(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍"
        )
        return text.translate(trans_table)

    def smallcap(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 
            "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ0𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
        )
        return text.translate(trans_table)

    def script(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"
        )
        return text.translate(trans_table)

    def bold_script(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩"
        )
        return text.translate(trans_table)

    def tiny(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ"
        )
        return text.translate(trans_table)

    def comic(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "ᗩᗷᑕᗪᗴᖴᘜᕼIᒍKᒪᗰᑎOᑭᑫᖇՏTᑌᐯᗯ᙭YᘔᗩᗷᑕᗪᗴᖴᘜᕼIᒍKᒪᗰᑎOᑭᑫᖇՏTᑌᐯᗯ᙭Yᘔ"
        )
        return text.translate(trans_table)

    def san(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 
            "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
        )
        return text.translate(trans_table)

    def slant_san(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"
        )
        return text.translate(trans_table)

    def slant(text):
        
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡"
        )
        return text.translate(trans_table)

    def sim(text):
       
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹"
        )
        return text.translate(trans_table)

    def circles(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 
            "Ⓐ︎Ⓑ︎Ⓒ︎Ⓓ︎Ⓔ︎Ⓕ︎Ⓖ︎Ⓗ︎Ⓘ︎Ⓙ︎Ⓚ︎Ⓛ︎Ⓜ︎Ⓝ︎Ⓞ︎Ⓟ︎Ⓠ︎Ⓡ︎Ⓢ︎Ⓣ︎Ⓤ︎Ⓥ︎Ⓦ︎Ⓧ︎Ⓨ︎Ⓩ︎Ⓐ︎Ⓑ︎Ⓒ︎Ⓓ︎Ⓔ︎Ⓕ︎Ⓖ︎Ⓗ︎Ⓘ︎Ⓙ︎Ⓚ︎Ⓛ︎Ⓜ︎Ⓝ︎Ⓞ︎Ⓟ︎Ⓠ︎Ⓡ︎Ⓢ︎Ⓣ︎Ⓤ︎Ⓥ︎Ⓦ︎Ⓧ︎Ⓨ︎Ⓩ︎⓪①②③④⑤⑥⑦⑧⑨"
        )
        return text.translate(trans_table)

    def dark_circle(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890", 
            "🅐︎🅑︎🅒︎🅓︎🅔︎🅕︎🅖︎🅗︎🅘︎🅙︎🅚︎🅛︎🅜︎🅝︎🅞︎🅟︎🅠︎🅡︎🅢︎🅣︎🅤︎🅥︎🅦︎🅧︎🅨︎🅩︎🅐︎🅑︎🅒︎🅓︎🅔︎🅕︎🅖︎🅗︎🅘︎🅙︎🅚︎🅛︎🅜︎🅝︎🅞︎🅟︎🅠︎🅡︎🅢︎🅣︎🅤︎🅥︎🅦︎🅧︎🅨︎🅩⓿➊➋➌➍➎➏➐➑➒"
        )
        return text.translate(trans_table)

    def gothic(text):
        trans_table = str.maketrans(
             "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ"
        )
        return text.translate(trans_table)
    def gothic(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔸𝔹ℭ𝔻𝔼𝔽𝔾ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ"
        )
        return text.translate(trans_table)
    def cloud(text):
        trans_table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            "a͜͡b͜͡c͜͡d͜͡e͜͡f͜͡g͜͡h͜͡i͜͡j͜͡k͜͡l͜͡m͜͡n͜͡o͜͡p͜͡q͜͡r͜͡s͜͡t͜͡u͜͡v͜͡w͜͡x͜͡y͜͡z͜͡A͜͡B͜͡C͜͡D͜͡E͜͡F͜͡G͜͡H͜͡I͜͡J͜͡K͜͡L͜͡M͜͡N͜͡O͜͡P͜͡Q͜͡R͜͡S͜͡T͜͡U͜͡V͜͡W͜͡X͜͡Y͜͡Z͜͡"
        )
        return text.translate(trans_table)

    def happy(text):
        style = {
            "a": "ă̈",
            "b": "b̆̈",
            "c": "c̆̈",
            "d": "d̆̈",
            "e": "ĕ̈",
            "f": "f̆̈",
            "g": "ğ̈",
            "h": "h̆̈",
            "i": "ĭ̈",
            "j": "j̆̈",
            "k": "k̆̈",
            "l": "l̆̈",
            "m": "m̆̈",
            "n": "n̆̈",
            "o": "ŏ̈",
            "p": "p̆̈",
            "q": "q̆̈",
            "r": "r̆̈",
            "s": "s̆̈",
            "t": "t̆̈",
            "u": "ŭ̈",
            "v": "v̆̈",
            "w": "w̆̈",
            "x": "x̆̈",
            "y": "y̆̈",
            "z": "z̆̈",
            "A": "Ă̈",
            "B": "B̆̈",
            "C": "C̆̈",
            "D": "D̆̈",
            "E": "Ĕ̈",
            "F": "F̆̈",
            "G": "Ğ̈",
            "H": "H̆̈",
            "I": "Ĭ̈",
            "J": "J̆̈",
            "K": "K̆̈",
            "L": "L̆̈",
            "M": "M̆̈",
            "N": "N̆̈",
            "O": "Ŏ̈",
            "P": "P̆̈",
            "Q": "Q̆̈",
            "R": "R̆̈",
            "S": "S̆̈",
            "T": "T̆̈",
            "U": "Ŭ̈",
            "V": "V̆̈",
            "W": "W̆̈",
            "X": "X̆̈",
            "Y": "Y̆̈",
            "Z": "Z̆̈",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def sad(text):
        style = {
            "a": "ȃ̈",
            "b": "b̑̈",
            "c": "c̑̈",
            "d": "d̑̈",
            "e": "ȇ̈",
            "f": "f̑̈",
            "g": "g̑̈",
            "h": "h̑̈",
            "i": "ȋ̈",
            "j": "j̑̈",
            "k": "k̑̈",
            "l": "l̑̈",
            "m": "m̑̈",
            "n": "n̑̈",
            "o": "ȏ̈",
            "p": "p̑̈",
            "q": "q̑̈",
            "r": "ȓ̈",
            "s": "s̑̈",
            "t": "t̑̈",
            "u": "ȗ̈",
            "v": "v̑̈",
            "w": "w̑̈",
            "x": "x̑̈",
            "y": "y̑̈",
            "z": "z̑̈",
            "A": "Ȃ̈",
            "B": "B̑̈",
            "C": "C̑̈",
            "D": "D̑̈",
            "E": "Ȇ̈",
            "F": "F̑̈",
            "G": "G̑̈",
            "H": "H̑̈",
            "I": "Ȋ̈",
            "J": "J̑̈",
            "K": "K̑̈",
            "L": "L̑̈",
            "M": "M̑̈",
            "N": "N̑̈",
            "O": "Ȏ̈",
            "P": "P̑̈",
            "Q": "Q̑̈",
            "R": "Ȓ̈",
            "S": "S̑̈",
            "T": "T̑̈",
            "U": "Ȗ̈",
            "V": "V̑̈",
            "W": "W̑̈",
            "X": "X̑̈",
            "Y": "Y̑̈",
            "Z": "Z̑̈",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def special(text):
        style = {
            "a": "🇦 ",
            "b": "🇧 ",
            "c": "🇨 ",
            "d": "🇩 ",
            "e": "🇪 ",
            "f": "🇫 ",
            "g": "🇬 ",
            "h": "🇭 ",
            "i": "🇮 ",
            "j": "🇯 ",
            "k": "🇰 ",
            "l": "🇱 ",
            "m": "🇲 ",
            "n": "🇳 ",
            "o": "🇴 ",
            "p": "🇵 ",
            "q": "🇶 ",
            "r": "🇷 ",
            "s": "🇸 ",
            "t": "🇹 ",
            "u": "🇺 ",
            "v": "🇻 ",
            "w": "🇼 ",
            "x": "🇽 ",
            "y": "🇾 ",
            "z": "🇿 ",
            "A": "🇦 ",
            "B": "🇧 ",
            "C": "🇨 ",
            "D": "🇩 ",
            "E": "🇪 ",
            "F": "🇫 ",
            "G": "🇬 ",
            "H": "🇭 ",
            "I": "🇮 ",
            "J": "🇯 ",
            "K": "🇰 ",
            "L": "🇱 ",
            "M": "🇲 ",
            "N": "🇳 ",
            "O": "🇴 ",
            "P": "🇵 ",
            "Q": "🇶 ",
            "R": "🇷 ",
            "S": "🇸 ",
            "T": "🇹 ",
            "U": "🇺 ",
            "V": "🇻 ",
            "W": "🇼 ",
            "X": "🇽 ",
            "Y": "🇾 ",
            "Z": "🇿 ",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def square(text):
        style = {
            "a": "🄰",
            "b": "🄱",
            "c": "🄲",
            "d": "🄳",
            "e": "🄴",
            "f": "🄵",
            "g": "🄶",
            "h": "🄷",
            "i": "🄸",
            "j": "🄹",
            "k": "🄺",
            "l": "🄻",
            "m": "🄼",
            "n": "🄽",
            "o": "🄾",
            "p": "🄿",
            "q": "🅀",
            "r": "🅁",
            "s": "🅂",
            "t": "🅃",
            "u": "🅄",
            "v": "🅅",
            "w": "🅆",
            "x": "🅇",
            "y": "🅈",
            "z": "🅉",
            "A": "🄰",
            "B": "🄱",
            "C": "🄲",
            "D": "🄳",
            "E": "🄴",
            "F": "🄵",
            "G": "🄶",
            "H": "🄷",
            "I": "🄸",
            "J": "🄹",
            "K": "🄺",
            "L": "🄻",
            "M": "🄼",
            "N": "🄽",
            "O": "🄾",
            "P": "🄿",
            "Q": "🅀",
            "R": "🅁",
            "S": "🅂",
            "T": "🅃",
            "U": "🅄",
            "V": "🅅",
            "W": "🅆",
            "X": "🅇",
            "Y": "🅈",
            "Z": "🅉",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def dark_square(text):
        style = {
            "a": "🅰︎",
            "b": "🅱︎",
            "c": "🅲︎",
            "d": "🅳︎",
            "e": "🅴︎",
            "f": "🅵︎",
            "g": "🅶︎",
            "h": "🅷︎",
            "i": "🅸︎",
            "j": "🅹︎",
            "k": "🅺︎",
            "l": "🅻︎",
            "m": "🅼︎",
            "n": "🅽︎",
            "o": "🅾︎",
            "p": "🅿︎",
            "q": "🆀︎",
            "r": "🆁︎",
            "s": "🆂︎",
            "t": "🆃︎",
            "u": "🆄︎",
            "v": "🆅︎",
            "w": "🆆︎",
            "x": "🆇︎",
            "y": "🆈︎",
            "z": "🆉︎",
            "A": "🅰︎",
            "B": "🅱︎",
            "C": "🅲︎",
            "D": "🅳︎",
            "E": "🅴︎",
            "F": "🅵︎",
            "G": "🅶︎",
            "H": "🅷︎",
            "I": "🅸︎",
            "J": "🅹︎",
            "K": "🅺︎",
            "L": "🅻︎",
            "M": "🅼︎",
            "N": "🅽︎",
            "O": "🅾︎",
            "P": "🅿︎",
            "Q": "🆀︎",
            "R": "🆁︎",
            "S": "🆂︎",
            "T": "🆃︎",
            "U": "🆄︎",
            "V": "🆅︎",
            "W": "🆆︎",
            "X": "🆇︎",
            "Y": "🆈︎",
            "Z": "🆉︎",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def andalucia(text):
        style = {
            "a": "ꪖ",
            "b": "᥇",
            "c": "ᥴ",
            "d": "ᦔ",
            "e": "ꫀ",
            "f": "ᠻ",
            "g": "ᧁ",
            "h": "ꫝ",
            "i": "𝓲",
            "j": "𝓳",
            "k": "𝘬",
            "l": "ꪶ",
            "m": "ꪑ",
            "n": "ꪀ",
            "o": "ꪮ",
            "p": "ρ",
            "q": "𝘲",
            "r": "𝘳",
            "s": "𝘴",
            "t": "𝓽",
            "u": "ꪊ",
            "v": "ꪜ",
            "w": "᭙",
            "x": "᥊",
            "y": "ꪗ",
            "z": "ɀ",
            "A": "ꪖ",
            "B": "᥇",
            "C": "ᥴ",
            "D": "ᦔ",
            "E": "ꫀ",
            "F": "ᠻ",
            "G": "ᧁ",
            "H": "ꫝ",
            "I": "𝓲",
            "J": "𝓳",
            "K": "𝘬",
            "L": "ꪶ",
            "M": "ꪑ",
            "N": "ꪀ",
            "O": "ꪮ",
            "P": "ρ",
            "Q": "𝘲",
            "R": "𝘳",
            "S": "𝘴",
            "T": "𝓽",
            "U": "ꪊ",
            "V": "ꪜ",
            "W": "᭙",
            "X": "᥊",
            "Y": "ꪗ",
            "Z": "ɀ",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def manga(text):
        style = {
            "a": "卂",
            "b": "乃",
            "c": "匚",
            "d": "ᗪ",
            "e": "乇",
            "f": "千",
            "g": "ᘜ",
            "h": "卄",
            "i": "|",
            "j": "ﾌ",
            "k": "Ҝ",
            "l": "ㄥ",
            "m": "爪",
            "n": "几",
            "o": "ㄖ",
            "p": "卩",
            "q": "Ҩ",
            "r": "尺",
            "s": "丂",
            "t": "ㄒ",
            "u": "ㄩ",
            "v": "ᐯ",
            "w": "山",
            "x": "乂",
            "y": "ㄚ",
            "z": "乙",
            "A": "卂",
            "B": "乃",
            "C": "匚",
            "D": "ᗪ",
            "E": "乇",
            "F": "千",
            "G": "ᘜ",
            "H": "卄",
            "I": "|",
            "J": "ﾌ",
            "K": "Ҝ",
            "L": "ㄥ",
            "M": "爪",
            "N": "几",
            "O": "ㄖ",
            "P": "卩",
            "Q": "Ҩ",
            "R": "尺",
            "S": "丂",
            "T": "ㄒ",
            "U": "ㄩ",
            "V": "ᐯ",
            "W": "山",
            "X": "乂",
            "Y": "ㄚ",
            "Z": "乙",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def stinky(text):
        style = {
            "a": "a̾",
            "b": "b̾",
            "c": "c̾",
            "d": "d̾",
            "e": "e̾",
            "f": "f̾",
            "g": "g̾",
            "h": "h̾",
            "i": "i̾",
            "j": "j̾",
            "k": "k̾",
            "l": "l̾",
            "m": "m̾",
            "n": "n̾",
            "o": "o̾",
            "p": "p̾",
            "q": "q̾",
            "r": "r̾",
            "s": "s̾",
            "t": "t̾",
            "u": "u̾",
            "v": "v̾",
            "w": "w̾",
            "x": "x̾",
            "y": "y̾",
            "z": "z̾",
            "A": "A̾",
            "B": "B̾",
            "C": "C̾",
            "D": "D̾",
            "E": "E̾",
            "F": "F̾",
            "G": "G̾",
            "H": "H̾",
            "I": "I̾",
            "J": "J̾",
            "K": "K̾",
            "L": "L̾",
            "M": "M̾",
            "N": "N̾",
            "O": "O̾",
            "P": "P̾",
            "Q": "Q̾",
            "R": "R̾",
            "S": "S̾",
            "T": "T̾",
            "U": "U̾",
            "V": "V̾",
            "W": "W̾",
            "X": "X̾",
            "Y": "Y̾",
            "Z": "Z̾",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def bubbles(text):
        style = {
            "a": "ḁͦ",
            "b": "b̥ͦ",
            "c": "c̥ͦ",
            "d": "d̥ͦ",
            "e": "e̥ͦ",
            "f": "f̥ͦ",
            "g": "g̥ͦ",
            "h": "h̥ͦ",
            "i": "i̥ͦ",
            "j": "j̥ͦ",
            "k": "k̥ͦ",
            "l": "l̥ͦ",
            "m": "m̥ͦ",
            "n": "n̥ͦ",
            "o": "o̥ͦ",
            "p": "p̥ͦ",
            "q": "q̥ͦ",
            "r": "r̥ͦ",
            "s": "s̥ͦ",
            "t": "t̥ͦ",
            "u": "u̥ͦ",
            "v": "v̥ͦ",
            "w": "w̥ͦ",
            "x": "x̥ͦ",
            "y": "y̥ͦ",
            "z": "z̥ͦ",
            "A": "Ḁͦ",
            "B": "B̥ͦ",
            "C": "C̥ͦ",
            "D": "D̥ͦ",
            "E": "E̥ͦ",
            "F": "F̥ͦ",
            "G": "G̥ͦ",
            "H": "H̥ͦ",
            "I": "I̥ͦ",
            "J": "J̥ͦ",
            "K": "K̥ͦ",
            "L": "L̥ͦ",
            "M": "M̥ͦ",
            "N": "N̥ͦ",
            "O": "O̥ͦ",
            "P": "P̥ͦ",
            "Q": "Q̥ͦ",
            "R": "R̥ͦ",
            "S": "S̥ͦ",
            "T": "T̥ͦ",
            "U": "U̥ͦ",
            "V": "V̥ͦ",
            "W": "W̥ͦ",
            "X": "X̥ͦ",
            "Y": "Y̥ͦ",
            "Z": "Z̥ͦ",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def underline(text):
        style = {
            "a": "a͟",
            "b": "b͟",
            "c": "c͟",
            "d": "d͟",
            "e": "e͟",
            "f": "f͟",
            "g": "g͟",
            "h": "h͟",
            "i": "i͟",
            "j": "j͟",
            "k": "k͟",
            "l": "l͟",
            "m": "m͟",
            "n": "n͟",
            "o": "o͟",
            "p": "p͟",
            "q": "q͟",
            "r": "r͟",
            "s": "s͟",
            "t": "t͟",
            "u": "u͟",
            "v": "v͟",
            "w": "w͟",
            "x": "x͟",
            "y": "y͟",
            "z": "z͟",
            "A": "A͟",
            "B": "B͟",
            "C": "C͟",
            "D": "D͟",
            "E": "E͟",
            "F": "F͟",
            "G": "G͟",
            "H": "H͟",
            "I": "I͟",
            "J": "J͟",
            "K": "K͟",
            "L": "L͟",
            "M": "M͟",
            "N": "N͟",
            "O": "O͟",
            "P": "P͟",
            "Q": "Q͟",
            "R": "R͟",
            "S": "S͟",
            "T": "T͟",
            "U": "U͟",
            "V": "V͟",
            "W": "W͟",
            "X": "X͟",
            "Y": "Y͟",
            "Z": "Z͟",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def ladybug(text):
        style = {
            "a": "ꍏ",
            "b": "ꌃ",
            "c": "ꏳ",
            "d": "ꀷ",
            "e": "ꏂ",
            "f": "ꎇ",
            "g": "ꁅ",
            "h": "ꀍ",
            "i": "ꀤ",
            "j": "꒻",
            "k": "ꀘ",
            "l": "꒒",
            "m": "ꎭ",
            "n": "ꈤ",
            "o": "ꂦ",
            "p": "ᖘ",
            "q": "ꆰ",
            "r": "ꋪ",
            "s": "ꌚ",
            "t": "꓄",
            "u": "ꀎ",
            "v": "꒦",
            "w": "ꅐ",
            "x": "ꉧ",
            "y": "ꌩ",
            "z": "ꁴ",
            "A": "ꍏ",
            "B": "ꌃ",
            "C": "ꏳ",
            "D": "ꀷ",
            "E": "ꏂ",
            "F": "ꎇ",
            "G": "ꁅ",
            "H": "ꀍ",
            "I": "ꀤ",
            "J": "꒻",
            "K": "ꀘ",
            "L": "꒒",
            "M": "ꎭ",
            "N": "ꈤ",
            "O": "ꂦ",
            "P": "ᖘ",
            "Q": "ꆰ",
            "R": "ꋪ",
            "S": "ꌚ",
            "T": "꓄",
            "U": "ꀎ",
            "V": "꒦",
            "W": "ꅐ",
            "X": "ꉧ",
            "Y": "ꌩ",
            "Z": "ꁴ",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def rays(text):
        style = {
            "a": "a҉",
            "b": "b҉",
            "c": "c҉",
            "d": "d҉",
            "e": "e҉",
            "f": "f҉",
            "g": "g҉",
            "h": "h҉",
            "i": "i҉",
            "j": "j҉",
            "k": "k҉",
            "l": "l҉",
            "m": "m҉",
            "n": "n҉",
            "o": "o҉",
            "p": "p҉",
            "q": "q҉",
            "r": "r҉",
            "s": "s҉",
            "t": "t҉",
            "u": "u҉",
            "v": "v҉",
            "w": "w҉",
            "x": "x҉",
            "y": "y҉",
            "z": "z҉",
            "A": "A҉",
            "B": "B҉",
            "C": "C҉",
            "D": "D҉",
            "E": "E҉",
            "F": "F҉",
            "G": "G҉",
            "H": "H҉",
            "I": "I҉",
            "J": "J҉",
            "K": "K҉",
            "L": "L҉",
            "M": "M҉",
            "N": "N҉",
            "O": "O҉",
            "P": "P҉",
            "Q": "Q҉",
            "R": "R҉",
            "S": "S҉",
            "T": "T҉",
            "U": "U҉",
            "V": "V҉",
            "W": "W҉",
            "X": "X҉",
            "Y": "Y҉",
            "Z": "Z҉",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def birds(text):
        style = {
            "a": "a҈",
            "b": "b҈",
            "c": "c҈",
            "d": "d҈",
            "e": "e҈",
            "f": "f҈",
            "g": "g҈",
            "h": "h҈",
            "i": "i҈",
            "j": "j҈",
            "k": "k҈",
            "l": "l҈",
            "m": "m҈",
            "n": "n҈",
            "o": "o҈",
            "p": "p҈",
            "q": "q҈",
            "r": "r҈",
            "s": "s҈",
            "t": "t҈",
            "u": "u҈",
            "v": "v҈",
            "w": "w҈",
            "x": "x҈",
            "y": "y҈",
            "z": "z҈",
            "A": "A҈",
            "B": "B҈",
            "C": "C҈",
            "D": "D҈",
            "E": "E҈",
            "F": "F҈",
            "G": "G҈",
            "H": "H҈",
            "I": "I҈",
            "J": "J҈",
            "K": "K҈",
            "L": "L҈",
            "M": "M҈",
            "N": "N҈",
            "O": "O҈",
            "P": "P҈",
            "Q": "Q҈",
            "R": "R҈",
            "S": "S҈",
            "T": "T҈",
            "U": "U҈",
            "V": "V҈",
            "W": "W҈",
            "X": "X҈",
            "Y": "Y҈",
            "Z": "Z҈",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def slash(text):
        style = {
            "a": "a̸",
            "b": "b̸",
            "c": "c̸",
            "d": "d̸",
            "e": "e̸",
            "f": "f̸",
            "g": "g̸",
            "h": "h̸",
            "i": "i̸",
            "j": "j̸",
            "k": "k̸",
            "l": "l̸",
            "m": "m̸",
            "n": "n̸",
            "o": "o̸",
            "p": "p̸",
            "q": "q̸",
            "r": "r̸",
            "s": "s̸",
            "t": "t̸",
            "u": "u̸",
            "v": "v̸",
            "w": "w̸",
            "x": "x̸",
            "y": "y̸",
            "z": "z̸",
            "A": "A̸",
            "B": "B̸",
            "C": "C̸",
            "D": "D̸",
            "E": "E̸",
            "F": "F̸",
            "G": "G̸",
            "H": "H̸",
            "I": "I̸",
            "J": "J̸",
            "K": "K̸",
            "L": "L̸",
            "M": "M̸",
            "N": "N̸",
            "O": "O̸",
            "P": "P̸",
            "Q": "Q̸",
            "R": "R̸",
            "S": "S̸",
            "T": "T̸",
            "U": "U̸",
            "V": "V̸",
            "W": "W̸",
            "X": "X̸",
            "Y": "Y̸",
            "Z": "Z̸",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def stop(text):
        style = {
            "a": "a⃠",
            "b": "b⃠",
            "c": "c⃠",
            "d": "d⃠",
            "e": "e⃠",
            "f": "f⃠",
            "g": "g⃠",
            "h": "h⃠",
            "i": "i⃠",
            "j": "j⃠",
            "k": "k⃠",
            "l": "l⃠",
            "m": "m⃠",
            "n": "n⃠",
            "o": "o⃠",
            "p": "p⃠",
            "q": "q⃠",
            "r": "r⃠",
            "s": "s⃠",
            "t": "t⃠",
            "u": "u⃠",
            "v": "v⃠",
            "w": "w⃠",
            "x": "x⃠",
            "y": "y⃠",
            "z": "z⃠",
            "A": "A⃠",
            "B": "B⃠",
            "C": "C⃠",
            "D": "D⃠",
            "E": "E⃠",
            "F": "F⃠",
            "G": "G⃠",
            "H": "H⃠",
            "I": "I⃠",
            "J": "J⃠",
            "K": "K⃠",
            "L": "L⃠",
            "M": "M⃠",
            "N": "N⃠",
            "O": "O⃠",
            "P": "P⃠",
            "Q": "Q⃠",
            "R": "R⃠",
            "S": "S⃠",
            "T": "T⃠",
            "U": "U⃠",
            "V": "V⃠",
            "W": "W⃠",
            "X": "X⃠",
            "Y": "Y⃠",
            "Z": "Z⃠",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def skyline(text):
        style = {
            "a": "a̺͆",
            "b": "b̺͆",
            "c": "c̺͆",
            "d": "d̺͆",
            "e": "e̺͆",
            "f": "f̺͆",
            "g": "g̺͆",
            "h": "h̺͆",
            "i": "i̺͆",
            "j": "j̺͆",
            "k": "k̺͆",
            "l": "l̺͆",
            "m": "m̺͆",
            "n": "n̺͆",
            "o": "o̺͆",
            "p": "p̺͆",
            "q": "q̺͆",
            "r": "r̺͆",
            "s": "s̺͆",
            "t": "t̺͆",
            "u": "u̺͆",
            "v": "v̺͆",
            "w": "w̺͆",
            "x": "x̺͆",
            "y": "y̺͆",
            "z": "z̺͆",
            "A": "A̺͆",
            "B": "B̺͆",
            "C": "C̺͆",
            "D": "D̺͆",
            "E": "E̺͆",
            "F": "F̺͆",
            "G": "G̺͆",
            "H": "H̺͆",
            "I": "I̺͆",
            "J": "J̺͆",
            "K": "K̺͆",
            "L": "L̺͆",
            "M": "M̺͆",
            "N": "N̺͆",
            "O": "O̺͆",
            "P": "P̺͆",
            "Q": "Q̺͆",
            "R": "R̺͆",
            "S": "S̺͆",
            "T": "T̺͆",
            "U": "U̺͆",
            "V": "V̺͆",
            "W": "W̺͆",
            "X": "X̺͆",
            "Y": "Y̺͆",
            "Z": "Z̺͆",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def arrows(text):
        style = {
            "a": "a͎",
            "b": "b͎",
            "c": "c͎",
            "d": "d͎",
            "e": "e͎",
            "f": "f͎",
            "g": "g͎",
            "h": "h͎",
            "i": "i͎",
            "j": "j͎",
            "k": "k͎",
            "l": "l͎",
            "m": "m͎",
            "n": "n͎",
            "o": "o͎",
            "p": "p͎",
            "q": "q͎",
            "r": "r͎",
            "s": "s͎",
            "t": "t͎",
            "u": "u͎",
            "v": "v͎",
            "w": "w͎",
            "x": "x͎",
            "y": "y͎",
            "z": "z͎",
            "A": "A͎",
            "B": "B͎",
            "C": "C͎",
            "D": "D͎",
            "E": "E͎",
            "F": "F͎",
            "G": "G͎",
            "H": "H͎",
            "I": "I͎",
            "J": "J͎",
            "K": "K͎",
            "L": "L͎",
            "M": "M͎",
            "N": "N͎",
            "O": "O͎",
            "P": "P͎",
            "Q": "Q͎",
            "R": "R͎",
            "S": "S͎",
            "T": "T͎",
            "U": "U͎",
            "V": "V͎",
            "W": "W͎",
            "X": "X͎",
            "Y": "Y͎",
            "Z": "Z͎",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def rvnes(text):
        style = {
            "a": "ል",
            "b": "ጌ",
            "c": "ር",
            "d": "ዕ",
            "e": "ቿ",
            "f": "ቻ",
            "g": "ኗ",
            "h": "ዘ",
            "i": "ጎ",
            "j": "ጋ",
            "k": "ጕ",
            "l": "ረ",
            "m": "ጠ",
            "n": "ክ",
            "o": "ዐ",
            "p": "የ",
            "q": "ዒ",
            "r": "ዪ",
            "s": "ነ",
            "t": "ፕ",
            "u": "ሁ",
            "v": "ሀ",
            "w": "ሠ",
            "x": "ሸ",
            "y": "ሃ",
            "z": "ጊ",
            "A": "ል",
            "B": "ጌ",
            "C": "ር",
            "D": "ዕ",
            "E": "ቿ",
            "F": "ቻ",
            "G": "ኗ",
            "H": "ዘ",
            "I": "ጎ",
            "J": "ጋ",
            "K": "ጕ",
            "L": "ረ",
            "M": "ጠ",
            "N": "ክ",
            "O": "ዐ",
            "P": "የ",
            "Q": "ዒ",
            "R": "ዪ",
            "S": "ነ",
            "T": "ፕ",
            "U": "ሁ",
            "V": "ሀ",
            "W": "ሠ",
            "X": "ሸ",
            "Y": "ሃ",
            "Z": "ጊ",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def strike(text):
        style = {
            "a": "a̶",
            "b": "b̶",
            "c": "c̶",
            "d": "d̶",
            "e": "e̶",
            "f": "f̶",
            "g": "g̶",
            "h": "h̶",
            "i": "i̶",
            "j": "j̶",
            "k": "k̶",
            "l": "l̶",
            "m": "m̶",
            "n": "n̶",
            "o": "o̶",
            "p": "p̶",
            "q": "q̶",
            "r": "r̶",
            "s": "s̶",
            "t": "t̶",
            "u": "u̶",
            "v": "v̶",
            "w": "w̶",
            "x": "x̶",
            "y": "y̶",
            "z": "z̶",
            "A": "A̶",
            "B": "B̶",
            "C": "C̶",
            "D": "D̶",
            "E": "E̶",
            "F": "F̶",
            "G": "G̶",
            "H": "H̶",
            "I": "I̶",
            "J": "J̶",
            "K": "K̶",
            "L": "L̶",
            "M": "M̶",
            "N": "N̶",
            "O": "O̶",
            "P": "P̶",
            "Q": "Q̶",
            "R": "R̶",
            "S": "S̶",
            "T": "T̶",
            "U": "U̶",
            "V": "V̶",
            "W": "W̶",
            "X": "X̶",
            "Y": "Y̶",
            "Z": "Z̶",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text

    def frozen(text):
        style = {
            "a": "a༙",
            "b": "b༙",
            "c": "c༙",
            "d": "d༙",
            "e": "e༙",
            "f": "f༙",
            "g": "g༙",
            "h": "h༙",
            "i": "i༙",
            "j": "j༙",
            "k": "k༙",
            "l": "l༙",
            "m": "m༙",
            "n": "n༙",
            "o": "o༙",
            "p": "p༙",
            "q": "q༙",
            "r": "r༙",
            "s": "s༙",
            "t": "t༙",
            "u": "u༙",
            "v": "v༙",
            "w": "w༙",
            "x": "x༙",
            "y": "y༙",
            "z": "z༙",
            "A": "A༙",
            "B": "B༙",
            "C": "C༙",
            "D": "D༙",
            "E": "E༙",
            "F": "F༙",
            "G": "G༙",
            "H": "H༙",
            "I": "I༙",
            "J": "J༙",
            "K": "K༙",
            "L": "L༙",
            "M": "M༙",
            "N": "N༙",
            "O": "O༙",
            "P": "P༙",
            "Q": "Q༙",
            "R": "R༙",
            "S": "S༙",
            "T": "T༙",
            "U": "U༙",
            "V": "V༙",
            "W": "W༙",
            "X": "X༙",
            "Y": "Y༙",
            "Z": "Z༙",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text


from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YukkiMusic import app

@app.on_message(filters.command(["font", "fonts"]))
async def style_buttons(c, m, cb=False):
    buttons = [
        [
            InlineKeyboardButton("𝚃𝚢𝚙𝚎𝚠𝚛𝚒𝚝𝚎𝚛", callback_data="style+typewriter"),
            InlineKeyboardButton("𝕆𝕦𝕥𝕝𝕚𝕟𝕖", callback_data="style+outline"),
            InlineKeyboardButton("𝐒𝐞𝐫𝐢𝐟", callback_data="style+serif"),
        ],
        [
            InlineKeyboardButton("𝑺𝒆𝒓𝒊𝒇", callback_data="style+bold_cool"),
            InlineKeyboardButton("𝑆𝑒𝑟𝑖𝑓", callback_data="style+cool"),
            InlineKeyboardButton("Sᴍᴀʟʟ Cᴀᴘs", callback_data="style+small_cap"),
        ],
        [
            InlineKeyboardButton("𝓈𝒸𝓇𝒾𝓅𝓉", callback_data="style+script"),
            InlineKeyboardButton("𝓼𝓬𝓻𝓲𝓹𝓽", callback_data="style+script_bolt"),
            InlineKeyboardButton("ᵗⁱⁿʸ", callback_data="style+tiny"),
        ],
        [
            InlineKeyboardButton("ᑕOᗰIᑕ", callback_data="style+comic"),
            InlineKeyboardButton("𝗦𝗮𝗻𝘀", callback_data="style+sans"),
            InlineKeyboardButton("𝙎𝙖𝙣𝙨", callback_data="style+slant_sans"),
        ],
        [
            InlineKeyboardButton("𝘚𝘢𝘯𝘴", callback_data="style+slant"),
            InlineKeyboardButton("𝖲𝖺𝗇𝗌", callback_data="style+sim"),
            InlineKeyboardButton("Ⓒ︎Ⓘ︎Ⓡ︎Ⓒ︎Ⓛ︎Ⓔ︎Ⓢ︎", callback_data="style+circles"),
        ],
        [
            InlineKeyboardButton("🅒︎🅘︎🅡︎🅒︎🅛︎🅔︎🅢︎", callback_data="style+circle_dark"),
            InlineKeyboardButton("𝔊𝔬𝔱𝔥𝔦𝔠", callback_data="style+gothic"),
            InlineKeyboardButton("𝕲𝖔𝖙𝖍𝖎𝖈", callback_data="style+gothic_bolt"),
        ],
        [
            InlineKeyboardButton("C͜͡l͜͡o͜͡u͜͡d͜͡s͜͡", callback_data="style+cloud"),
            InlineKeyboardButton("H̆̈ă̈p̆̈p̆̈y̆̈", callback_data="style+happy"),
            InlineKeyboardButton("S̑̈ȃ̈d̑̈", callback_data="style+sad"),
        ],
        [InlineKeyboardButton("ɴᴇxᴛ ➻", callback_data="nxt")],
    ]
    if not cb:
        await m.reply_text(
            text=m.text.split(None, 1)[1],
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True,
        )
    else:
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))


@app.on_callback_query(filters.regex("^nxt"))
async def nxt(c, m):
    if m.data == "nxt":
        buttons = [
            [
                InlineKeyboardButton("🇸 🇵 🇪 🇨 🇮 🇦 🇱 ", callback_data="style+special"),
                InlineKeyboardButton("🅂🅀🅄🄰🅁🄴🅂", callback_data="style+squares"),
                InlineKeyboardButton("🆂︎🆀︎🆄︎🅰︎🆁︎🅴︎🆂︎", callback_data="style+squares_bold"),
            ],
            [
                InlineKeyboardButton("ꪖꪀᦔꪖꪶꪊᥴ𝓲ꪖ", callback_data="style+andalucia"),
                InlineKeyboardButton("爪卂几ᘜ卂", callback_data="style+manga"),
                InlineKeyboardButton("S̾t̾i̾n̾k̾y̾", callback_data="style+stinky"),
            ],
            [
                InlineKeyboardButton("B̥ͦu̥ͦb̥ͦb̥ͦl̥ͦe̥ͦs̥ͦ", callback_data="style+bubbles"),
                InlineKeyboardButton("U͟n͟d͟e͟r͟l͟i͟n͟e͟", callback_data="style+underline"),
                InlineKeyboardButton("꒒ꍏꀷꌩꌃꀎꁅ", callback_data="style+ladybug"),
            ],
            [
                InlineKeyboardButton("R҉a҉y҉s҉", callback_data="style+rays"),
                InlineKeyboardButton("B҈i҈r҈d҈s҈", callback_data="style+birds"),
                InlineKeyboardButton("S̸l̸a̸s̸h̸", callback_data="style+slash"),
            ],
            [
                InlineKeyboardButton("s⃠t⃠o⃠p⃠", callback_data="style+stop"),
                InlineKeyboardButton("S̺͆k̺͆y̺͆l̺͆i̺͆n̺͆e̺͆", callback_data="style+skyline"),
                InlineKeyboardButton("A͎r͎r͎o͎w͎s͎", callback_data="style+arrows"),
            ],
            [
                InlineKeyboardButton("ዪሀክቿነ", callback_data="style+qvnes"),
                InlineKeyboardButton("S̶t̶r̶i̶k̶e̶", callback_data="style+strike"),
                InlineKeyboardButton("F༙r༙o༙z༙e༙n༙", callback_data="style+frozen"),
            ],
            [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="nxt+0")],
        ]
        await m.answer()
        await m.message.edit_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        await style_buttons(c, m, cb=True)


@app.on_callback_query(filters.regex("^style"))
async def style(c, m):
    await m.answer()
    cmd, style = m.data.split("+")

    if style == "typewriter":
        cls = Fonts.typewriter
    if style == "outline":
        cls = Fonts.outline
    if style == "serif":
        cls = Fonts.serief
    if style == "bold_cool":
        cls = Fonts.bold_cool
    if style == "cool":
        cls = Fonts.cool
    if style == "small_cap":
        cls = Fonts.smallcap
    if style == "script":
        cls = Fonts.script
    if style == "script_bolt":
        cls = Fonts.bold_script
    if style == "tiny":
        cls = Fonts.tiny
    if style == "comic":
        cls = Fonts.comic
    if style == "sans":
        cls = Fonts.san
    if style == "slant_sans":
        cls = Fonts.slant_san
    if style == "slant":
        cls = Fonts.slant
    if style == "sim":
        cls = Fonts.sim
    if style == "circles":
        cls = Fonts.circles
    if style == "circle_dark":
        cls = Fonts.dark_circle
    if style == "gothic":
        cls = Fonts.gothic
    if style == "gothic_bolt":
        cls = Fonts.bold_gothic
    if style == "cloud":
        cls = Fonts.cloud
    if style == "happy":
        cls = Fonts.happy
    if style == "sad":
        cls = Fonts.sad
    if style == "special":
        cls = Fonts.special
    if style == "squares":
        cls = Fonts.square
    if style == "squares_bold":
        cls = Fonts.dark_square
    if style == "andalucia":
        cls = Fonts.andalucia
    if style == "manga":
        cls = Fonts.manga
    if style == "stinky":
        cls = Fonts.stinky
    if style == "bubbles":
        cls = Fonts.bubbles
    if style == "underline":
        cls = Fonts.underline
    if style == "ladybug":
        cls = Fonts.ladybug
    if style == "rays":
        cls = Fonts.rays
    if style == "birds":
        cls = Fonts.birds
    if style == "slash":
        cls = Fonts.slash
    if style == "stop":
        cls = Fonts.stop
    if style == "skyline":
        cls = Fonts.skyline
    if style == "arrows":
        cls = Fonts.arrows
    if style == "qvnes":
        cls = Fonts.rvnes
    if style == "strike":
        cls = Fonts.strike
    if style == "frozen":
        cls = Fonts.frozen
    new_text = cls(m.message.reply_to_message.text.split(None, 1)[1])
    try:
        await m.message.edit_text(f"`{new_text}`")
    except:
        pass


__HELP__ = """
• /font [text] - ᴄᴏɴᴠᴇʀᴛs sɪᴍᴩʟᴇ ᴛᴇxᴛ ᴛᴏ ʙᴇᴀᴜᴛɪғᴜʟ ᴛᴇxᴛ ʙʏ ᴄʜᴀɴɢɪɴɢ ɪᴛ's ғᴏɴᴛ.
 """

__MODULE__ = "Fᴏɴᴛ"