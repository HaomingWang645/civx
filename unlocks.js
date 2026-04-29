// What each tech historically unlocks: resources, organisms, monuments, military
// units, creative works, organizations, and named historical figures.
// Each entry has English name + Chinese translation rendered in parentheses.

window.TECH_UNLOCK_CATEGORIES = {
  resource: { icon: "🪨", label: "Resource" },
  plant:    { icon: "🌾", label: "Plant" },
  animal:   { icon: "🐎", label: "Animal" },
  wonder:   { icon: "🏛️", label: "Wonder" },
  unit:     { icon: "⚔️", label: "Unit / Device" },
  work:     { icon: "📖", label: "Work" },
  org:      { icon: "🏢", label: "Organization" },
  person:   { icon: "👤", label: "Person" },
};

window.TECH_UNLOCKS = {
  // ─── Lower Paleolithic ───────────────────────────────────────
  "bipedal-gait": [
    { type: "person", name: "Australopithecus afarensis (Lucy)", name_zh: "南方古猿阿法种(露西)" },
  ],
  "oldowan": [
    { type: "person", name: "Homo habilis", name_zh: "能人" },
  ],
  "fire-use": [
    { type: "resource", name: "Charcoal", name_zh: "木炭" },
  ],
  "acheulean": [
    { type: "person", name: "Homo erectus", name_zh: "直立人" },
  ],
  "wooden-spear": [
    { type: "unit", name: "Schöningen spears", name_zh: "舍宁根矛" },
  ],
  "cooking": [
    { type: "person", name: "Homo erectus (encephalization)", name_zh: "直立人(脑容量增大)" },
  ],

  // ─── Middle Paleolithic ──────────────────────────────────────
  "levallois": [
    { type: "person", name: "Homo sapiens", name_zh: "智人" },
    { type: "person", name: "Neanderthals", name_zh: "尼安德特人" },
  ],
  "pigments": [
    { type: "resource", name: "Red ochre", name_zh: "红赭石" },
    { type: "work", name: "Blombos engravings", name_zh: "布隆博斯洞穴刻画" },
  ],
  "burial": [
    { type: "wonder", name: "Sungir burials", name_zh: "松吉尔遗址墓葬" },
  ],

  // ─── Upper Paleolithic ───────────────────────────────────────
  "cave-art": [
    { type: "wonder", name: "Chauvet Cave", name_zh: "肖维岩洞" },
    { type: "wonder", name: "Lascaux", name_zh: "拉斯科洞窟" },
    { type: "wonder", name: "Altamira", name_zh: "阿尔塔米拉洞窟" },
    { type: "wonder", name: "Sulawesi cave paintings", name_zh: "苏拉威西洞穴画" },
  ],
  "flute": [
    { type: "work", name: "Divje Babe Flute", name_zh: "迪亚布巴贝骨笛" },
    { type: "work", name: "Hohle Fels flute", name_zh: "霍勒费尔斯骨笛" },
  ],
  "figurines": [
    { type: "work", name: "Venus of Willendorf", name_zh: "维伦多夫的维纳斯" },
    { type: "work", name: "Löwenmensch (Lion-man)", name_zh: "狮人雕像" },
  ],
  "atlatl": [
    { type: "unit", name: "Atlatl darts", name_zh: "投矛器飞镖" },
  ],
  "shamanism": [
    { type: "person", name: "Shaman", name_zh: "萨满" },
  ],
  "rafts": [
    { type: "wonder", name: "Settlement of Sahul (Australia)", name_zh: "萨胡尔大陆(澳大利亚)的定居" },
  ],

  // ─── Mesolithic ──────────────────────────────────────────────
  "dog": [
    { type: "animal", name: "Dog (Canis lupus familiaris)", name_zh: "家犬" },
  ],
  "bow-arrow": [
    { type: "unit", name: "Archer", name_zh: "弓箭手" },
  ],

  // ─── Neolithic ───────────────────────────────────────────────
  "plant-cultivation": [
    { type: "plant", name: "Wheat", name_zh: "小麦" },
    { type: "plant", name: "Barley", name_zh: "大麦" },
    { type: "plant", name: "Lentil", name_zh: "扁豆" },
    { type: "plant", name: "Rice", name_zh: "水稻" },
    { type: "plant", name: "Maize", name_zh: "玉米" },
  ],
  "animal-domestication": [
    { type: "animal", name: "Sheep", name_zh: "绵羊" },
    { type: "animal", name: "Goat", name_zh: "山羊" },
    { type: "animal", name: "Cattle", name_zh: "牛" },
    { type: "animal", name: "Pig", name_zh: "猪" },
  ],
  "pottery": [
    { type: "resource", name: "Clay", name_zh: "黏土" },
  ],
  "village": [
    { type: "wonder", name: "Jericho", name_zh: "杰里科" },
    { type: "wonder", name: "Çatalhöyük", name_zh: "加泰土丘" },
  ],
  "megaliths": [
    { type: "wonder", name: "Göbekli Tepe", name_zh: "哥贝克力石阵" },
    { type: "wonder", name: "Stonehenge", name_zh: "巨石阵" },
    { type: "wonder", name: "Carnac stones", name_zh: "卡纳克巨石" },
  ],
  "copper-smelting": [
    { type: "resource", name: "Copper", name_zh: "铜" },
    { type: "resource", name: "Tin", name_zh: "锡" },
  ],
  "fermentation-brewing": [
    { type: "work", name: "Hymn to Ninkasi", name_zh: "宁卡西颂歌" },
  ],

  // ─── Bronze Age ──────────────────────────────────────────────
  "bronze-metallurgy": [
    { type: "resource", name: "Bronze", name_zh: "青铜" },
  ],
  "spoked-wheel": [
    { type: "unit", name: "Spoked-wheel cart", name_zh: "辐条轮战车" },
  ],
  "horse-domestication": [
    { type: "animal", name: "Horse", name_zh: "马" },
  ],
  "chariot": [
    { type: "unit", name: "War chariot", name_zh: "战车" },
    { type: "unit", name: "Hittite chariotry", name_zh: "赫梯战车队" },
  ],
  "composite-bow": [
    { type: "unit", name: "Horse archer", name_zh: "弓骑兵" },
  ],
  "city-state": [
    { type: "wonder", name: "Uruk", name_zh: "乌鲁克" },
    { type: "wonder", name: "Ur", name_zh: "乌尔" },
    { type: "wonder", name: "Memphis", name_zh: "孟菲斯" },
  ],
  "code-of-law": [
    { type: "work", name: "Code of Ur-Nammu", name_zh: "《乌尔纳姆法典》" },
    { type: "work", name: "Code of Hammurabi", name_zh: "《汉谟拉比法典》" },
    { type: "person", name: "Hammurabi", name_zh: "汉谟拉比" },
  ],
  "cuneiform": [
    { type: "work", name: "Epic of Gilgamesh", name_zh: "《吉尔伽美什史诗》" },
    { type: "person", name: "Enheduanna (earliest named author)", name_zh: "恩赫杜安娜(最早具名作者)" },
  ],
  "hieroglyphics": [
    { type: "work", name: "Pyramid Texts", name_zh: "《金字塔铭文》" },
    { type: "work", name: "Book of the Dead", name_zh: "《亡灵书》" },
    { type: "wonder", name: "Rosetta Stone", name_zh: "罗塞塔石碑" },
  ],
  "alphabet-phoenician": [
    { type: "work", name: "Mesha Stele", name_zh: "米沙石碑" },
  ],
  "abacus": [
    { type: "unit", name: "Sumerian abacus", name_zh: "苏美尔算盘" },
  ],
  "astronomy-observation": [
    { type: "work", name: "Enuma Anu Enlil", name_zh: "《埃努玛·阿努·恩利尔》" },
    { type: "work", name: "MUL.APIN", name_zh: "《MUL.APIN》星表" },
  ],
  "solar-calendar": [
    { type: "work", name: "Egyptian civil calendar", name_zh: "埃及民用历" },
  ],
  "monumental-architecture": [
    { type: "wonder", name: "Stepped temples", name_zh: "阶梯式神庙" },
  ],
  "pyramid-ziggurat": [
    { type: "wonder", name: "Great Pyramid of Giza", name_zh: "吉萨大金字塔" },
    { type: "wonder", name: "Ziggurat of Ur", name_zh: "乌尔大塔庙" },
    { type: "wonder", name: "Step Pyramid of Djoser", name_zh: "左塞尔阶梯金字塔" },
    { type: "person", name: "Imhotep", name_zh: "印何阗" },
  ],
  "glass-making": [
    { type: "resource", name: "Glass", name_zh: "玻璃" },
  ],
  "silver-gold-metallurgy": [
    { type: "resource", name: "Silver", name_zh: "银" },
    { type: "resource", name: "Gold", name_zh: "金" },
    { type: "resource", name: "Electrum", name_zh: "琥珀金" },
  ],
  "olive-wine": [
    { type: "plant", name: "Olive", name_zh: "橄榄" },
    { type: "plant", name: "Grape", name_zh: "葡萄" },
  ],
  "linen-textile": [
    { type: "plant", name: "Flax", name_zh: "亚麻" },
  ],
  "standing-army": [
    { type: "unit", name: "Akkadian infantry", name_zh: "阿卡德步兵" },
    { type: "person", name: "Sargon of Akkad", name_zh: "阿卡德的萨尔贡" },
  ],
  "maritime-trade": [
    { type: "wonder", name: "Tyre", name_zh: "提尔" },
    { type: "wonder", name: "Byblos", name_zh: "比布鲁斯" },
  ],
  "galley-ship": [
    { type: "unit", name: "Phoenician bireme", name_zh: "腓尼基双层桨座船" },
  ],
  "proto-medicine": [
    { type: "work", name: "Edwin Smith Papyrus", name_zh: "《埃德温·史密斯纸草》" },
    { type: "work", name: "Diagnostic Handbook (Esagil-kin-apli)", name_zh: "《诊断手册》(埃萨吉尔-金-阿普利)" },
  ],

  // ─── Classical Antiquity ─────────────────────────────────────
  "iron-smelting": [
    { type: "resource", name: "Iron", name_zh: "铁" },
  ],
  "steel-bloomery": [
    { type: "resource", name: "Wootz steel", name_zh: "乌兹钢" },
    { type: "resource", name: "Damascus steel", name_zh: "大马士革钢" },
  ],
  "iron-weapons": [
    { type: "unit", name: "Hoplite", name_zh: "希腊重装步兵" },
    { type: "unit", name: "Legionary", name_zh: "罗马军团士兵" },
  ],
  "alphabet-greek": [
    { type: "work", name: "Iliad", name_zh: "《伊利亚特》" },
    { type: "work", name: "Odyssey", name_zh: "《奥德赛》" },
    { type: "person", name: "Homer", name_zh: "荷马" },
  ],
  "alphabet-latin": [
    { type: "work", name: "Aeneid", name_zh: "《埃涅阿斯纪》" },
    { type: "person", name: "Virgil", name_zh: "维吉尔" },
  ],
  "philosophy": [
    { type: "person", name: "Socrates", name_zh: "苏格拉底" },
    { type: "person", name: "Plato", name_zh: "柏拉图" },
    { type: "person", name: "Aristotle", name_zh: "亚里士多德" },
    { type: "person", name: "Confucius", name_zh: "孔子" },
    { type: "person", name: "Laozi", name_zh: "老子" },
    { type: "person", name: "Siddhartha Gautama (Buddha)", name_zh: "乔达摩·悉达多(佛陀)" },
    { type: "work", name: "Republic (Plato)", name_zh: "《理想国》(柏拉图)" },
    { type: "work", name: "Analects", name_zh: "《论语》" },
  ],
  "geometry-euclidean": [
    { type: "person", name: "Euclid", name_zh: "欧几里得" },
    { type: "work", name: "Elements (Euclid)", name_zh: "《几何原本》(欧几里得)" },
    { type: "person", name: "Archimedes", name_zh: "阿基米德" },
  ],
  "zero-numeral": [
    { type: "person", name: "Brahmagupta", name_zh: "婆罗摩笈多" },
    { type: "work", name: "Brāhma-sphuṭa-siddhānta", name_zh: "《婆罗摩历算书》" },
  ],
  "alchemy": [
    { type: "person", name: "Zosimos of Panopolis", name_zh: "帕诺波利斯的佐西默斯" },
    { type: "person", name: "Jabir ibn Hayyan", name_zh: "贾比尔·伊本·哈扬" },
  ],
  "coinage": [
    { type: "resource", name: "Lydian electrum coin", name_zh: "吕底亚琥珀金币" },
    { type: "person", name: "Croesus", name_zh: "克罗伊索斯" },
  ],
  "democracy": [
    { type: "person", name: "Cleisthenes", name_zh: "克里斯提尼" },
    { type: "person", name: "Pericles", name_zh: "伯里克利" },
  ],
  "republic": [
    { type: "person", name: "Cicero", name_zh: "西塞罗" },
    { type: "work", name: "On the Commonwealth", name_zh: "《论共和国》" },
  ],
  "empire": [
    { type: "person", name: "Cyrus the Great", name_zh: "居鲁士大帝" },
    { type: "person", name: "Alexander the Great", name_zh: "亚历山大大帝" },
    { type: "person", name: "Augustus", name_zh: "奥古斯都" },
    { type: "person", name: "Qin Shi Huang", name_zh: "秦始皇" },
    { type: "person", name: "Ashoka", name_zh: "阿育王" },
  ],
  "roman-law": [
    { type: "work", name: "Twelve Tables", name_zh: "《十二铜表法》" },
    { type: "work", name: "Corpus Juris Civilis", name_zh: "《查士丁尼民法大全》" },
    { type: "person", name: "Justinian I", name_zh: "查士丁尼一世" },
  ],
  "roads-paved": [
    { type: "wonder", name: "Appian Way", name_zh: "阿庇亚大道" },
    { type: "wonder", name: "Persian Royal Road", name_zh: "波斯御道" },
    { type: "wonder", name: "Silk Road", name_zh: "丝绸之路" },
  ],
  "aqueduct": [
    { type: "wonder", name: "Pont du Gard", name_zh: "加尔桥" },
    { type: "wonder", name: "Aqua Claudia", name_zh: "克劳狄渡槽" },
  ],
  "arch-vault": [
    { type: "wonder", name: "Pantheon (dome)", name_zh: "万神殿(穹顶)" },
    { type: "wonder", name: "Colosseum", name_zh: "罗马斗兽场" },
  ],
  "concrete-roman": [
    { type: "resource", name: "Pozzolana cement", name_zh: "火山灰水泥" },
    { type: "wonder", name: "Pantheon dome", name_zh: "万神殿穹顶" },
  ],
  "crossbow": [
    { type: "unit", name: "Han dynasty crossbowman", name_zh: "汉朝弩兵" },
  ],
  "siege-engine": [
    { type: "unit", name: "Catapult", name_zh: "投石机" },
    { type: "unit", name: "Ballista", name_zh: "弩炮" },
    { type: "unit", name: "Battering ram", name_zh: "攻城槌" },
  ],
  "cavalry": [
    { type: "unit", name: "Cataphract", name_zh: "重甲骑兵" },
    { type: "unit", name: "Persian Immortal", name_zh: "波斯不死军" },
  ],
  "saddle-stirrup": [
    { type: "unit", name: "Heavy cavalry", name_zh: "重骑兵" },
  ],
  "silk-production": [
    { type: "animal", name: "Silkworm (Bombyx mori)", name_zh: "家蚕" },
    { type: "plant", name: "Mulberry", name_zh: "桑树" },
  ],
  "paper-making": [
    { type: "person", name: "Cai Lun", name_zh: "蔡伦" },
  ],
  "world-religion": [
    { type: "person", name: "Jesus of Nazareth", name_zh: "拿撒勒人耶稣" },
    { type: "person", name: "Paul the Apostle", name_zh: "使徒保罗" },
    { type: "person", name: "Muhammad", name_zh: "穆罕默德" },
    { type: "person", name: "Buddha", name_zh: "佛陀" },
    { type: "person", name: "Zoroaster", name_zh: "琐罗亚斯德" },
    { type: "work", name: "Bible", name_zh: "《圣经》" },
    { type: "work", name: "Qur'an", name_zh: "《古兰经》" },
    { type: "work", name: "Tripitaka", name_zh: "《三藏》" },
  ],
  "monasticism": [
    { type: "person", name: "Benedict of Nursia", name_zh: "努西亚的本笃" },
    { type: "org", name: "Benedictine Order", name_zh: "本笃会" },
  ],
  "library": [
    { type: "wonder", name: "Library of Alexandria", name_zh: "亚历山大图书馆" },
    { type: "wonder", name: "Library of Pergamon", name_zh: "帕加马图书馆" },
    { type: "wonder", name: "Nalanda", name_zh: "那烂陀寺" },
  ],
  "scientific-method-proto": [
    { type: "person", name: "Aristotle", name_zh: "亚里士多德" },
    { type: "person", name: "Ibn al-Haytham", name_zh: "海什木(伊本·海赛姆)" },
  ],
  "medicine-galenic": [
    { type: "person", name: "Hippocrates", name_zh: "希波克拉底" },
    { type: "person", name: "Galen", name_zh: "盖伦" },
    { type: "work", name: "Hippocratic Corpus", name_zh: "《希波克拉底文集》" },
  ],
  "compass-early": [
    { type: "unit", name: "South-pointing chariot", name_zh: "指南车" },
  ],
  "triremes": [
    { type: "unit", name: "Athenian trireme", name_zh: "雅典三列桨战船" },
    { type: "person", name: "Themistocles", name_zh: "地米斯托克利" },
  ],
  "gear-mechanism": [
    { type: "work", name: "Antikythera mechanism", name_zh: "安提基特拉机械" },
    { type: "person", name: "Hero of Alexandria", name_zh: "亚历山大里亚的希罗" },
  ],
  "woodblock-printing": [
    { type: "work", name: "Diamond Sutra", name_zh: "《金刚经》" },
  ],

  // ─── Medieval ────────────────────────────────────────────────
  "arabic-numerals": [
    { type: "person", name: "Muhammad ibn Musa al-Khwarizmi", name_zh: "花剌子米" },
    { type: "person", name: "Fibonacci", name_zh: "斐波那契" },
  ],
  "algebra": [
    { type: "work", name: "The Compendious Book on Calculation", name_zh: "《代数学》" },
    { type: "person", name: "Omar Khayyam", name_zh: "欧玛尔·海亚姆" },
  ],
  "gunpowder": [
    { type: "resource", name: "Saltpeter", name_zh: "硝石" },
    { type: "resource", name: "Sulfur", name_zh: "硫磺" },
    { type: "work", name: "Wujing Zongyao", name_zh: "《武经总要》" },
  ],
  "moveable-type": [
    { type: "person", name: "Bi Sheng", name_zh: "毕昇" },
  ],
  "mechanical-clock": [
    { type: "wonder", name: "Strasbourg astronomical clock", name_zh: "斯特拉斯堡天文钟" },
    { type: "wonder", name: "Salisbury Cathedral clock", name_zh: "索尔兹伯里大教堂钟" },
    { type: "person", name: "Su Song", name_zh: "苏颂" },
  ],
  "windmill": [
    { type: "wonder", name: "Kinderdijk windmills", name_zh: "金德代克风车群" },
  ],
  "horse-collar": [
    { type: "unit", name: "Heavy plow team", name_zh: "重犁畜队" },
  ],
  "university": [
    { type: "wonder", name: "University of Bologna", name_zh: "博洛尼亚大学" },
    { type: "wonder", name: "University of Paris", name_zh: "巴黎大学" },
    { type: "wonder", name: "Oxford", name_zh: "牛津大学" },
    { type: "wonder", name: "Al-Qarawiyyin", name_zh: "卡鲁因大学" },
  ],
  "scholasticism": [
    { type: "person", name: "Thomas Aquinas", name_zh: "托马斯·阿奎那" },
    { type: "person", name: "Peter Abelard", name_zh: "彼得·阿伯拉尔" },
    { type: "work", name: "Summa Theologica", name_zh: "《神学大全》" },
  ],
  "gothic-architecture": [
    { type: "wonder", name: "Notre-Dame de Paris", name_zh: "巴黎圣母院" },
    { type: "wonder", name: "Chartres Cathedral", name_zh: "沙特尔大教堂" },
    { type: "wonder", name: "Cologne Cathedral", name_zh: "科隆大教堂" },
  ],
  "castle": [
    { type: "wonder", name: "Krak des Chevaliers", name_zh: "骑士堡" },
    { type: "wonder", name: "Tower of London", name_zh: "伦敦塔" },
    { type: "wonder", name: "Himeji Castle", name_zh: "姬路城" },
  ],
  "knight-cavalry": [
    { type: "unit", name: "Knight (man-at-arms)", name_zh: "骑士(重装战士)" },
    { type: "org", name: "Knights Templar", name_zh: "圣殿骑士团" },
    { type: "org", name: "Knights Hospitaller", name_zh: "医院骑士团" },
  ],
  "longbow": [
    { type: "unit", name: "English longbowman", name_zh: "英格兰长弓手" },
    { type: "wonder", name: "Battle of Agincourt", name_zh: "阿金库尔战役" },
  ],
  "cannon-early": [
    { type: "unit", name: "Bombard", name_zh: "臼炮" },
    { type: "unit", name: "Dardanelles Gun", name_zh: "达达尼尔海峡巨炮" },
  ],
  "caravel": [
    { type: "unit", name: "Portuguese caravel", name_zh: "葡萄牙卡拉维尔帆船" },
    { type: "person", name: "Henry the Navigator", name_zh: "航海家亨利" },
  ],
  "hospital": [
    { type: "wonder", name: "Bimaristan al-Mansuri", name_zh: "曼苏里医院" },
  ],
  "guild": [
    { type: "org", name: "Hanseatic League", name_zh: "汉萨同盟" },
    { type: "org", name: "Worshipful Company of Mercers", name_zh: "布商公会" },
  ],
  "banking-double-entry": [
    { type: "org", name: "Medici Bank", name_zh: "美第奇银行" },
    { type: "person", name: "Cosimo de' Medici", name_zh: "科西莫·德·美第奇" },
    { type: "person", name: "Luca Pacioli", name_zh: "卢卡·帕乔利" },
  ],
  "letter-of-credit": [
    { type: "work", name: "Bill of exchange", name_zh: "汇票" },
  ],
  "spectacles": [
    { type: "person", name: "Salvino degli Armati", name_zh: "萨尔维诺·德利·阿尔马蒂" },
  ],
  "distillation": [
    { type: "resource", name: "Brandy", name_zh: "白兰地" },
    { type: "resource", name: "Whiskey", name_zh: "威士忌" },
    { type: "person", name: "Avicenna", name_zh: "阿维森纳(伊本·西那)" },
  ],
  "paper-mill": [
    { type: "wonder", name: "Fabriano paper mill", name_zh: "法布里亚诺造纸厂" },
  ],

  // ─── Renaissance ─────────────────────────────────────────────
  "printing-press": [
    { type: "person", name: "Johannes Gutenberg", name_zh: "约翰内斯·古腾堡" },
    { type: "work", name: "Gutenberg Bible", name_zh: "《古腾堡圣经》" },
  ],
  "vernacular-literature": [
    { type: "person", name: "Dante Alighieri", name_zh: "但丁·阿利吉耶里" },
    { type: "person", name: "Geoffrey Chaucer", name_zh: "杰弗里·乔叟" },
    { type: "person", name: "Miguel de Cervantes", name_zh: "米格尔·德·塞万提斯" },
    { type: "work", name: "Divine Comedy", name_zh: "《神曲》" },
    { type: "work", name: "The Canterbury Tales", name_zh: "《坎特伯雷故事集》" },
    { type: "work", name: "Don Quixote", name_zh: "《堂吉诃德》" },
  ],
  "humanism": [
    { type: "person", name: "Petrarch", name_zh: "彼特拉克" },
    { type: "person", name: "Erasmus", name_zh: "伊拉斯谟" },
    { type: "work", name: "In Praise of Folly", name_zh: "《愚人颂》" },
  ],
  "linear-perspective": [
    { type: "person", name: "Filippo Brunelleschi", name_zh: "菲利波·布鲁内莱斯基" },
    { type: "person", name: "Leon Battista Alberti", name_zh: "莱昂·巴蒂斯塔·阿尔伯蒂" },
    { type: "work", name: "On Painting (Della pittura)", name_zh: "《论绘画》" },
  ],
  "oil-painting": [
    { type: "person", name: "Jan van Eyck", name_zh: "扬·凡·艾克" },
    { type: "person", name: "Leonardo da Vinci", name_zh: "列奥纳多·达·芬奇" },
    { type: "person", name: "Michelangelo", name_zh: "米开朗琪罗" },
    { type: "person", name: "Raphael", name_zh: "拉斐尔" },
    { type: "person", name: "Rembrandt", name_zh: "伦勃朗" },
    { type: "work", name: "Mona Lisa", name_zh: "《蒙娜丽莎》" },
    { type: "work", name: "The Last Supper", name_zh: "《最后的晚餐》" },
    { type: "work", name: "The School of Athens", name_zh: "《雅典学院》" },
    { type: "work", name: "Sistine Chapel ceiling", name_zh: "西斯廷礼拜堂天顶画" },
  ],
  "opera-orchestra": [
    { type: "person", name: "Claudio Monteverdi", name_zh: "克劳迪奥·蒙特威尔第" },
    { type: "work", name: "L'Orfeo", name_zh: "《奥菲欧》" },
  ],
  "scientific-method": [
    { type: "person", name: "Francis Bacon", name_zh: "弗朗西斯·培根" },
    { type: "person", name: "Galileo Galilei", name_zh: "伽利略·伽利雷" },
    { type: "work", name: "Novum Organum", name_zh: "《新工具》" },
  ],
  "heliocentrism": [
    { type: "person", name: "Nicolaus Copernicus", name_zh: "尼古拉·哥白尼" },
    { type: "person", name: "Johannes Kepler", name_zh: "约翰内斯·开普勒" },
    { type: "person", name: "Galileo Galilei", name_zh: "伽利略·伽利雷" },
    { type: "work", name: "De revolutionibus orbium coelestium", name_zh: "《天体运行论》" },
    { type: "work", name: "Astronomia nova", name_zh: "《新天文学》" },
  ],
  "logarithms": [
    { type: "person", name: "John Napier", name_zh: "约翰·纳皮尔" },
    { type: "work", name: "Mirifici Logarithmorum Canonis Descriptio", name_zh: "《奇妙对数表》" },
  ],
  "anatomy-vesalius": [
    { type: "person", name: "Andreas Vesalius", name_zh: "安德烈亚斯·维萨里" },
    { type: "work", name: "De humani corporis fabrica", name_zh: "《人体的构造》" },
  ],
  "microscope": [
    { type: "person", name: "Antonie van Leeuwenhoek", name_zh: "安东尼·范·列文虎克" },
    { type: "person", name: "Robert Hooke", name_zh: "罗伯特·胡克" },
    { type: "work", name: "Micrographia", name_zh: "《显微图谱》" },
  ],
  "telescope": [
    { type: "person", name: "Galileo Galilei", name_zh: "伽利略·伽利雷" },
    { type: "work", name: "Sidereus Nuncius", name_zh: "《星际信使》" },
  ],
  "pendulum-clock": [
    { type: "person", name: "Christiaan Huygens", name_zh: "克里斯蒂安·惠更斯" },
  ],
  "protestant-reformation": [
    { type: "person", name: "Martin Luther", name_zh: "马丁·路德" },
    { type: "person", name: "John Calvin", name_zh: "约翰·加尔文" },
    { type: "work", name: "Ninety-five Theses", name_zh: "《九十五条论纲》" },
  ],
  "nation-state": [
    { type: "person", name: "Cardinal Richelieu", name_zh: "黎塞留枢机" },
    { type: "person", name: "Louis XIV", name_zh: "路易十四" },
  ],
  "joint-stock-company": [
    { type: "org", name: "Dutch East India Company (VOC)", name_zh: "荷兰东印度公司" },
    { type: "org", name: "English East India Company", name_zh: "英国东印度公司" },
    { type: "org", name: "Hudson's Bay Company", name_zh: "哈德逊湾公司" },
  ],
  "mercantilism": [
    { type: "person", name: "Jean-Baptiste Colbert", name_zh: "让-巴蒂斯特·柯尔贝尔" },
  ],
  "galleon": [
    { type: "unit", name: "Manila galleon", name_zh: "马尼拉大帆船" },
    { type: "unit", name: "Spanish treasure fleet", name_zh: "西班牙宝船队" },
  ],
  "ocean-navigation": [
    { type: "person", name: "Vasco da Gama", name_zh: "瓦斯科·达·伽马" },
    { type: "person", name: "Ferdinand Magellan", name_zh: "斐迪南·麦哲伦" },
    { type: "person", name: "Zheng He", name_zh: "郑和" },
  ],
  "new-world-encounter": [
    { type: "person", name: "Christopher Columbus", name_zh: "克里斯托弗·哥伦布" },
    { type: "person", name: "Amerigo Vespucci", name_zh: "亚美利哥·韦斯普奇" },
    { type: "wonder", name: "Hispaniola landing", name_zh: "伊斯帕尼奥拉岛登陆" },
  ],
  "colonialism": [
    { type: "person", name: "Hernán Cortés", name_zh: "埃尔南·科尔特斯" },
    { type: "person", name: "Francisco Pizarro", name_zh: "弗朗西斯科·皮萨罗" },
  ],
  "columbian-exchange": [
    { type: "plant", name: "Potato", name_zh: "马铃薯" },
    { type: "plant", name: "Tomato", name_zh: "番茄" },
    { type: "plant", name: "Maize", name_zh: "玉米" },
    { type: "plant", name: "Cacao (chocolate)", name_zh: "可可(巧克力)" },
    { type: "plant", name: "Tobacco", name_zh: "烟草" },
    { type: "plant", name: "Chili pepper", name_zh: "辣椒" },
    { type: "plant", name: "Vanilla", name_zh: "香草" },
    { type: "animal", name: "Horse (to Americas)", name_zh: "马(传入美洲)" },
    { type: "animal", name: "Cattle (to Americas)", name_zh: "牛(传入美洲)" },
  ],
  "musket": [
    { type: "unit", name: "Matchlock musketeer", name_zh: "火绳枪兵" },
    { type: "unit", name: "Spanish tercio", name_zh: "西班牙方阵" },
  ],
  "artillery": [
    { type: "unit", name: "Field cannon", name_zh: "野战炮" },
  ],
  "bastion-fortification": [
    { type: "wonder", name: "Star fort of Naarden", name_zh: "纳尔登星形要塞" },
    { type: "wonder", name: "Palmanova", name_zh: "帕尔马诺瓦城" },
  ],

  // ─── Enlightenment ───────────────────────────────────────────
  "newtonian-mechanics": [
    { type: "person", name: "Isaac Newton", name_zh: "艾萨克·牛顿" },
    { type: "work", name: "Philosophiæ Naturalis Principia Mathematica", name_zh: "《自然哲学的数学原理》" },
  ],
  "calculus": [
    { type: "person", name: "Isaac Newton", name_zh: "艾萨克·牛顿" },
    { type: "person", name: "Gottfried Wilhelm Leibniz", name_zh: "戈特弗里德·威廉·莱布尼茨" },
  ],
  "gravitation-law": [
    { type: "work", name: "Inverse-square law", name_zh: "平方反比定律" },
  ],
  "cartesian-coordinates": [
    { type: "person", name: "René Descartes", name_zh: "勒内·笛卡尔" },
    { type: "work", name: "La Géométrie", name_zh: "《几何学》" },
  ],
  "probability-theory": [
    { type: "person", name: "Blaise Pascal", name_zh: "布莱兹·帕斯卡" },
    { type: "person", name: "Pierre de Fermat", name_zh: "皮埃尔·德·费马" },
  ],
  "thermometer": [
    { type: "person", name: "Daniel Gabriel Fahrenheit", name_zh: "丹尼尔·华伦海特" },
    { type: "person", name: "Anders Celsius", name_zh: "安德斯·摄尔修斯" },
  ],
  "barometer": [
    { type: "person", name: "Evangelista Torricelli", name_zh: "埃万杰利斯塔·托里拆利" },
  ],
  "germ-precursor": [
    { type: "person", name: "Antonie van Leeuwenhoek", name_zh: "安东尼·范·列文虎克" },
  ],
  "vaccination": [
    { type: "person", name: "Edward Jenner", name_zh: "爱德华·詹纳" },
  ],
  "chemistry-modern": [
    { type: "person", name: "Antoine Lavoisier", name_zh: "安托万·拉瓦锡" },
    { type: "work", name: "Traité élémentaire de chimie", name_zh: "《化学基础论》" },
    { type: "resource", name: "Oxygen (named)", name_zh: "氧(命名)" },
  ],
  "electricity-static": [
    { type: "person", name: "Benjamin Franklin", name_zh: "本杰明·富兰克林" },
    { type: "person", name: "Charles-Augustin de Coulomb", name_zh: "夏尔·奥古斯丁·库仑" },
  ],
  "steam-pump": [
    { type: "person", name: "Thomas Newcomen", name_zh: "托马斯·纽科门" },
    { type: "person", name: "Thomas Savery", name_zh: "托马斯·萨弗里" },
  ],
  "steam-engine-watt": [
    { type: "person", name: "James Watt", name_zh: "詹姆斯·瓦特" },
    { type: "person", name: "Matthew Boulton", name_zh: "马修·博尔顿" },
    { type: "org", name: "Boulton & Watt", name_zh: "博尔顿与瓦特公司" },
  ],
  "coke-iron": [
    { type: "person", name: "Abraham Darby I", name_zh: "亚伯拉罕·达比一世" },
    { type: "wonder", name: "Coalbrookdale", name_zh: "科尔布鲁克代尔" },
  ],
  "canal-system": [
    { type: "wonder", name: "Bridgewater Canal", name_zh: "布里奇沃特运河" },
    { type: "wonder", name: "Erie Canal", name_zh: "伊利运河" },
    { type: "wonder", name: "Canal du Midi", name_zh: "米迪运河" },
  ],
  "agricultural-revolution": [
    { type: "person", name: "Jethro Tull", name_zh: "杰思罗·塔尔" },
    { type: "unit", name: "Seed drill", name_zh: "条播机" },
  ],
  "crop-rotation-norfolk": [
    { type: "person", name: "Charles Townshend", name_zh: "查尔斯·汤森" },
  ],
  "selective-breeding": [
    { type: "person", name: "Robert Bakewell", name_zh: "罗伯特·贝克韦尔" },
    { type: "animal", name: "Dishley Leicester sheep", name_zh: "迪希莱-莱斯特绵羊" },
  ],
  "enlightenment-philosophy": [
    { type: "person", name: "John Locke", name_zh: "约翰·洛克" },
    { type: "person", name: "Voltaire", name_zh: "伏尔泰" },
    { type: "person", name: "Jean-Jacques Rousseau", name_zh: "让-雅克·卢梭" },
    { type: "person", name: "Immanuel Kant", name_zh: "伊曼努尔·康德" },
    { type: "person", name: "David Hume", name_zh: "大卫·休谟" },
    { type: "work", name: "Two Treatises of Government", name_zh: "《政府论》" },
    { type: "work", name: "The Social Contract", name_zh: "《社会契约论》" },
  ],
  "liberal-democracy": [
    { type: "person", name: "Thomas Jefferson", name_zh: "托马斯·杰斐逊" },
    { type: "person", name: "James Madison", name_zh: "詹姆斯·麦迪逊" },
    { type: "work", name: "Declaration of Independence", name_zh: "《独立宣言》" },
    { type: "work", name: "Declaration of the Rights of Man", name_zh: "《人权宣言》" },
  ],
  "separation-of-powers": [
    { type: "person", name: "Montesquieu", name_zh: "孟德斯鸠" },
    { type: "work", name: "The Spirit of the Laws", name_zh: "《论法的精神》" },
  ],
  "encyclopedia": [
    { type: "person", name: "Denis Diderot", name_zh: "德尼·狄德罗" },
    { type: "person", name: "Jean le Rond d'Alembert", name_zh: "让·勒朗·达朗贝尔" },
    { type: "work", name: "Encyclopédie", name_zh: "《百科全书》" },
  ],
  "factory-system": [
    { type: "wonder", name: "Cromford Mill", name_zh: "克罗姆福德工厂" },
    { type: "person", name: "Richard Arkwright", name_zh: "理查德·阿克莱特" },
  ],
  "spinning-jenny": [
    { type: "person", name: "James Hargreaves", name_zh: "詹姆斯·哈格里夫斯" },
  ],
  "power-loom": [
    { type: "person", name: "Edmund Cartwright", name_zh: "埃德蒙·卡特赖特" },
  ],
  "naval-warship": [
    { type: "unit", name: "HMS Victory", name_zh: "胜利号战舰" },
    { type: "person", name: "Horatio Nelson", name_zh: "霍雷肖·纳尔逊" },
  ],
  "central-bank": [
    { type: "org", name: "Bank of England", name_zh: "英格兰银行" },
    { type: "org", name: "Banque de France", name_zh: "法兰西银行" },
  ],

  // ─── Industrial ──────────────────────────────────────────────
  "bessemer-steel": [
    { type: "person", name: "Henry Bessemer", name_zh: "亨利·贝塞麦" },
    { type: "person", name: "Andrew Carnegie", name_zh: "安德鲁·卡内基" },
    { type: "org", name: "Carnegie Steel", name_zh: "卡内基钢铁公司" },
  ],
  "railway-locomotive": [
    { type: "person", name: "George Stephenson", name_zh: "乔治·斯蒂芬森" },
    { type: "unit", name: "Stephenson's Rocket", name_zh: "火箭号机车" },
  ],
  "telegraph": [
    { type: "person", name: "Samuel Morse", name_zh: "塞缪尔·摩尔斯" },
    { type: "person", name: "Charles Wheatstone", name_zh: "查尔斯·惠斯通" },
    { type: "work", name: "Morse code", name_zh: "摩尔斯电码" },
  ],
  "railroad-network": [
    { type: "wonder", name: "Transcontinental Railroad", name_zh: "横贯大陆铁路" },
    { type: "wonder", name: "Trans-Siberian Railway", name_zh: "西伯利亚大铁路" },
  ],
  "steamship": [
    { type: "unit", name: "SS Great Eastern", name_zh: "大东方号" },
    { type: "unit", name: "RMS Titanic", name_zh: "泰坦尼克号" },
    { type: "person", name: "Isambard Kingdom Brunel", name_zh: "伊桑巴德·金德姆·布鲁内尔" },
  ],
  "electric-battery": [
    { type: "person", name: "Alessandro Volta", name_zh: "亚历山德罗·伏打" },
  ],
  "electromagnetism": [
    { type: "person", name: "Hans Christian Ørsted", name_zh: "汉斯·克里斯蒂安·奥斯特" },
    { type: "person", name: "Michael Faraday", name_zh: "迈克尔·法拉第" },
    { type: "person", name: "James Clerk Maxwell", name_zh: "詹姆斯·克拉克·麦克斯韦" },
    { type: "work", name: "A Treatise on Electricity and Magnetism", name_zh: "《电磁通论》" },
  ],
  "electric-motor": [
    { type: "person", name: "Nikola Tesla", name_zh: "尼古拉·特斯拉" },
    { type: "person", name: "Michael Faraday", name_zh: "迈克尔·法拉第" },
  ],
  "telephone": [
    { type: "person", name: "Alexander Graham Bell", name_zh: "亚历山大·格拉汉姆·贝尔" },
    { type: "org", name: "Bell Telephone Company", name_zh: "贝尔电话公司" },
    { type: "org", name: "AT&T", name_zh: "美国电话电报公司" },
  ],
  "radio-wireless": [
    { type: "person", name: "Guglielmo Marconi", name_zh: "古列尔莫·马可尼" },
    { type: "person", name: "Heinrich Hertz", name_zh: "海因里希·赫兹" },
  ],
  "photography": [
    { type: "person", name: "Louis Daguerre", name_zh: "路易·达盖尔" },
    { type: "person", name: "William Henry Fox Talbot", name_zh: "威廉·亨利·福克斯·塔尔博特" },
    { type: "org", name: "Eastman Kodak", name_zh: "伊士曼柯达" },
  ],
  "cinema": [
    { type: "person", name: "Auguste & Louis Lumière", name_zh: "卢米埃尔兄弟" },
    { type: "work", name: "Workers Leaving the Lumière Factory", name_zh: "《工厂大门》" },
  ],
  "oil-petroleum": [
    { type: "resource", name: "Crude oil", name_zh: "原油" },
    { type: "person", name: "John D. Rockefeller", name_zh: "约翰·D·洛克菲勒" },
    { type: "org", name: "Standard Oil", name_zh: "标准石油" },
  ],
  "internal-combustion": [
    { type: "person", name: "Nikolaus Otto", name_zh: "尼古拉斯·奥托" },
    { type: "person", name: "Rudolf Diesel", name_zh: "鲁道夫·狄塞尔" },
  ],
  "automobile": [
    { type: "person", name: "Karl Benz", name_zh: "卡尔·本茨" },
    { type: "person", name: "Gottlieb Daimler", name_zh: "戈特利布·戴姆勒" },
    { type: "unit", name: "Benz Patent-Motorwagen", name_zh: "奔驰一号" },
    { type: "unit", name: "Ford Model T", name_zh: "福特T型车" },
  ],
  "evolution-darwin": [
    { type: "person", name: "Charles Darwin", name_zh: "查尔斯·达尔文" },
    { type: "person", name: "Alfred Russel Wallace", name_zh: "阿尔弗雷德·罗素·华莱士" },
    { type: "work", name: "On the Origin of Species", name_zh: "《物种起源》" },
    { type: "work", name: "The Descent of Man", name_zh: "《人类的由来》" },
  ],
  "germ-theory": [
    { type: "person", name: "Louis Pasteur", name_zh: "路易·巴斯德" },
    { type: "person", name: "Robert Koch", name_zh: "罗伯特·科赫" },
    { type: "person", name: "Ignaz Semmelweis", name_zh: "伊格纳兹·塞麦尔维斯" },
  ],
  "antiseptic-surgery": [
    { type: "person", name: "Joseph Lister", name_zh: "约瑟夫·李斯特" },
  ],
  "anesthesia": [
    { type: "person", name: "William Morton", name_zh: "威廉·莫顿" },
    { type: "resource", name: "Ether", name_zh: "乙醚" },
    { type: "resource", name: "Chloroform", name_zh: "氯仿" },
  ],
  "public-sanitation": [
    { type: "person", name: "John Snow", name_zh: "约翰·斯诺" },
    { type: "person", name: "Edwin Chadwick", name_zh: "埃德温·查德威克" },
  ],
  "thermodynamics": [
    { type: "person", name: "Sadi Carnot", name_zh: "萨迪·卡诺" },
    { type: "person", name: "Rudolf Clausius", name_zh: "鲁道夫·克劳修斯" },
    { type: "person", name: "Lord Kelvin", name_zh: "开尔文勋爵" },
    { type: "person", name: "Ludwig Boltzmann", name_zh: "路德维希·玻尔兹曼" },
  ],
  "periodic-table": [
    { type: "person", name: "Dmitri Mendeleev", name_zh: "德米特里·门捷列夫" },
  ],
  "atomic-theory": [
    { type: "person", name: "John Dalton", name_zh: "约翰·道尔顿" },
    { type: "person", name: "Ernest Rutherford", name_zh: "欧内斯特·卢瑟福" },
    { type: "person", name: "Niels Bohr", name_zh: "尼尔斯·玻尔" },
  ],
  "electron-discovery": [
    { type: "person", name: "J.J. Thomson", name_zh: "约瑟夫·约翰·汤姆孙" },
  ],
  "x-ray": [
    { type: "person", name: "Wilhelm Röntgen", name_zh: "威廉·伦琴" },
  ],
  "machine-tool": [
    { type: "person", name: "Henry Maudslay", name_zh: "亨利·莫兹利" },
    { type: "person", name: "Joseph Whitworth", name_zh: "约瑟夫·惠特沃斯" },
  ],
  "interchangeable-parts": [
    { type: "person", name: "Eli Whitney", name_zh: "伊莱·惠特尼" },
    { type: "person", name: "John H. Hall", name_zh: "约翰·H·霍尔" },
  ],
  "assembly-line": [
    { type: "person", name: "Henry Ford", name_zh: "亨利·福特" },
    { type: "unit", name: "Ford Model T", name_zh: "福特T型车" },
    { type: "org", name: "Ford Motor Company", name_zh: "福特汽车公司" },
  ],
  "modern-corporation": [
    { type: "org", name: "Standard Oil", name_zh: "标准石油" },
    { type: "org", name: "U.S. Steel", name_zh: "美国钢铁公司" },
    { type: "org", name: "General Electric", name_zh: "通用电气" },
  ],
  "labor-union": [
    { type: "org", name: "Knights of Labor", name_zh: "劳动骑士团" },
    { type: "org", name: "American Federation of Labor (AFL)", name_zh: "美国劳工联合会" },
    { type: "org", name: "Trades Union Congress", name_zh: "英国职工大会" },
  ],
  "newspaper-mass": [
    { type: "org", name: "The New York Sun", name_zh: "《纽约太阳报》" },
    { type: "org", name: "Reuters", name_zh: "路透社" },
    { type: "person", name: "Joseph Pulitzer", name_zh: "约瑟夫·普利策" },
  ],
  "skyscraper": [
    { type: "wonder", name: "Home Insurance Building", name_zh: "家庭保险大楼" },
    { type: "wonder", name: "Empire State Building", name_zh: "帝国大厦" },
    { type: "wonder", name: "Eiffel Tower", name_zh: "埃菲尔铁塔" },
    { type: "wonder", name: "Chrysler Building", name_zh: "克莱斯勒大厦" },
  ],
  "elevator": [
    { type: "person", name: "Elisha Otis", name_zh: "伊莱沙·奥的斯" },
    { type: "org", name: "Otis Elevator", name_zh: "奥的斯电梯公司" },
  ],
  "machine-gun": [
    { type: "unit", name: "Maxim gun", name_zh: "马克沁机枪" },
    { type: "unit", name: "Gatling gun", name_zh: "加特林机枪" },
    { type: "person", name: "Hiram Maxim", name_zh: "海勒姆·马克沁" },
  ],
  "electrification": [
    { type: "person", name: "Thomas Edison", name_zh: "托马斯·爱迪生" },
    { type: "person", name: "Nikola Tesla", name_zh: "尼古拉·特斯拉" },
    { type: "org", name: "General Electric", name_zh: "通用电气" },
    { type: "org", name: "Westinghouse Electric", name_zh: "西屋电气" },
  ],

  // ─── Modern ──────────────────────────────────────────────────
  "airplane": [
    { type: "person", name: "Wilbur & Orville Wright", name_zh: "莱特兄弟" },
    { type: "unit", name: "Wright Flyer", name_zh: "莱特兄弟飞行器" },
    { type: "person", name: "Charles Lindbergh", name_zh: "查尔斯·林白" },
    { type: "person", name: "Amelia Earhart", name_zh: "阿梅莉亚·埃尔哈特" },
  ],
  "relativity": [
    { type: "person", name: "Albert Einstein", name_zh: "阿尔伯特·爱因斯坦" },
    { type: "work", name: "On the Electrodynamics of Moving Bodies", name_zh: "《论动体的电动力学》" },
  ],
  "quantum-mechanics": [
    { type: "person", name: "Werner Heisenberg", name_zh: "维尔纳·海森堡" },
    { type: "person", name: "Erwin Schrödinger", name_zh: "埃尔温·薛定谔" },
    { type: "person", name: "Paul Dirac", name_zh: "保罗·狄拉克" },
    { type: "person", name: "Max Planck", name_zh: "马克斯·普朗克" },
    { type: "person", name: "Niels Bohr", name_zh: "尼尔斯·玻尔" },
  ],
  "radar": [
    { type: "person", name: "Robert Watson-Watt", name_zh: "罗伯特·沃森-瓦特" },
    { type: "wonder", name: "Chain Home", name_zh: "本土链雷达网" },
  ],
  "helicopter": [
    { type: "person", name: "Igor Sikorsky", name_zh: "伊戈尔·西科尔斯基" },
  ],
  "jet-engine": [
    { type: "person", name: "Frank Whittle", name_zh: "弗兰克·惠特尔" },
    { type: "person", name: "Hans von Ohain", name_zh: "汉斯·冯·奥海因" },
  ],
  "rocket": [
    { type: "person", name: "Wernher von Braun", name_zh: "维尔纳·冯·布劳恩" },
    { type: "person", name: "Robert H. Goddard", name_zh: "罗伯特·戈达德" },
    { type: "person", name: "Konstantin Tsiolkovsky", name_zh: "康斯坦丁·齐奥尔科夫斯基" },
    { type: "unit", name: "V-2 rocket", name_zh: "V-2火箭" },
    { type: "unit", name: "Saturn V", name_zh: "土星五号火箭" },
  ],
  "nuclear-fission": [
    { type: "person", name: "Lise Meitner", name_zh: "莉泽·迈特纳" },
    { type: "person", name: "Otto Hahn", name_zh: "奥托·哈恩" },
    { type: "person", name: "Enrico Fermi", name_zh: "恩里科·费米" },
    { type: "resource", name: "Uranium-235", name_zh: "铀-235" },
    { type: "resource", name: "Plutonium", name_zh: "钚" },
  ],
  "nuclear-weapon": [
    { type: "unit", name: "Little Boy", name_zh: "小男孩原子弹" },
    { type: "unit", name: "Fat Man", name_zh: "胖子原子弹" },
    { type: "person", name: "J. Robert Oppenheimer", name_zh: "罗伯特·奥本海默" },
    { type: "wonder", name: "Hiroshima & Nagasaki", name_zh: "广岛与长崎" },
  ],
  "nuclear-power": [
    { type: "wonder", name: "Obninsk Nuclear Power Plant", name_zh: "奥布宁斯克核电站" },
    { type: "wonder", name: "Chernobyl", name_zh: "切尔诺贝利" },
  ],
  "antibiotics": [
    { type: "person", name: "Alexander Fleming", name_zh: "亚历山大·弗莱明" },
    { type: "person", name: "Howard Florey", name_zh: "霍华德·弗洛里" },
    { type: "resource", name: "Penicillin", name_zh: "青霉素" },
    { type: "resource", name: "Streptomycin", name_zh: "链霉素" },
  ],
  "vaccines-modern": [
    { type: "person", name: "Jonas Salk", name_zh: "乔纳斯·索尔克" },
    { type: "person", name: "Albert Sabin", name_zh: "阿尔伯特·萨宾" },
    { type: "person", name: "Maurice Hilleman", name_zh: "莫里斯·希勒曼" },
  ],
  "dna-structure": [
    { type: "person", name: "James Watson", name_zh: "詹姆斯·沃森" },
    { type: "person", name: "Francis Crick", name_zh: "弗朗西斯·克里克" },
    { type: "person", name: "Rosalind Franklin", name_zh: "罗莎琳德·富兰克林" },
    { type: "person", name: "Maurice Wilkins", name_zh: "莫里斯·威尔金斯" },
    { type: "work", name: "Molecular Structure of Nucleic Acids", name_zh: "《核酸的分子结构》" },
  ],
  "synthetic-fertilizer": [
    { type: "person", name: "Fritz Haber", name_zh: "弗里茨·哈伯" },
    { type: "person", name: "Carl Bosch", name_zh: "卡尔·博施" },
    { type: "resource", name: "Ammonia", name_zh: "氨" },
  ],
  "green-revolution": [
    { type: "person", name: "Norman Borlaug", name_zh: "诺曼·布劳格" },
    { type: "plant", name: "Dwarf wheat", name_zh: "矮秆小麦" },
    { type: "plant", name: "IR8 rice", name_zh: "IR8水稻" },
  ],
  "plastic-polymer": [
    { type: "resource", name: "Bakelite", name_zh: "酚醛塑料" },
    { type: "resource", name: "Polyethylene", name_zh: "聚乙烯" },
    { type: "resource", name: "PVC", name_zh: "聚氯乙烯" },
    { type: "person", name: "Leo Baekeland", name_zh: "利奥·贝克兰" },
  ],
  "transistor": [
    { type: "person", name: "John Bardeen", name_zh: "约翰·巴丁" },
    { type: "person", name: "Walter Brattain", name_zh: "沃尔特·布拉顿" },
    { type: "person", name: "William Shockley", name_zh: "威廉·肖克利" },
    { type: "org", name: "Bell Labs", name_zh: "贝尔实验室" },
  ],
  "semiconductor": [
    { type: "person", name: "Jack Kilby", name_zh: "杰克·基尔比" },
    { type: "person", name: "Robert Noyce", name_zh: "罗伯特·诺伊斯" },
    { type: "org", name: "Fairchild Semiconductor", name_zh: "仙童半导体" },
    { type: "org", name: "Intel", name_zh: "英特尔" },
    { type: "org", name: "TSMC", name_zh: "台积电" },
  ],
  "digital-computer": [
    { type: "person", name: "Alan Turing", name_zh: "艾伦·图灵" },
    { type: "person", name: "John von Neumann", name_zh: "约翰·冯·诺依曼" },
    { type: "person", name: "Grace Hopper", name_zh: "葛丽丝·霍普" },
    { type: "unit", name: "ENIAC", name_zh: "埃尼阿克" },
    { type: "unit", name: "Colossus", name_zh: "巨人计算机" },
  ],
  "programming-language": [
    { type: "person", name: "John Backus", name_zh: "约翰·巴科斯" },
    { type: "person", name: "John McCarthy", name_zh: "约翰·麦卡锡" },
    { type: "person", name: "Dennis Ritchie", name_zh: "丹尼斯·里奇" },
    { type: "work", name: "Fortran", name_zh: "Fortran 语言" },
    { type: "work", name: "Lisp", name_zh: "Lisp 语言" },
    { type: "work", name: "C", name_zh: "C 语言" },
  ],
  "mainframe": [
    { type: "unit", name: "IBM System/360", name_zh: "IBM System/360" },
    { type: "org", name: "IBM", name_zh: "国际商业机器公司" },
  ],
  "television": [
    { type: "person", name: "Vladimir Zworykin", name_zh: "弗拉基米尔·兹沃利金" },
    { type: "person", name: "Philo Farnsworth", name_zh: "菲洛·法恩斯沃思" },
    { type: "org", name: "BBC", name_zh: "英国广播公司" },
    { type: "org", name: "RCA", name_zh: "美国无线电公司" },
  ],
  "satellite": [
    { type: "unit", name: "Sputnik 1", name_zh: "斯普特尼克一号" },
    { type: "unit", name: "Telstar", name_zh: "电星一号" },
    { type: "unit", name: "Hubble Space Telescope", name_zh: "哈勃太空望远镜" },
  ],
  "spaceflight": [
    { type: "person", name: "Yuri Gagarin", name_zh: "尤里·加加林" },
    { type: "person", name: "Valentina Tereshkova", name_zh: "瓦莲京娜·捷列什科娃" },
    { type: "unit", name: "Vostok 1", name_zh: "东方一号" },
  ],
  "moon-landing": [
    { type: "person", name: "Neil Armstrong", name_zh: "尼尔·阿姆斯特朗" },
    { type: "person", name: "Buzz Aldrin", name_zh: "巴兹·奥尔德林" },
    { type: "unit", name: "Apollo 11", name_zh: "阿波罗11号" },
    { type: "unit", name: "Saturn V", name_zh: "土星五号火箭" },
  ],
  "mass-media": [
    { type: "org", name: "BBC", name_zh: "英国广播公司" },
    { type: "org", name: "NBC", name_zh: "美国全国广播公司" },
    { type: "org", name: "CNN", name_zh: "有线电视新闻网" },
  ],
  "consumer-economy": [
    { type: "org", name: "Walmart", name_zh: "沃尔玛" },
    { type: "org", name: "Sears", name_zh: "西尔斯百货" },
  ],
  "credit-card": [
    { type: "org", name: "Visa", name_zh: "维萨" },
    { type: "org", name: "Mastercard", name_zh: "万事达" },
    { type: "org", name: "American Express", name_zh: "美国运通" },
  ],
  "container-shipping": [
    { type: "person", name: "Malcom McLean", name_zh: "马尔康·麦克莱恩" },
    { type: "unit", name: "Container ship", name_zh: "集装箱船" },
  ],
  "highway-system": [
    { type: "wonder", name: "Eisenhower Interstate System", name_zh: "艾森豪威尔州际公路系统" },
    { type: "wonder", name: "Autobahn", name_zh: "德国高速公路" },
  ],
  "welfare-state": [
    { type: "person", name: "William Beveridge", name_zh: "威廉·贝弗里奇" },
    { type: "work", name: "Beveridge Report", name_zh: "《贝弗里奇报告》" },
    { type: "org", name: "National Health Service (NHS)", name_zh: "国民保健服务" },
  ],
  "decolonization": [
    { type: "person", name: "Mahatma Gandhi", name_zh: "圣雄甘地" },
    { type: "person", name: "Kwame Nkrumah", name_zh: "夸梅·恩克鲁玛" },
    { type: "person", name: "Nelson Mandela", name_zh: "纳尔逊·曼德拉" },
  ],
  "united-nations": [
    { type: "org", name: "United Nations", name_zh: "联合国" },
    { type: "org", name: "International Monetary Fund", name_zh: "国际货币基金组织" },
    { type: "org", name: "World Bank", name_zh: "世界银行" },
    { type: "org", name: "WTO", name_zh: "世界贸易组织" },
  ],
  "birth-control": [
    { type: "person", name: "Margaret Sanger", name_zh: "玛格丽特·桑格" },
    { type: "person", name: "Carl Djerassi", name_zh: "卡尔·杰拉西" },
  ],
  "air-conditioning": [
    { type: "person", name: "Willis Carrier", name_zh: "威利斯·开利" },
    { type: "org", name: "Carrier Corporation", name_zh: "开利公司" },
  ],

  // ─── Information ─────────────────────────────────────────────
  "microprocessor": [
    { type: "unit", name: "Intel 4004", name_zh: "英特尔4004" },
    { type: "person", name: "Federico Faggin", name_zh: "费德里科·法金" },
    { type: "person", name: "Ted Hoff", name_zh: "泰德·霍夫" },
    { type: "org", name: "Intel", name_zh: "英特尔" },
  ],
  "advanced-chip-manufacturing": [
    { type: "org", name: "TSMC", name_zh: "台积电" },
    { type: "org", name: "ASML", name_zh: "阿斯麦" },
    { type: "org", name: "Samsung Foundry", name_zh: "三星代工" },
    { type: "org", name: "NVIDIA", name_zh: "英伟达" },
    { type: "person", name: "Morris Chang", name_zh: "张忠谋" },
    { type: "person", name: "Jensen Huang", name_zh: "黄仁勋" },
    { type: "unit", name: "EUV scanner (ASML NXE/EXE)", name_zh: "极紫外光刻机(ASML NXE/EXE)" },
    { type: "unit", name: "FinFET transistor", name_zh: "鳍式场效应晶体管(FinFET)" },
    { type: "unit", name: "Apple M-series chip", name_zh: "苹果M系列芯片" },
    { type: "unit", name: "NVIDIA H100 / Blackwell GPU", name_zh: "英伟达 H100 / Blackwell GPU" },
  ],
  "personal-computer": [
    { type: "unit", name: "Apple II", name_zh: "Apple II" },
    { type: "unit", name: "IBM PC", name_zh: "IBM PC" },
    { type: "unit", name: "Commodore 64", name_zh: "康懋达64" },
    { type: "person", name: "Steve Wozniak", name_zh: "史蒂夫·沃兹尼亚克" },
    { type: "person", name: "Steve Jobs", name_zh: "史蒂夫·乔布斯" },
    { type: "org", name: "Apple", name_zh: "苹果公司" },
    { type: "org", name: "Microsoft", name_zh: "微软" },
  ],
  "gui-mouse": [
    { type: "person", name: "Doug Engelbart", name_zh: "道格拉斯·恩格尔巴特" },
    { type: "person", name: "Alan Kay", name_zh: "艾伦·凯" },
    { type: "org", name: "Xerox PARC", name_zh: "施乐帕克研究中心" },
  ],
  "packet-switching": [
    { type: "person", name: "Paul Baran", name_zh: "保罗·巴兰" },
    { type: "person", name: "Donald Davies", name_zh: "唐纳德·戴维斯" },
    { type: "person", name: "Leonard Kleinrock", name_zh: "伦纳德·克兰罗克" },
  ],
  "arpanet-internet": [
    { type: "person", name: "Vint Cerf", name_zh: "文顿·瑟夫" },
    { type: "person", name: "Robert Kahn", name_zh: "罗伯特·卡恩" },
    { type: "org", name: "ARPA / DARPA", name_zh: "美国国防高等研究计划署" },
  ],
  "email": [
    { type: "person", name: "Ray Tomlinson", name_zh: "雷·汤姆林森" },
  ],
  "world-wide-web": [
    { type: "person", name: "Tim Berners-Lee", name_zh: "蒂姆·伯纳斯-李" },
    { type: "org", name: "CERN", name_zh: "欧洲核子研究组织" },
    { type: "work", name: "HTML", name_zh: "超文本标记语言" },
    { type: "work", name: "HTTP", name_zh: "超文本传输协议" },
  ],
  "search-engine": [
    { type: "person", name: "Larry Page", name_zh: "拉里·佩奇" },
    { type: "person", name: "Sergey Brin", name_zh: "谢尔盖·布林" },
    { type: "org", name: "Google", name_zh: "谷歌" },
    { type: "work", name: "PageRank", name_zh: "PageRank 算法" },
  ],
  "fiber-optic": [
    { type: "person", name: "Charles K. Kao", name_zh: "高锟" },
  ],
  "mobile-phone": [
    { type: "unit", name: "Motorola DynaTAC", name_zh: "摩托罗拉DynaTAC" },
    { type: "person", name: "Martin Cooper", name_zh: "马丁·库帕" },
  ],
  "smartphone": [
    { type: "unit", name: "iPhone", name_zh: "iPhone" },
    { type: "unit", name: "BlackBerry", name_zh: "黑莓" },
    { type: "unit", name: "Android", name_zh: "安卓" },
    { type: "person", name: "Steve Jobs", name_zh: "史蒂夫·乔布斯" },
    { type: "org", name: "Apple", name_zh: "苹果公司" },
    { type: "org", name: "Google", name_zh: "谷歌" },
  ],
  "social-media": [
    { type: "org", name: "Facebook (Meta)", name_zh: "Facebook(Meta)" },
    { type: "org", name: "Twitter (X)", name_zh: "Twitter(X)" },
    { type: "org", name: "TikTok", name_zh: "TikTok" },
    { type: "org", name: "YouTube", name_zh: "YouTube" },
    { type: "person", name: "Mark Zuckerberg", name_zh: "马克·扎克伯格" },
  ],
  "streaming-media": [
    { type: "org", name: "Netflix", name_zh: "奈飞" },
    { type: "org", name: "YouTube", name_zh: "YouTube" },
    { type: "org", name: "Spotify", name_zh: "Spotify" },
  ],
  "cloud-computing": [
    { type: "org", name: "Amazon Web Services (AWS)", name_zh: "亚马逊云服务(AWS)" },
    { type: "org", name: "Microsoft Azure", name_zh: "微软Azure" },
    { type: "org", name: "Google Cloud", name_zh: "谷歌云" },
  ],
  "ecommerce": [
    { type: "org", name: "Amazon", name_zh: "亚马逊" },
    { type: "org", name: "eBay", name_zh: "eBay" },
    { type: "org", name: "Alibaba", name_zh: "阿里巴巴" },
    { type: "person", name: "Jeff Bezos", name_zh: "杰夫·贝索斯" },
    { type: "person", name: "Jack Ma", name_zh: "马云" },
  ],
  "gps": [
    { type: "unit", name: "NAVSTAR satellite", name_zh: "NAVSTAR卫星" },
  ],
  "gene-sequencing": [
    { type: "wonder", name: "Human Genome Project", name_zh: "人类基因组计划" },
    { type: "person", name: "Frederick Sanger", name_zh: "弗雷德里克·桑格" },
    { type: "person", name: "Craig Venter", name_zh: "克雷格·文特尔" },
  ],
  "genetic-engineering": [
    { type: "person", name: "Paul Berg", name_zh: "保罗·伯格" },
    { type: "person", name: "Herbert Boyer", name_zh: "赫伯特·博耶" },
    { type: "person", name: "Stanley N. Cohen", name_zh: "斯坦利·科恩" },
    { type: "org", name: "Genentech", name_zh: "基因泰克" },
    { type: "resource", name: "Recombinant insulin", name_zh: "重组胰岛素" },
  ],
  "crispr": [
    { type: "person", name: "Jennifer Doudna", name_zh: "詹妮弗·杜德纳" },
    { type: "person", name: "Emmanuelle Charpentier", name_zh: "埃马纽埃尔·沙尔庞捷" },
    { type: "person", name: "Feng Zhang", name_zh: "张锋" },
  ],
  "mri-imaging": [
    { type: "person", name: "Paul Lauterbur", name_zh: "保罗·劳特伯" },
    { type: "person", name: "Peter Mansfield", name_zh: "彼得·曼斯菲尔德" },
  ],
  "ivf": [
    { type: "person", name: "Robert G. Edwards", name_zh: "罗伯特·爱德华兹" },
    { type: "person", name: "Patrick Steptoe", name_zh: "帕特里克·斯特普托" },
  ],
  "mrna-vaccine": [
    { type: "person", name: "Katalin Karikó", name_zh: "卡塔林·考里科" },
    { type: "person", name: "Drew Weissman", name_zh: "德鲁·韦斯曼" },
    { type: "org", name: "BioNTech", name_zh: "拜恩泰科" },
    { type: "org", name: "Moderna", name_zh: "莫德纳" },
  ],
  "solar-photovoltaic": [
    { type: "unit", name: "Photovoltaic cell", name_zh: "光伏电池" },
  ],
  "wind-turbine": [
    { type: "org", name: "Vestas", name_zh: "维斯塔斯" },
  ],
  "lithium-battery": [
    { type: "person", name: "John B. Goodenough", name_zh: "约翰·B·古迪纳夫" },
    { type: "person", name: "Akira Yoshino", name_zh: "吉野彰" },
    { type: "resource", name: "Lithium", name_zh: "锂" },
  ],
  "electric-vehicle": [
    { type: "unit", name: "Tesla Roadster", name_zh: "特斯拉Roadster跑车" },
    { type: "unit", name: "Tesla Model S", name_zh: "特斯拉Model S" },
    { type: "person", name: "Elon Musk", name_zh: "埃隆·马斯克" },
    { type: "org", name: "Tesla, Inc.", name_zh: "特斯拉公司" },
    { type: "org", name: "BYD", name_zh: "比亚迪" },
  ],
  "machine-learning": [
    { type: "person", name: "Geoffrey Hinton", name_zh: "杰弗里·辛顿" },
    { type: "person", name: "Yann LeCun", name_zh: "杨立昆" },
    { type: "person", name: "Yoshua Bengio", name_zh: "约书亚·本吉奥" },
  ],
  "deep-learning": [
    { type: "work", name: "AlexNet", name_zh: "AlexNet" },
    { type: "org", name: "DeepMind", name_zh: "DeepMind" },
    { type: "unit", name: "AlphaGo", name_zh: "AlphaGo" },
  ],
  "large-language-model": [
    { type: "org", name: "OpenAI", name_zh: "OpenAI" },
    { type: "org", name: "Anthropic", name_zh: "Anthropic" },
    { type: "org", name: "Google DeepMind", name_zh: "谷歌DeepMind" },
    { type: "unit", name: "ChatGPT", name_zh: "ChatGPT" },
    { type: "unit", name: "Claude", name_zh: "Claude" },
    { type: "work", name: "Attention Is All You Need", name_zh: "《Attention Is All You Need》" },
  ],
  "cryptocurrency": [
    { type: "resource", name: "Bitcoin", name_zh: "比特币" },
    { type: "resource", name: "Ether", name_zh: "以太币" },
    { type: "person", name: "Satoshi Nakamoto", name_zh: "中本聪" },
  ],
  "reusable-rocket": [
    { type: "org", name: "SpaceX", name_zh: "SpaceX" },
    { type: "unit", name: "Falcon 9", name_zh: "猎鹰9号" },
    { type: "unit", name: "Starship", name_zh: "星舰" },
    { type: "person", name: "Elon Musk", name_zh: "埃隆·马斯克" },
  ],
  "autonomous-vehicle": [
    { type: "org", name: "Waymo", name_zh: "Waymo" },
    { type: "org", name: "Cruise", name_zh: "Cruise" },
    { type: "org", name: "Tesla Autopilot", name_zh: "特斯拉Autopilot" },
  ],
  "3d-printing": [
    { type: "person", name: "Chuck Hull", name_zh: "查克·赫尔" },
  ],
  "robotics": [
    { type: "unit", name: "Unimate", name_zh: "Unimate(首台工业机器人)" },
    { type: "org", name: "Boston Dynamics", name_zh: "波士顿动力" },
    { type: "org", name: "iRobot", name_zh: "iRobot" },
  ],
  "quantum-computing": [
    { type: "org", name: "IBM Quantum", name_zh: "IBM量子" },
    { type: "org", name: "Google Quantum AI", name_zh: "谷歌量子AI" },
    { type: "unit", name: "Sycamore (Google)", name_zh: "悬铃木量子处理器" },
  ],
  "climate-science": [
    { type: "org", name: "IPCC", name_zh: "政府间气候变化专门委员会" },
    { type: "work", name: "Keeling Curve", name_zh: "基林曲线" },
    { type: "person", name: "Charles David Keeling", name_zh: "查尔斯·大卫·基林" },
  ],

  // ─── Military additions ───
  "tank": [
    { type: "unit", name: "Mark I tank", name_zh: "马克I型坦克" },
    { type: "unit", name: "T-34", name_zh: "T-34坦克" },
    { type: "unit", name: "M4 Sherman", name_zh: "M4谢尔曼坦克" },
    { type: "unit", name: "Tiger I", name_zh: "虎式坦克" },
    { type: "person", name: "J.F.C. Fuller", name_zh: "J·F·C·富勒" },
  ],
  "aircraft-carrier": [
    { type: "unit", name: "USS Langley (CV-1)", name_zh: "美国海军兰利号航空母舰" },
    { type: "unit", name: "USS Enterprise (CV-6)", name_zh: "企业号航空母舰" },
    { type: "unit", name: "HMS Hermes", name_zh: "赫尔墨斯号航空母舰" },
    { type: "wonder", name: "Battle of Midway", name_zh: "中途岛海战" },
  ],
  "submarine-warfare": [
    { type: "unit", name: "Type VII U-boat", name_zh: "VII型潜艇" },
    { type: "unit", name: "Type XXI U-boat", name_zh: "XXI型潜艇" },
    { type: "person", name: "Karl Dönitz", name_zh: "卡尔·邓尼茨" },
    { type: "unit", name: "Wolfpack tactics", name_zh: "狼群战术" },
  ],
  "thermonuclear-weapon": [
    { type: "unit", name: "Ivy Mike", name_zh: "常春藤·麦克氢弹试验" },
    { type: "unit", name: "Castle Bravo", name_zh: "城堡·布拉沃氢弹试验" },
    { type: "unit", name: "Tsar Bomba", name_zh: "沙皇炸弹" },
    { type: "person", name: "Edward Teller", name_zh: "爱德华·泰勒" },
    { type: "person", name: "Stanislaw Ulam", name_zh: "斯坦尼斯瓦夫·乌拉姆" },
    { type: "person", name: "Andrei Sakharov", name_zh: "安德烈·萨哈罗夫" },
  ],
  "icbm": [
    { type: "unit", name: "R-7 Semyorka", name_zh: "R-7火箭" },
    { type: "unit", name: "Atlas missile", name_zh: "宇宙神导弹" },
    { type: "unit", name: "Minuteman III", name_zh: "民兵III型导弹" },
    { type: "unit", name: "Polaris (submarine-launched)", name_zh: "北极星导弹" },
  ],
  "nuclear-submarine": [
    { type: "unit", name: "USS Nautilus (SSN-571)", name_zh: "鹦鹉螺号核潜艇" },
    { type: "unit", name: "USS George Washington (SSBN-598)", name_zh: "乔治·华盛顿号核潜艇" },
    { type: "unit", name: "Trident missile", name_zh: "三叉戟导弹" },
    { type: "person", name: "Hyman G. Rickover", name_zh: "海曼·G·里科弗" },
  ],
  "nuclear-aircraft-carrier": [
    { type: "unit", name: "USS Enterprise (CVN-65)", name_zh: "企业号核动力航母" },
    { type: "unit", name: "Nimitz class", name_zh: "尼米兹级航母" },
    { type: "unit", name: "Gerald R. Ford class", name_zh: "福特级航母" },
  ],
  "guided-missile": [
    { type: "unit", name: "AIM-9 Sidewinder", name_zh: "AIM-9响尾蛇导弹" },
    { type: "unit", name: "AIM-7 Sparrow", name_zh: "AIM-7麻雀导弹" },
    { type: "unit", name: "SA-2 Guideline", name_zh: "SA-2地空导弹" },
    { type: "unit", name: "BGM-71 TOW", name_zh: "BGM-71陶式反坦克导弹" },
  ],
  "precision-guided-munition": [
    { type: "unit", name: "Paveway laser-guided bomb", name_zh: "宝石路激光制导炸弹" },
    { type: "unit", name: "JDAM", name_zh: "联合直接攻击弹药(JDAM)" },
    { type: "unit", name: "Tomahawk cruise missile", name_zh: "战斧巡航导弹" },
    { type: "unit", name: "AGM-114 Hellfire", name_zh: "AGM-114地狱火导弹" },
  ],
  "stealth-aircraft": [
    { type: "unit", name: "F-117 Nighthawk", name_zh: "F-117夜鹰战斗机" },
    { type: "unit", name: "B-2 Spirit", name_zh: "B-2幽灵轰炸机" },
    { type: "person", name: "Ben Rich (Skunk Works)", name_zh: "本·里奇(臭鼬工厂)" },
    { type: "org", name: "Lockheed Skunk Works", name_zh: "洛克希德臭鼬工厂" },
  ],
  "drone-uav": [
    { type: "unit", name: "MQ-1 Predator", name_zh: "MQ-1捕食者无人机" },
    { type: "unit", name: "MQ-9 Reaper", name_zh: "MQ-9死神无人机" },
    { type: "unit", name: "RQ-4 Global Hawk", name_zh: "RQ-4全球鹰无人机" },
    { type: "unit", name: "Bayraktar TB2", name_zh: "拜拉克塔尔TB2无人机" },
    { type: "org", name: "General Atomics", name_zh: "通用原子能公司" },
  ],
  "fifth-gen-fighter": [
    { type: "unit", name: "F-22 Raptor", name_zh: "F-22猛禽战斗机" },
    { type: "unit", name: "F-35 Lightning II", name_zh: "F-35闪电II战斗机" },
    { type: "unit", name: "Sukhoi Su-57", name_zh: "苏-57战斗机" },
  ],
  "cyber-warfare": [
    { type: "unit", name: "Stuxnet", name_zh: "震网病毒" },
    { type: "unit", name: "NotPetya", name_zh: "NotPetya勒索软件" },
    { type: "org", name: "NSA TAO", name_zh: "美国国安局特定入侵行动办公室" },
    { type: "org", name: "Unit 8200", name_zh: "以色列8200部队" },
  ],
  "hypersonic-weapon": [
    { type: "unit", name: "Avangard", name_zh: "先锋高超音速导弹" },
    { type: "unit", name: "Hwasong-8", name_zh: "火星-8导弹" },
  ],

  // ─── Future Age + backfill prereqs ───
  "plasma-physics": [
    { type: "person", name: "Hannes Alfvén", name_zh: "汉尼斯·阿尔芬" },
    { type: "person", name: "Lyman Spitzer", name_zh: "莱曼·斯皮策" },
    { type: "unit", name: "Stellarator", name_zh: "仿星器" },
    { type: "unit", name: "Tokamak", name_zh: "托卡马克装置" },
  ],
  "neuroscience": [
    { type: "person", name: "Alan Hodgkin & Andrew Huxley", name_zh: "霍奇金与赫胥黎" },
    { type: "person", name: "Wilder Penfield", name_zh: "怀尔德·彭菲尔德" },
    { type: "person", name: "Eric Kandel", name_zh: "埃里克·坎德尔" },
    { type: "work", name: "Hodgkin–Huxley model", name_zh: "霍奇金-赫胥黎方程" },
  ],
  "gene-therapy": [
    { type: "person", name: "French Anderson", name_zh: "威廉·法兰奇·安德森" },
    { type: "unit", name: "Luxturna", name_zh: "Luxturna基因疗法" },
    { type: "unit", name: "Zolgensma", name_zh: "Zolgensma基因疗法" },
    { type: "unit", name: "Casgevy (CRISPR)", name_zh: "Casgevy(CRISPR疗法)" },
  ],
  "tissue-engineering": [
    { type: "person", name: "Robert Langer", name_zh: "罗伯特·兰格" },
    { type: "person", name: "Joseph Vacanti", name_zh: "约瑟夫·瓦坎蒂" },
    { type: "unit", name: "Vacanti mouse", name_zh: "瓦坎蒂老鼠" },
    { type: "person", name: "Anthony Atala", name_zh: "安东尼·阿塔拉" },
  ],
  "closed-loop-life-support": [
    { type: "wonder", name: "Biosphere 2", name_zh: "生物圈二号" },
    { type: "unit", name: "ISS ECLSS", name_zh: "国际空间站环境控制系统" },
    { type: "unit", name: "BIOS-3 (Soviet)", name_zh: "BIOS-3(苏联生命维持系统)" },
  ],
  "fusion-power": [
    { type: "org", name: "ITER", name_zh: "国际热核聚变实验堆" },
    { type: "org", name: "Commonwealth Fusion Systems", name_zh: "联邦聚变系统公司" },
    { type: "unit", name: "SPARC tokamak", name_zh: "SPARC托卡马克" },
    { type: "unit", name: "Joint European Torus (JET)", name_zh: "欧洲联合环面装置(JET)" },
    { type: "wonder", name: "National Ignition Facility", name_zh: "国家点火装置" },
  ],
  "humanoid-robot": [
    { type: "unit", name: "Atlas (Boston Dynamics)", name_zh: "阿特拉斯机器人(波士顿动力)" },
    { type: "unit", name: "Tesla Optimus", name_zh: "特斯拉Optimus" },
    { type: "unit", name: "Figure 02", name_zh: "Figure 02机器人" },
    { type: "unit", name: "Unitree H1", name_zh: "宇树H1机器人" },
    { type: "org", name: "Boston Dynamics", name_zh: "波士顿动力" },
  ],
  "agi": [
    { type: "org", name: "OpenAI", name_zh: "OpenAI" },
    { type: "org", name: "Anthropic", name_zh: "Anthropic" },
    { type: "org", name: "Google DeepMind", name_zh: "谷歌DeepMind" },
    { type: "person", name: "Demis Hassabis", name_zh: "戴密斯·哈萨比斯" },
    { type: "person", name: "Stuart Russell", name_zh: "斯图尔特·罗素" },
    { type: "person", name: "Nick Bostrom", name_zh: "尼克·博斯特罗姆" },
  ],
  "brain-computer-interface": [
    { type: "org", name: "Neuralink", name_zh: "Neuralink" },
    { type: "org", name: "Synchron", name_zh: "Synchron" },
    { type: "unit", name: "Utah array", name_zh: "犹他电极阵列" },
    { type: "unit", name: "N1 Implant (Neuralink)", name_zh: "N1脑机接口(Neuralink)" },
    { type: "person", name: "Miguel Nicolelis", name_zh: "米格尔·尼科莱利斯" },
  ],
  "moon-base": [
    { type: "org", name: "NASA Artemis program", name_zh: "NASA阿耳忒弥斯计划" },
    { type: "unit", name: "Lunar Gateway", name_zh: "月球门户空间站" },
    { type: "unit", name: "Artemis Base Camp", name_zh: "阿耳忒弥斯基地" },
    { type: "org", name: "International Lunar Research Station", name_zh: "国际月球科研站" },
  ],
  "mars-colony": [
    { type: "org", name: "SpaceX", name_zh: "SpaceX" },
    { type: "unit", name: "Starship", name_zh: "星舰" },
    { type: "person", name: "Elon Musk", name_zh: "埃隆·马斯克" },
    { type: "wonder", name: "Olympus Mons", name_zh: "奥林帕斯山" },
    { type: "plant", name: "Mars potato (The Martian)", name_zh: "火星马铃薯" },
  ],
  "asteroid-mining": [
    { type: "unit", name: "OSIRIS-REx mission", name_zh: "OSIRIS-REx任务" },
    { type: "unit", name: "Hayabusa2 mission", name_zh: "隼鸟2号任务" },
    { type: "wonder", name: "Asteroid 16 Psyche", name_zh: "16灵神星" },
    { type: "resource", name: "Platinum-group metals", name_zh: "铂族金属" },
    { type: "resource", name: "Asteroid water ice", name_zh: "小行星水冰" },
  ],
  "anti-aging": [
    { type: "org", name: "Altos Labs", name_zh: "Altos实验室" },
    { type: "org", name: "Calico (Alphabet)", name_zh: "Calico" },
    { type: "person", name: "Aubrey de Grey", name_zh: "奥布里·德格雷" },
    { type: "person", name: "David Sinclair", name_zh: "大卫·辛克莱" },
    { type: "unit", name: "Yamanaka factors (OSKM)", name_zh: "山中因子(OSKM)" },
  ],
  "lab-grown-meat": [
    { type: "org", name: "Eat Just (GOOD Meat)", name_zh: "Eat Just (GOOD Meat)" },
    { type: "org", name: "UPSIDE Foods", name_zh: "UPSIDE Foods" },
    { type: "person", name: "Mark Post", name_zh: "马克·波斯特" },
    { type: "unit", name: "Cultivated chicken", name_zh: "培育鸡肉" },
  ],
  "synthetic-biology": [
    { type: "person", name: "Craig Venter", name_zh: "克雷格·文特尔" },
    { type: "unit", name: "Synthetic Mycoplasma (JCVI-syn3.0)", name_zh: "合成支原体" },
    { type: "work", name: "AlphaFold", name_zh: "AlphaFold蛋白结构预测" },
    { type: "org", name: "Ginkgo Bioworks", name_zh: "Ginkgo Bioworks" },
    { type: "unit", name: "ESM3 protein model", name_zh: "ESM3蛋白质模型" },
  ],
  "room-temp-superconductor": [
    { type: "resource", name: "Lanthanum decahydride (LaH10)", name_zh: "氢化镧(LaH10)" },
    { type: "resource", name: "YBCO superconductor", name_zh: "钇钡铜氧超导体" },
    { type: "person", name: "Karl Müller", name_zh: "卡尔·米勒" },
    { type: "person", name: "J. Georg Bednorz", name_zh: "约翰内斯·贝德诺尔茨" },
  ],
  "nanotechnology": [
    { type: "person", name: "K. Eric Drexler", name_zh: "K·埃里克·德雷克斯勒" },
    { type: "person", name: "Richard Feynman", name_zh: "理查德·费曼" },
    { type: "work", name: "Engines of Creation", name_zh: "《创造的发动机》" },
    { type: "resource", name: "Carbon nanotube", name_zh: "碳纳米管" },
    { type: "resource", name: "Graphene", name_zh: "石墨烯" },
  ],
  "quantum-applications": [
    { type: "org", name: "IBM Quantum", name_zh: "IBM量子" },
    { type: "org", name: "Google Quantum AI", name_zh: "谷歌量子AI" },
    { type: "org", name: "IonQ", name_zh: "IonQ" },
    { type: "unit", name: "Shor's algorithm", name_zh: "秀尔算法" },
    { type: "unit", name: "Grover's algorithm", name_zh: "格罗弗算法" },
  ],
  "carbon-capture-scale": [
    { type: "org", name: "Climeworks", name_zh: "Climeworks" },
    { type: "unit", name: "Orca DAC plant", name_zh: "Orca碳捕集工厂" },
    { type: "unit", name: "Mammoth DAC plant", name_zh: "Mammoth碳捕集工厂" },
    { type: "org", name: "Carbon Engineering", name_zh: "Carbon Engineering" },
  ],
  "fusion-rocket": [
    { type: "unit", name: "Direct Fusion Drive", name_zh: "直接聚变驱动" },
    { type: "unit", name: "Daedalus probe (study)", name_zh: "代达罗斯探测器(研究)" },
    { type: "unit", name: "PFRC reactor", name_zh: "PFRC聚变反应堆" },
  ],
  "space-elevator": [
    { type: "person", name: "Konstantin Tsiolkovsky", name_zh: "康斯坦丁·齐奥尔科夫斯基" },
    { type: "person", name: "Yuri Artsutanov", name_zh: "尤里·阿尔楚塔诺夫" },
    { type: "person", name: "Bradley Edwards", name_zh: "布拉德利·爱德华兹" },
    { type: "resource", name: "Carbon nanotube cable", name_zh: "碳纳米管缆绳" },
  ],
  "post-scarcity": [
    { type: "person", name: "Peter Diamandis", name_zh: "彼得·迪亚曼迪斯" },
    { type: "work", name: "Abundance (book)", name_zh: "《富足》" },
    { type: "work", name: "Universal Basic Income", name_zh: "全民基本收入(UBI)" },
    { type: "person", name: "John Maynard Keynes (1930 essay)", name_zh: "凯恩斯(1930年论文)" },
  ],
  "digital-immortality": [
    { type: "person", name: "Hans Moravec", name_zh: "汉斯·莫拉维克" },
    { type: "person", name: "Ray Kurzweil", name_zh: "雷·库兹韦尔" },
    { type: "work", name: "The Singularity Is Near", name_zh: "《奇点临近》" },
    { type: "unit", name: "Whole-brain emulation", name_zh: "全脑仿真" },
  ],

  // ─── Future Age (social) ───
  "universal-basic-income": [
    { type: "person", name: "Andrew Yang", name_zh: "杨安泽" },
    { type: "person", name: "Milton Friedman (negative income tax)", name_zh: "米尔顿·弗里德曼" },
    { type: "org", name: "GiveDirectly", name_zh: "GiveDirectly" },
    { type: "unit", name: "Alaska Permanent Fund", name_zh: "阿拉斯加永久基金" },
    { type: "work", name: "Universal Basic Income (book, Van Parijs)", name_zh: "《全民基本收入》(范帕里斯)" },
  ],
  "liquid-democracy": [
    { type: "person", name: "Audrey Tang (Taiwan Digital Minister)", name_zh: "唐凤(台湾数字部长)" },
    { type: "unit", name: "vTaiwan platform", name_zh: "vTaiwan平台" },
    { type: "org", name: "e-Estonia", name_zh: "电子爱沙尼亚" },
    { type: "org", name: "Pirate Party", name_zh: "海盗党" },
    { type: "work", name: "Liquid Feedback (software)", name_zh: "Liquid Feedback软件" },
  ],
  "network-state": [
    { type: "person", name: "Balaji Srinivasan", name_zh: "巴拉吉·斯里尼瓦桑" },
    { type: "work", name: "The Network State (book)", name_zh: "《网络国家》" },
    { type: "unit", name: "Próspera (Honduras ZEDE)", name_zh: "普罗斯佩拉(洪都拉斯特区)" },
    { type: "unit", name: "Zuzalu (pop-up city)", name_zh: "Zuzalu(实验性城邦)" },
  ],
  "ai-governance": [
    { type: "unit", name: "Estonia AI judge (pilot)", name_zh: "爱沙尼亚AI法官(试点)" },
    { type: "work", name: "EU AI Act", name_zh: "欧盟人工智能法案" },
    { type: "org", name: "Singapore Smart Nation", name_zh: "新加坡智慧国家" },
    { type: "work", name: "Algorithmic Regulation (Tim O'Reilly)", name_zh: "《算法监管》(奥莱利)" },
  ],
  "transhumanism": [
    { type: "person", name: "Nick Bostrom", name_zh: "尼克·博斯特罗姆" },
    { type: "person", name: "Ray Kurzweil", name_zh: "雷·库兹韦尔" },
    { type: "person", name: "Max More", name_zh: "马克斯·摩尔" },
    { type: "person", name: "FM-2030", name_zh: "FM-2030" },
    { type: "org", name: "Humanity+ (WTA)", name_zh: "人类+协会" },
  ],
  "longtermism": [
    { type: "person", name: "Derek Parfit", name_zh: "德里克·帕菲特" },
    { type: "person", name: "Toby Ord", name_zh: "托比·奥德" },
    { type: "person", name: "William MacAskill", name_zh: "威廉·麦卡斯基尔" },
    { type: "work", name: "The Precipice (Ord, 2020)", name_zh: "《悬崖》(奥德,2020)" },
    { type: "work", name: "What We Owe the Future", name_zh: "《我们欠未来的》" },
    { type: "org", name: "80,000 Hours", name_zh: "80,000 Hours" },
  ],
  "generative-art": [
    { type: "org", name: "Midjourney", name_zh: "Midjourney" },
    { type: "unit", name: "Stable Diffusion", name_zh: "Stable Diffusion" },
    { type: "unit", name: "DALL-E", name_zh: "DALL·E" },
    { type: "unit", name: "Sora (OpenAI)", name_zh: "Sora(OpenAI)" },
    { type: "person", name: "Refik Anadol", name_zh: "雷菲克·阿纳多尔" },
    { type: "person", name: "Holly Herndon", name_zh: "霍莉·赫顿" },
  ],
  "metaverse": [
    { type: "work", name: "Snow Crash (Neal Stephenson)", name_zh: "《雪崩》(尼尔·斯蒂芬森)" },
    { type: "work", name: "Ready Player One", name_zh: "《头号玩家》" },
    { type: "org", name: "Meta Reality Labs", name_zh: "Meta现实实验室" },
    { type: "unit", name: "Apple Vision Pro", name_zh: "苹果Vision Pro" },
    { type: "unit", name: "VRChat", name_zh: "VRChat" },
  ],
  "decentralized-autonomous-org": [
    { type: "org", name: "MakerDAO", name_zh: "MakerDAO" },
    { type: "org", name: "Uniswap", name_zh: "Uniswap" },
    { type: "org", name: "ConstitutionDAO", name_zh: "ConstitutionDAO" },
    { type: "person", name: "Vitalik Buterin", name_zh: "维塔利克·布特林" },
    { type: "unit", name: "Smart contracts", name_zh: "智能合约" },
  ],

  // ─── Future Age (additional) ───
  "hyperloop": [
    { type: "work", name: "Hyperloop white paper (Musk 2013)", name_zh: "超回路列车白皮书" },
    { type: "org", name: "Virgin Hyperloop", name_zh: "维珍超回路" },
    { type: "org", name: "HyperloopTT", name_zh: "HyperloopTT" },
    { type: "org", name: "Boring Company", name_zh: "Boring公司" },
  ],
  "neuromorphic-chip": [
    { type: "unit", name: "Intel Loihi 2", name_zh: "英特尔Loihi 2" },
    { type: "unit", name: "IBM TrueNorth", name_zh: "IBM TrueNorth" },
    { type: "unit", name: "SpiNNaker (Manchester)", name_zh: "SpiNNaker(曼彻斯特)" },
    { type: "person", name: "Carver Mead", name_zh: "卡弗·米德" },
    { type: "org", name: "BrainChip", name_zh: "BrainChip公司" },
  ],
  "lab-grown-organs": [
    { type: "person", name: "Anthony Atala", name_zh: "安东尼·阿塔拉" },
    { type: "unit", name: "Lab-grown bladder (2006)", name_zh: "实验室培育膀胱" },
    { type: "org", name: "United Therapeutics", name_zh: "United Therapeutics" },
    { type: "unit", name: "Organoid", name_zh: "类器官" },
  ],
  "sentientism": [
    { type: "person", name: "Peter Singer", name_zh: "彼得·辛格" },
    { type: "work", name: "Animal Liberation (1975)", name_zh: "《动物解放》" },
    { type: "person", name: "Jeff Sebo", name_zh: "杰夫·塞博" },
    { type: "person", name: "Donald Watson", name_zh: "唐纳德·沃森" },
    { type: "org", name: "Open Philanthropy (animal welfare)", name_zh: "Open Philanthropy(动物福利)" },
  ],
  "dna-data-storage": [
    { type: "org", name: "Microsoft Research", name_zh: "微软研究院" },
    { type: "org", name: "Catalog Technologies", name_zh: "Catalog Technologies" },
    { type: "org", name: "Twist Bioscience", name_zh: "Twist Bioscience" },
    { type: "person", name: "George Church", name_zh: "乔治·丘奇" },
  ],
  "cancer-cure": [
    { type: "unit", name: "CAR-T cell therapy", name_zh: "CAR-T细胞疗法" },
    { type: "unit", name: "Keytruda (pembrolizumab)", name_zh: "Keytruda(派姆单抗)" },
    { type: "unit", name: "Personalized mRNA cancer vaccine", name_zh: "个性化mRNA癌症疫苗" },
    { type: "person", name: "James Allison", name_zh: "詹姆斯·艾利森" },
  ],
  "ai-judge": [
    { type: "unit", name: "COMPAS recidivism algorithm", name_zh: "COMPAS再犯预测算法" },
    { type: "unit", name: "Estonia AI judge (pilot)", name_zh: "爱沙尼亚AI法官(试点)" },
    { type: "work", name: "Weapons of Math Destruction", name_zh: "《数学杀伤性武器》" },
    { type: "person", name: "Cathy O'Neil", name_zh: "凯西·奥尼尔" },
  ],
  "space-based-solar": [
    { type: "org", name: "Caltech Space Solar Power Project", name_zh: "加州理工太空太阳能项目" },
    { type: "work", name: "SOLARIS (ESA)", name_zh: "SOLARIS(欧空局)" },
    { type: "person", name: "Peter Glaser (concept, 1968)", name_zh: "彼得·格拉泽" },
    { type: "unit", name: "Microwave power transmission", name_zh: "微波输电" },
  ],
  "photonic-computing": [
    { type: "org", name: "Lightmatter", name_zh: "Lightmatter" },
    { type: "org", name: "Lightelligence", name_zh: "Lightelligence" },
    { type: "unit", name: "Photonic tensor core", name_zh: "光子张量核" },
    { type: "org", name: "PsiQuantum", name_zh: "PsiQuantum" },
  ],
  "metamaterials": [
    { type: "person", name: "John Pendry", name_zh: "约翰·彭德里" },
    { type: "person", name: "David Smith", name_zh: "大卫·史密斯" },
    { type: "unit", name: "Cloaking device", name_zh: "隐身斗篷" },
    { type: "unit", name: "Negative refractive index lens", name_zh: "负折射率透镜" },
  ],
  "programmable-matter": [
    { type: "work", name: "Claytronics (CMU)", name_zh: "Claytronics项目(CMU)" },
    { type: "unit", name: "M-Blocks (MIT)", name_zh: "M-Blocks机器人模块" },
    { type: "person", name: "Seth Goldstein", name_zh: "塞斯·戈德斯坦" },
    { type: "person", name: "Daniela Rus", name_zh: "丹妮拉·罗斯" },
  ],
  "interstellar-probe": [
    { type: "unit", name: "Breakthrough Starshot", name_zh: "突破摄星计划" },
    { type: "person", name: "Yuri Milner", name_zh: "尤里·米尔纳" },
    { type: "person", name: "Stephen Hawking", name_zh: "史蒂芬·霍金" },
    { type: "unit", name: "Project Daedalus (1970s)", name_zh: "代达罗斯计划" },
    { type: "wonder", name: "Proxima Centauri b", name_zh: "比邻星b" },
  ],
  "terraforming-mars": [
    { type: "person", name: "Carl Sagan", name_zh: "卡尔·萨根" },
    { type: "person", name: "Robert Zubrin", name_zh: "罗伯特·祖布林" },
    { type: "work", name: "The Case for Mars", name_zh: "《赶往火星》" },
    { type: "unit", name: "Paraterraforming (worldhouse)", name_zh: "局部地球化(世界穹顶)" },
  ],

  // ─── Future Age (physics & math) ───
  "formal-mathematics": [
    { type: "unit", name: "Lean theorem prover", name_zh: "Lean证明助手" },
    { type: "unit", name: "Coq", name_zh: "Coq证明助手" },
    { type: "unit", name: "Mathlib", name_zh: "Mathlib数学库" },
    { type: "unit", name: "AlphaProof (DeepMind)", name_zh: "AlphaProof(DeepMind)" },
    { type: "person", name: "Terence Tao", name_zh: "陶哲轩" },
    { type: "person", name: "Peter Scholze", name_zh: "彼得·朔尔策" },
  ],
  "gravitational-wave-spectroscopy": [
    { type: "unit", name: "LIGO (advanced)", name_zh: "高级LIGO" },
    { type: "unit", name: "LISA (ESA-NASA)", name_zh: "LISA(欧空局-NASA)" },
    { type: "unit", name: "Einstein Telescope", name_zh: "爱因斯坦望远镜" },
    { type: "unit", name: "NANOGrav (pulsar timing)", name_zh: "NANOGrav脉冲星计时阵列" },
    { type: "person", name: "Kip Thorne", name_zh: "基普·索恩" },
    { type: "person", name: "Rainer Weiss", name_zh: "雷纳·韦斯" },
  ],
  "dark-sector-physics": [
    { type: "unit", name: "XENONnT detector", name_zh: "XENONnT探测器" },
    { type: "wonder", name: "Vera C. Rubin Observatory", name_zh: "薇拉·鲁宾天文台" },
    { type: "unit", name: "ADMX axion search", name_zh: "ADMX轴子探测" },
    { type: "person", name: "Vera Rubin (astronomer)", name_zh: "薇拉·鲁宾" },
    { type: "person", name: "Fritz Zwicky", name_zh: "弗里茨·兹威基" },
    { type: "work", name: "ΛCDM concordance cosmology", name_zh: "ΛCDM协调宇宙学" },
  ],
  "quantum-gravity": [
    { type: "work", name: "String theory", name_zh: "弦理论" },
    { type: "work", name: "Loop quantum gravity", name_zh: "圈量子引力" },
    { type: "person", name: "Edward Witten", name_zh: "爱德华·威滕" },
    { type: "person", name: "Roger Penrose", name_zh: "罗杰·彭罗斯" },
    { type: "person", name: "Carlo Rovelli", name_zh: "卡洛·罗韦利" },
    { type: "work", name: "AdS/CFT correspondence", name_zh: "反德西特/共形场论对偶" },
    { type: "person", name: "Juan Maldacena", name_zh: "胡安·马尔达塞纳" },
  ],
  "p-vs-np-resolved": [
    { type: "person", name: "Stephen Cook", name_zh: "斯蒂芬·库克" },
    { type: "person", name: "Leonid Levin", name_zh: "列昂尼德·列文" },
    { type: "work", name: "Cook–Levin theorem", name_zh: "库克-列文定理" },
    { type: "org", name: "Clay Mathematics Institute", name_zh: "克莱数学研究所" },
    { type: "work", name: "Millennium Prize Problems", name_zh: "千禧年大奖难题" },
  ],

  // ─── Future Age (mid-century) ───
  "space-habitat": [
    { type: "unit", name: "O'Neill cylinder", name_zh: "奥尼尔圆筒" },
    { type: "unit", name: "Stanford torus", name_zh: "斯坦福圆环" },
    { type: "unit", name: "Bernal sphere", name_zh: "贝尔纳球" },
    { type: "person", name: "Gerard K. O'Neill", name_zh: "杰拉德·K·奥尼尔" },
    { type: "org", name: "L5 Society", name_zh: "L5协会" },
    { type: "work", name: "The High Frontier (book)", name_zh: "《高边疆》" },
  ],
  "artificial-photosynthesis": [
    { type: "person", name: "Daniel Nocera", name_zh: "丹尼尔·诺切拉" },
    { type: "unit", name: "Artificial leaf", name_zh: "人工叶" },
    { type: "unit", name: "Bionic Leaf 2.0", name_zh: "仿生叶 2.0" },
    { type: "org", name: "Twelve (company)", name_zh: "Twelve公司" },
    { type: "org", name: "Synhelion", name_zh: "Synhelion" },
    { type: "org", name: "Air Company", name_zh: "Air Company" },
  ],
  "genetic-disease-eradication": [
    { type: "unit", name: "Casgevy (CRISPR therapy)", name_zh: "Casgevy(CRISPR疗法)" },
    { type: "unit", name: "Luxturna", name_zh: "Luxturna" },
    { type: "unit", name: "Zolgensma", name_zh: "Zolgensma" },
    { type: "unit", name: "Polygenic risk score", name_zh: "多基因风险评分" },
    { type: "person", name: "Jennifer Doudna", name_zh: "詹妮弗·杜德纳" },
  ],
  "self-replicating-machines": [
    { type: "person", name: "John von Neumann", name_zh: "约翰·冯·诺依曼" },
    { type: "person", name: "K. Eric Drexler", name_zh: "K·埃里克·德雷克斯勒" },
    { type: "person", name: "Robert Freitas", name_zh: "罗伯特·弗雷塔斯" },
    { type: "unit", name: "Universal constructor", name_zh: "通用构造机" },
    { type: "work", name: "NASA 1980 study (Lunar self-replicating factory)", name_zh: "NASA 1980年自复制工厂研究" },
  ],
  "superintelligence": [
    { type: "person", name: "I.J. Good", name_zh: "I·J·古德" },
    { type: "person", name: "Nick Bostrom", name_zh: "尼克·博斯特罗姆" },
    { type: "person", name: "Stuart Russell", name_zh: "斯图尔特·罗素" },
    { type: "person", name: "Eliezer Yudkowsky", name_zh: "埃利泽·尤德科夫斯基" },
    { type: "work", name: "Superintelligence: Paths, Dangers, Strategies", name_zh: "《超级智能》" },
    { type: "work", name: "AI alignment problem", name_zh: "AI对齐问题" },
  ],
  "seti-first-contact": [
    { type: "person", name: "Frank Drake", name_zh: "弗兰克·德雷克" },
    { type: "org", name: "SETI Institute", name_zh: "SETI研究所" },
    { type: "work", name: "Drake equation", name_zh: "德雷克方程" },
    { type: "work", name: "Fermi paradox", name_zh: "费米悖论" },
    { type: "org", name: "Breakthrough Listen", name_zh: "突破聆听计划" },
    { type: "unit", name: "Project Ozma (1960)", name_zh: "奥兹玛计划" },
  ],

  // ─── Far Future ───
  "dyson-swarm": [
    { type: "person", name: "Freeman Dyson", name_zh: "弗里曼·戴森" },
    { type: "unit", name: "Statite (solar sail)", name_zh: "光力悬浮卫星" },
    { type: "work", name: "Kardashev scale", name_zh: "卡尔达肖夫等级" },
    { type: "person", name: "Robert Bradbury", name_zh: "罗伯特·布拉德伯里" },
    { type: "work", name: "Search for Dyson sphere candidates (Tabby's star)", name_zh: "戴森球候选搜索(塔比之星)" },
  ],
  "matrioshka-brain": [
    { type: "person", name: "Robert Bradbury", name_zh: "罗伯特·布拉德伯里" },
    { type: "work", name: "Reversible computing", name_zh: "可逆计算" },
    { type: "work", name: "Landauer's principle", name_zh: "兰道尔原理" },
    { type: "unit", name: "Jupiter brain", name_zh: "木星之脑" },
  ],
  "stellar-engineering": [
    { type: "unit", name: "Shkadov thruster", name_zh: "希卡多夫推进器" },
    { type: "unit", name: "Star lifting", name_zh: "恒星采矿" },
    { type: "person", name: "Leonid Shkadov", name_zh: "列昂尼德·希卡多夫" },
    { type: "person", name: "David Criswell", name_zh: "大卫·克里斯韦尔" },
  ],
  "generation-ship-colony": [
    { type: "work", name: "Project Hyperion", name_zh: "海泊龙计划" },
    { type: "work", name: "100 Year Starship initiative", name_zh: "百年星舰计划" },
    { type: "unit", name: "Rama-class habitat (Clarke)", name_zh: "罗摩级栖息地(克拉克)" },
    { type: "wonder", name: "Proxima Centauri b", name_zh: "比邻星b" },
  ],
  "galactic-civilization": [
    { type: "work", name: "Kardashev Type III", name_zh: "卡尔达肖夫III型" },
    { type: "work", name: "Drake equation", name_zh: "德雷克方程" },
    { type: "work", name: "Fermi paradox", name_zh: "费米悖论" },
    { type: "work", name: "Great Filter", name_zh: "大过滤器" },
    { type: "person", name: "Carl Sagan (Cosmos)", name_zh: "卡尔·萨根(宇宙)" },
  ],
  "speciation": [
    { type: "person", name: "Stephen Hawking", name_zh: "史蒂芬·霍金" },
    { type: "person", name: "Cixin Liu", name_zh: "刘慈欣" },
    { type: "person", name: "Greg Egan", name_zh: "格雷格·伊根" },
    { type: "work", name: "The Diamond Age (Stephenson)", name_zh: "《钻石时代》" },
    { type: "work", name: "Cordwainer Smith's Underpeople", name_zh: "考德怀纳·史密斯笔下的下层人" },
  ],
  "substrate-independent-humanity": [
    { type: "person", name: "Hans Moravec", name_zh: "汉斯·莫拉维克" },
    { type: "person", name: "Ray Kurzweil", name_zh: "雷·库兹韦尔" },
    { type: "person", name: "Robin Hanson", name_zh: "罗宾·汉森" },
    { type: "work", name: "The Age of Em (book)", name_zh: "《模拟人类时代》" },
    { type: "work", name: "Whole brain emulation", name_zh: "全脑仿真" },
  ],
  "antimatter-production": [
    { type: "org", name: "CERN", name_zh: "欧洲核子研究组织" },
    { type: "unit", name: "Penning trap", name_zh: "潘宁离子阱" },
    { type: "unit", name: "Antihydrogen", name_zh: "反氢" },
    { type: "work", name: "Antimatter rocket", name_zh: "反物质火箭" },
    { type: "work", name: "AEgIS experiment", name_zh: "AEgIS实验" },
  ],
  "warp-drive": [
    { type: "person", name: "Miguel Alcubierre", name_zh: "米格尔·阿尔库别雷" },
    { type: "person", name: "Erik Lentz", name_zh: "埃里克·伦茨" },
    { type: "org", name: "NASA Eagleworks", name_zh: "NASA Eagleworks实验室" },
    { type: "work", name: "Krasnikov tube", name_zh: "克拉斯尼科夫管" },
    { type: "resource", name: "Negative-energy density (exotic matter)", name_zh: "负能量密度(奇异物质)" },
  ],
  "kardashev-type-ii": [
    { type: "person", name: "Nikolai Kardashev", name_zh: "尼古拉·卡尔达肖夫" },
    { type: "work", name: "Kardashev Type I (planetary)", name_zh: "卡尔达肖夫I型(行星级)" },
    { type: "work", name: "Kardashev Type II (stellar)", name_zh: "卡尔达肖夫II型(恒星级)" },
    { type: "person", name: "Carl Sagan (extension)", name_zh: "卡尔·萨根(扩展)" },
  ],
};
