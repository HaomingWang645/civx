// What each tech historically unlocks: resources, organisms, monuments, military
// units, creative works, organizations, and named historical figures.
// Each entry has English name + Chinese translation rendered in parentheses.
//
// Linking precedence per entry (see app.js renderer):
//   url:  "https://..."   → link to that arbitrary URL (use for things with no
//                            good Wikipedia article — e.g. recent products,
//                            company sites, mission pages)
//   wiki: false           → render as a flat non-link chip
//   wiki: "Article Title" → link directly to that Wikipedia article
//   (absent)              → default Wikipedia search by name

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
    { type: "person", name: "Australopithecus afarensis (Lucy)", name_zh: "南方古猿阿法种(露西)", wiki: "Australopithecus afarensis" },
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
    { type: "person", name: "Homo erectus (encephalization)", name_zh: "直立人(脑容量增大)", wiki: "Homo erectus" },
  ],
  "rockshelter-occupation": [
    { type: "wonder", name: "Wonderwerk Cave", name_zh: "奇迹洞", wiki: "Wonderwerk Cave" },
    { type: "wonder", name: "Zhoukoudian", name_zh: "周口店", wiki: "Peking Man Site" },
    { type: "wonder", name: "Atapuerca", name_zh: "阿塔普埃尔卡", wiki: "Atapuerca Mountains" },
  ],
  "cooperative-hunting": [
    { type: "wonder", name: "Boxgrove rhinoceros kill", name_zh: "博克斯格罗夫犀牛遗址", wiki: "Boxgrove Quarry" },
    { type: "wonder", name: "Schöningen horse hunt", name_zh: "舍宁根猎马场", wiki: "Schöningen spears" },
  ],

  // ─── Middle Paleolithic ──────────────────────────────────────
  "levallois": [
    { type: "person", name: "Homo sapiens", name_zh: "智人" },
    { type: "person", name: "Neanderthals", name_zh: "尼安德特人" },
  ],
  "pigments": [
    { type: "resource", name: "Red ochre", name_zh: "红赭石" },
    { type: "work", name: "Blombos engravings", name_zh: "布隆博斯洞穴刻画", wiki: "Blombos Cave" },
  ],
  "burial": [
    { type: "wonder", name: "Sungir burials", name_zh: "松吉尔遗址墓葬", wiki: "Sungir" },
  ],
  "early-bone-tools": [
    { type: "unit", name: "Lissoir (hide-burnisher)", name_zh: "皮革磨光器", wiki: "Lissoir (tool)" },
    { type: "wonder", name: "Pech-de-l'Azé site", name_zh: "佩什德拉泽遗址", wiki: "Pech de l'Azé" },
  ],
  "sling-stones": [
    { type: "unit", name: "Slinger", name_zh: "投石手", wiki: "Sling (weapon)" },
  ],
  "snares-traps": [
    { type: "unit", name: "Deadfall trap", name_zh: "压杀陷阱", wiki: "Deadfall trap" },
    { type: "unit", name: "Pit trap", name_zh: "陷坑", wiki: "Trapping" },
  ],

  // ─── Upper Paleolithic ───────────────────────────────────────
  "cave-art": [
    { type: "wonder", name: "Chauvet Cave", name_zh: "肖维岩洞" },
    { type: "wonder", name: "Lascaux", name_zh: "拉斯科洞窟" },
    { type: "wonder", name: "Altamira", name_zh: "阿尔塔米拉洞窟" },
    { type: "wonder", name: "Sulawesi cave paintings", name_zh: "苏拉威西洞穴画", wiki: "Caves in the Maros-Pangkep karst" },
  ],
  "flute": [
    { type: "work", name: "Divje Babe Flute", name_zh: "迪亚布巴贝骨笛" },
    { type: "work", name: "Hohle Fels flute", name_zh: "霍勒费尔斯骨笛" },
  ],
  "figurines": [
    { type: "work", name: "Venus of Willendorf", name_zh: "维伦多夫的维纳斯" },
    { type: "work", name: "Löwenmensch (Lion-man)", name_zh: "狮人雕像", wiki: "Lion-man" },
  ],
  "atlatl": [
    { type: "unit", name: "Atlatl darts", name_zh: "投矛器飞镖", wiki: "Spear-thrower" },
  ],
  "shamanism": [
    { type: "person", name: "Shaman", name_zh: "萨满" },
  ],
  "rafts": [
    { type: "wonder", name: "Settlement of Sahul (Australia)", name_zh: "萨胡尔大陆(澳大利亚)的定居", wiki: "Prehistory of Australia" },
  ],
  "tailored-clothing": [
    { type: "wonder", name: "Sungir beaded garments", name_zh: "松吉尔串珠服饰", wiki: "Sungir" },
    { type: "wonder", name: "Mal'ta–Buret' culture", name_zh: "马利他–布列季文化", wiki: "Mal'ta–Buret' culture" },
  ],
  "hide-tents": [
    { type: "wonder", name: "Pavlov tent rings", name_zh: "巴甫洛夫帐圈遗址", wiki: "Pavlov (Czech Republic)" },
    { type: "wonder", name: "Dolní Věstonice site", name_zh: "下维斯特罗尼采遗址", wiki: "Dolní Věstonice (archaeological site)" },
    { type: "unit", name: "Tipi", name_zh: "圆锥皮屋", wiki: "Tipi" },
  ],

  // ─── Mesolithic ──────────────────────────────────────────────
  "dog": [
    { type: "animal", name: "Dog (Canis lupus familiaris)", name_zh: "家犬", wiki: "Dog" },
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
  "wool-textiles": [
    { type: "resource", name: "Wool", name_zh: "羊毛" },
    { type: "animal", name: "Wool sheep", name_zh: "细毛绵羊", wiki: "Sheep" },
  ],
  "proto-cities": [
    { type: "wonder", name: "Çatalhöyük", name_zh: "加泰土丘", wiki: "Çatalhöyük" },
    { type: "wonder", name: "Tell es-Sultan (Jericho)", name_zh: "杰里科古城", wiki: "Tell es-Sultan" },
    { type: "wonder", name: "Mehrgarh", name_zh: "梅赫尔格爾", wiki: "Mehrgarh" },
  ],
  "defensive-walls": [
    { type: "wonder", name: "Tower of Jericho", name_zh: "杰里科塔", wiki: "Tower of Jericho" },
    { type: "wonder", name: "Walls of Jericho", name_zh: "杰里科城墙", wiki: "Walls of Jericho" },
  ],

  // ─── Bronze Age ──────────────────────────────────────────────
  "bronze-metallurgy": [
    { type: "resource", name: "Bronze", name_zh: "青铜" },
  ],
  "spoked-wheel": [
    { type: "unit", name: "Spoked-wheel cart", name_zh: "辐条轮战车", wiki: "Spoke" },
  ],
  "horse-domestication": [
    { type: "animal", name: "Horse", name_zh: "马" },
  ],
  "chariot": [
    { type: "unit", name: "War chariot", name_zh: "战车" },
    { type: "unit", name: "Hittite chariotry", name_zh: "赫梯战车队", wiki: "Battle of Kadesh" },
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
    { type: "person", name: "Enheduanna (earliest named author)", name_zh: "恩赫杜安娜(最早具名作者)", wiki: "Enheduanna" },
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
    { type: "unit", name: "Sumerian abacus", name_zh: "苏美尔算盘", wiki: "Abacus" },
  ],
  "astronomy-observation": [
    { type: "work", name: "Enuma Anu Enlil", name_zh: "《埃努玛·阿努·恩利尔》" },
    { type: "work", name: "MUL.APIN", name_zh: "《MUL.APIN》星表" },
  ],
  "solar-calendar": [
    { type: "work", name: "Egyptian civil calendar", name_zh: "埃及民用历" },
  ],
  "cartography": [
    { type: "wonder", name: "Babylonian World Map", name_zh: "巴比伦世界地图", wiki: "Imago Mundi (Babylonian map)" },
    { type: "person", name: "Anaximander", name_zh: "阿那克西曼德", wiki: "Anaximander" },
    { type: "person", name: "Eratosthenes", name_zh: "埃拉托色尼", wiki: "Eratosthenes" },
    { type: "person", name: "Ptolemy", name_zh: "托勒密", wiki: "Ptolemy" },
    { type: "work", name: "Geographia (Ptolemy)", name_zh: "《地理学》(托勒密)", wiki: "Geography (Ptolemy)" },
  ],
  "monumental-architecture": [
    { type: "wonder", name: "Stepped temples", name_zh: "阶梯式神庙", wiki: "Step pyramid" },
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
    { type: "unit", name: "Akkadian infantry", name_zh: "阿卡德步兵", wiki: "Akkadian Empire" },
    { type: "person", name: "Sargon of Akkad", name_zh: "阿卡德的萨尔贡" },
  ],
  "maritime-trade": [
    { type: "wonder", name: "Tyre", name_zh: "提尔" },
    { type: "wonder", name: "Byblos", name_zh: "比布鲁斯" },
  ],
  "galley-ship": [
    { type: "unit", name: "Phoenician bireme", name_zh: "腓尼基双层桨座船", wiki: "Bireme" },
  ],
  "proto-medicine": [
    { type: "work", name: "Edwin Smith Papyrus", name_zh: "《埃德温·史密斯纸草》" },
    { type: "work", name: "Diagnostic Handbook (Esagil-kin-apli)", name_zh: "《诊断手册》(埃萨吉尔-金-阿普利)", wiki: "Esagil-kin-apli" },
  ],
  "tin-mining": [
    { type: "resource", name: "Cassiterite", name_zh: "锡石", wiki: "Cassiterite" },
    { type: "wonder", name: "Cornwall tin mines", name_zh: "康沃尔锡矿", wiki: "Mining in Cornwall and Devon" },
    { type: "wonder", name: "Uluburun shipwreck cargo", name_zh: "乌鲁布伦沉船货物", wiki: "Uluburun shipwreck" },
  ],
  "weights-measures": [
    { type: "unit", name: "Indus Valley cubic weights", name_zh: "印度河流域立方砝码", wiki: "Indus Valley civilisation" },
    { type: "unit", name: "Mesopotamian shekel & mina", name_zh: "美索不达米亚舍客勒与米那", wiki: "Shekel" },
    { type: "unit", name: "Egyptian deben", name_zh: "古埃及德本", wiki: "Deben (unit)" },
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
    { type: "resource", name: "Lydian electrum coin", name_zh: "吕底亚琥珀金币", wiki: "Electrum" },
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
    { type: "wonder", name: "Persian Royal Road", name_zh: "波斯御道", wiki: "Royal Road" },
    { type: "wonder", name: "Silk Road", name_zh: "丝绸之路" },
  ],
  "postal-system": [
    { type: "org", name: "Persian angarium (Royal Road couriers)", name_zh: "波斯御道驿传", wiki: "Angarium" },
    { type: "org", name: "Cursus publicus", name_zh: "罗马帝国邮政", wiki: "Cursus publicus" },
    { type: "org", name: "Mongol Yam", name_zh: "蒙古驿站", wiki: "Yam (route)" },
    { type: "person", name: "Cyrus the Great", name_zh: "居鲁士大帝", wiki: "Cyrus the Great" },
    { type: "person", name: "Augustus (cursus publicus founder)", name_zh: "奥古斯都(罗马邮政创立者)", wiki: "Augustus" },
  ],
  "aqueduct": [
    { type: "wonder", name: "Pont du Gard", name_zh: "加尔桥" },
    { type: "wonder", name: "Aqua Claudia", name_zh: "克劳狄渡槽" },
  ],
  "arch-vault": [
    { type: "wonder", name: "Pantheon (dome)", name_zh: "万神殿(穹顶)", wiki: "Pantheon, Rome" },
    { type: "wonder", name: "Colosseum", name_zh: "罗马斗兽场" },
  ],
  "concrete-roman": [
    { type: "resource", name: "Pozzolana cement", name_zh: "火山灰水泥" },
    { type: "wonder", name: "Pantheon dome", name_zh: "万神殿穹顶", wiki: "Pantheon, Rome" },
  ],
  "crossbow": [
    { type: "unit", name: "Han dynasty crossbowman", name_zh: "汉朝弩兵", wiki: "Military of the Han dynasty" },
  ],
  "siege-engine": [
    { type: "unit", name: "Catapult", name_zh: "投石机" },
    { type: "unit", name: "Ballista", name_zh: "弩炮" },
    { type: "unit", name: "Battering ram", name_zh: "攻城槌" },
  ],
  "cavalry": [
    { type: "unit", name: "Cataphract", name_zh: "重甲骑兵" },
    { type: "unit", name: "Persian Immortal", name_zh: "波斯不死军", wiki: "Immortals (Achaemenid Empire)" },
  ],
  "saddle-stirrup": [
    { type: "unit", name: "Heavy cavalry", name_zh: "重骑兵" },
  ],
  "silk-production": [
    { type: "animal", name: "Silkworm (Bombyx mori)", name_zh: "家蚕", wiki: "Bombyx mori" },
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
    { type: "wonder", name: "Library of Pergamon", name_zh: "帕加马图书馆", wiki: "Library of Pergamum" },
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
    { type: "unit", name: "Athenian trireme", name_zh: "雅典三列桨战船", wiki: "Trireme" },
    { type: "person", name: "Themistocles", name_zh: "地米斯托克利" },
  ],
  "gear-mechanism": [
    { type: "work", name: "Antikythera mechanism", name_zh: "安提基特拉机械" },
    { type: "person", name: "Hero of Alexandria", name_zh: "亚历山大里亚的希罗" },
  ],
  "woodblock-printing": [
    { type: "work", name: "Diamond Sutra", name_zh: "《金刚经》" },
  ],
  "parchment-vellum": [
    { type: "wonder", name: "Library of Pergamon", name_zh: "佩加蒙图书馆", wiki: "Library of Pergamum" },
    { type: "work", name: "Codex Sinaiticus", name_zh: "《西奈抄本》", wiki: "Codex Sinaiticus" },
  ],
  "theatre-drama": [
    { type: "wonder", name: "Theatre of Dionysus", name_zh: "狄俄尼索斯剧场", wiki: "Theatre of Dionysus" },
    { type: "person", name: "Aeschylus", name_zh: "埃斯库罗斯", wiki: "Aeschylus" },
    { type: "person", name: "Sophocles", name_zh: "索福克勒斯", wiki: "Sophocles" },
    { type: "person", name: "Euripides", name_zh: "欧里庇得斯", wiki: "Euripides" },
    { type: "person", name: "Aristophanes", name_zh: "阿里斯托芬", wiki: "Aristophanes" },
    { type: "work", name: "Oresteia", name_zh: "《俄瑞斯忒亚》", wiki: "Oresteia" },
    { type: "work", name: "Natyasastra", name_zh: "《舞论》", wiki: "Natya Shastra" },
  ],
  "codex": [
    { type: "work", name: "Codex Sinaiticus", name_zh: "《西奈抄本》", wiki: "Codex Sinaiticus" },
    { type: "work", name: "Codex Vaticanus", name_zh: "《梵蒂冈抄本》", wiki: "Codex Vaticanus" },
    { type: "work", name: "Vergilius Vaticanus", name_zh: "《梵蒂冈维吉尔抄本》", wiki: "Vergilius Vaticanus" },
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
    { type: "unit", name: "Heavy plow team", name_zh: "重犁畜队", wiki: "Carruca" },
  ],
  "university": [
    { type: "wonder", name: "University of Bologna", name_zh: "博洛尼亚大学" },
    { type: "wonder", name: "University of Paris", name_zh: "巴黎大学" },
    { type: "wonder", name: "Oxford", name_zh: "牛津大学", wiki: "University of Oxford" },
    { type: "wonder", name: "Al-Qarawiyyin", name_zh: "卡鲁因大学", wiki: "University of al-Qarawiyyin" },
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
    { type: "unit", name: "Knight (man-at-arms)", name_zh: "骑士(重装战士)", wiki: "Man-at-arms" },
    { type: "org", name: "Knights Templar", name_zh: "圣殿骑士团" },
    { type: "org", name: "Knights Hospitaller", name_zh: "医院骑士团" },
  ],
  "longbow": [
    { type: "unit", name: "English longbowman", name_zh: "英格兰长弓手", wiki: "English longbow" },
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
    { type: "wonder", name: "Bimaristan al-Mansuri", name_zh: "曼苏里医院", wiki: "Bimaristan" },
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
  "astrolabe": [
    { type: "person", name: "Hipparchus", name_zh: "喜帕恰斯", wiki: "Hipparchus" },
    { type: "person", name: "al-Khwarizmi", name_zh: "花剌子米", wiki: "Al-Khwarizmi" },
    { type: "person", name: "al-Zarqali", name_zh: "扎尔卡利", wiki: "Al-Zarqali" },
    { type: "unit", name: "Planispheric astrolabe", name_zh: "平面星盘", wiki: "Astrolabe" },
    { type: "unit", name: "Mariner's astrolabe", name_zh: "航海星盘", wiki: "Mariner's astrolabe" },
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
    { type: "wonder", name: "Fabriano paper mill", name_zh: "法布里亚诺造纸厂", wiki: "Paper and Watermark Museum" },
  ],
  "polyphony-notation": [
    { type: "person", name: "Guido of Arezzo", name_zh: "圭多·达莱佐", wiki: "Guido of Arezzo" },
    { type: "person", name: "Léonin", name_zh: "莱奥南", wiki: "Léonin" },
    { type: "person", name: "Pérotin", name_zh: "佩罗坦", wiki: "Pérotin" },
    { type: "work", name: "Magnus Liber Organi", name_zh: "《大奥尔加农曲集》", wiki: "Magnus Liber" },
  ],
  "plate-armor": [
    { type: "unit", name: "Man-at-arms (full plate)", name_zh: "重装板甲骑兵", wiki: "Man-at-arms" },
    { type: "person", name: "Missaglia armory family", name_zh: "米萨利亚兵器家族", wiki: "Missaglia" },
    { type: "wonder", name: "Gothic armour", name_zh: "哥特式板甲", wiki: "Gothic plate armour" },
  ],
  "crank-connecting-rod": [
    { type: "unit", name: "Water-powered sawmill", name_zh: "水力锯木机", wiki: "Sawmill" },
    { type: "unit", name: "Treadle lathe", name_zh: "踏板车床", wiki: "Lathe" },
    { type: "person", name: "Villard de Honnecourt", name_zh: "维亚尔·德·奥内库尔", wiki: "Villard de Honnecourt" },
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
    { type: "work", name: "On Painting (Della pittura)", name_zh: "《论绘画》", wiki: "De pictura" },
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
  "patent-system": [
    { type: "work", name: "Venetian Patent Statute (1474)", name_zh: "《威尼斯专利法》", wiki: "Venetian Patent Statute" },
    { type: "work", name: "Statute of Monopolies (1624)", name_zh: "《英国垄断法》", wiki: "Statute of Monopolies" },
    { type: "work", name: "U.S. Patent Act (1790)", name_zh: "《美国专利法》(1790)", wiki: "Patent Act of 1790" },
    { type: "org", name: "U.S. Patent and Trademark Office", name_zh: "美国专利商标局", wiki: "United States Patent and Trademark Office" },
    { type: "org", name: "World Intellectual Property Organization", name_zh: "世界知识产权组织", wiki: "World Intellectual Property Organization" },
  ],
  "stock-exchange": [
    { type: "org", name: "Amsterdam Stock Exchange", name_zh: "阿姆斯特丹证券交易所", wiki: "Amsterdam Stock Exchange" },
    { type: "org", name: "London Stock Exchange", name_zh: "伦敦证券交易所", wiki: "London Stock Exchange" },
    { type: "org", name: "New York Stock Exchange", name_zh: "纽约证券交易所", wiki: "New York Stock Exchange" },
    { type: "work", name: "Buttonwood Agreement (1792)", name_zh: "《梧桐树协议》", wiki: "Buttonwood Agreement" },
    { type: "person", name: "Joseph de la Vega", name_zh: "约瑟夫·德·拉·维加", wiki: "Joseph de la Vega" },
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
    { type: "wonder", name: "Hispaniola landing", name_zh: "伊斯帕尼奥拉岛登陆", wiki: "Hispaniola" },
  ],
  "colonialism": [
    { type: "person", name: "Hernán Cortés", name_zh: "埃尔南·科尔特斯" },
    { type: "person", name: "Francisco Pizarro", name_zh: "弗朗西斯科·皮萨罗" },
  ],
  "columbian-exchange": [
    { type: "plant", name: "Potato", name_zh: "马铃薯" },
    { type: "plant", name: "Tomato", name_zh: "番茄" },
    { type: "plant", name: "Maize", name_zh: "玉米" },
    { type: "plant", name: "Cacao (chocolate)", name_zh: "可可(巧克力)", wiki: "Theobroma cacao" },
    { type: "plant", name: "Tobacco", name_zh: "烟草" },
    { type: "plant", name: "Chili pepper", name_zh: "辣椒" },
    { type: "plant", name: "Vanilla", name_zh: "香草" },
    { type: "animal", name: "Horse (to Americas)", name_zh: "马(传入美洲)", wiki: "Mustang" },
    { type: "animal", name: "Cattle (to Americas)", name_zh: "牛(传入美洲)", wiki: "Criollo cattle" },
  ],
  "musket": [
    { type: "unit", name: "Matchlock musketeer", name_zh: "火绳枪兵", wiki: "Matchlock" },
    { type: "unit", name: "Spanish tercio", name_zh: "西班牙方阵" },
  ],
  "artillery": [
    { type: "unit", name: "Field cannon", name_zh: "野战炮", wiki: "Field artillery" },
  ],
  "bastion-fortification": [
    { type: "wonder", name: "Star fort of Naarden", name_zh: "纳尔登星形要塞", wiki: "Naarden" },
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
    { type: "resource", name: "Oxygen (named)", name_zh: "氧(命名)", wiki: "Oxygen" },
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
    { type: "person", name: "Charles Townshend", name_zh: "查尔斯·汤森", wiki: "Charles Townshend, 2nd Viscount Townshend" },
  ],
  "selective-breeding": [
    { type: "person", name: "Robert Bakewell", name_zh: "罗伯特·贝克韦尔" },
    { type: "animal", name: "Dishley Leicester sheep", name_zh: "迪希莱-莱斯特绵羊", wiki: "Leicester Longwool" },
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
    { type: "person", name: "William Morton", name_zh: "威廉·莫顿", wiki: "William T. G. Morton" },
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
    { type: "person", name: "John H. Hall", name_zh: "约翰·H·霍尔", wiki: "John H. Hall (gunsmith)" },
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
    { type: "org", name: "American Federation of Labor (AFL)", name_zh: "美国劳工联合会", wiki: "American Federation of Labor" },
    { type: "org", name: "Trades Union Congress", name_zh: "英国职工大会" },
  ],
  "newspaper-mass": [
    { type: "org", name: "The New York Sun", name_zh: "《纽约太阳报》", wiki: "The Sun (New York City)" },
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
  "aluminum-smelting": [
    { type: "person", name: "Charles Martin Hall", name_zh: "查尔斯·马丁·霍尔", wiki: "Charles Martin Hall" },
    { type: "person", name: "Paul Héroult", name_zh: "保罗·埃鲁", wiki: "Paul Héroult" },
    { type: "resource", name: "Aluminum", name_zh: "铝", wiki: "Aluminium" },
    { type: "resource", name: "Bauxite", name_zh: "铝土矿", wiki: "Bauxite" },
    { type: "resource", name: "Cryolite", name_zh: "冰晶石", wiki: "Cryolite" },
    { type: "org", name: "Alcoa", name_zh: "美国铝业公司", wiki: "Alcoa" },
  ],
  "electric-lighting": [
    { type: "person", name: "Thomas Edison", name_zh: "托马斯·爱迪生", wiki: "Thomas Edison" },
    { type: "person", name: "Joseph Swan", name_zh: "约瑟夫·斯旺", wiki: "Joseph Swan" },
    { type: "unit", name: "Incandescent light bulb", name_zh: "白炽灯泡", wiki: "Incandescent light bulb" },
    { type: "wonder", name: "Pearl Street Station", name_zh: "珍珠街发电站", wiki: "Pearl Street Station" },
    { type: "org", name: "General Electric", name_zh: "通用电气", wiki: "General Electric" },
  ],
  "submarine": [
    { type: "unit", name: "USS Holland (SS-1)", name_zh: "霍兰号潜艇", wiki: "USS Holland (SS-1)" },
    { type: "unit", name: "U-boat", name_zh: "U型潜艇", wiki: "U-boat" },
    { type: "unit", name: "H. L. Hunley", name_zh: "亨利·L·亨利号潜艇", wiki: "H. L. Hunley (submarine)" },
    { type: "person", name: "John Philip Holland", name_zh: "约翰·菲利普·霍兰", wiki: "John Philip Holland" },
  ],
  "sewing-machine": [
    { type: "person", name: "Elias Howe", name_zh: "伊莱亚斯·豪", wiki: "Elias Howe" },
    { type: "person", name: "Isaac Singer", name_zh: "艾萨克·辛格", wiki: "Isaac Singer" },
    { type: "org", name: "Singer Corporation", name_zh: "胜家公司", wiki: "Singer Corporation" },
    { type: "unit", name: "Lockstitch sewing machine", name_zh: "锁式缝纫机", wiki: "Lockstitch" },
  ],
  "phonograph": [
    { type: "person", name: "Thomas Edison", name_zh: "托马斯·爱迪生", wiki: "Thomas Edison" },
    { type: "person", name: "Emile Berliner", name_zh: "埃米尔·柏林纳", wiki: "Emile Berliner" },
    { type: "unit", name: "Tinfoil cylinder phonograph", name_zh: "锡箔圆筒留声机", wiki: "Phonograph cylinder" },
    { type: "unit", name: "Gramophone disc", name_zh: "圆盘留声机", wiki: "Phonograph record" },
    { type: "org", name: "Victor Talking Machine Company", name_zh: "胜利留声机公司", wiki: "Victor Talking Machine Company" },
  ],
  "impressionism": [
    { type: "person", name: "Claude Monet", name_zh: "克劳德·莫奈", wiki: "Claude Monet" },
    { type: "person", name: "Pierre-Auguste Renoir", name_zh: "皮埃尔-奥古斯特·雷诺阿", wiki: "Pierre-Auguste Renoir" },
    { type: "person", name: "Edgar Degas", name_zh: "埃德加·德加", wiki: "Edgar Degas" },
    { type: "person", name: "Camille Pissarro", name_zh: "卡米耶·毕沙罗", wiki: "Camille Pissarro" },
    { type: "person", name: "Berthe Morisot", name_zh: "贝尔特·莫里索", wiki: "Berthe Morisot" },
    { type: "work", name: "Impression, Sunrise", name_zh: "《日出·印象》", wiki: "Impression, Sunrise" },
    { type: "work", name: "Water Lilies (Monet series)", name_zh: "《睡莲》系列", wiki: "Water Lilies (Monet series)" },
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
    { type: "wonder", name: "Hiroshima & Nagasaki", name_zh: "广岛与长崎", wiki: "Atomic bombings of Hiroshima and Nagasaki" },
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
  "organ-transplant": [
    { type: "person", name: "Joseph Murray", name_zh: "约瑟夫·默里", wiki: "Joseph Murray" },
    { type: "person", name: "Christiaan Barnard", name_zh: "克里斯蒂安·巴纳德", wiki: "Christiaan Barnard" },
    { type: "person", name: "Alexis Carrel", name_zh: "亚历克西·卡雷尔", wiki: "Alexis Carrel" },
    { type: "resource", name: "Cyclosporine", name_zh: "环孢素", wiki: "Ciclosporin" },
    { type: "resource", name: "Tacrolimus", name_zh: "他克莫司", wiki: "Tacrolimus" },
    { type: "work", name: "HLA matching", name_zh: "人类白细胞抗原配型", wiki: "Human leukocyte antigen" },
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
    { type: "plant", name: "IR8 rice", name_zh: "IR8水稻", wiki: "IR8" },
  ],
  "plastic-polymer": [
    { type: "resource", name: "Bakelite", name_zh: "酚醛塑料" },
    { type: "resource", name: "Polyethylene", name_zh: "聚乙烯" },
    { type: "resource", name: "PVC", name_zh: "聚氯乙烯" },
    { type: "person", name: "Leo Baekeland", name_zh: "利奥·贝克兰" },
  ],
  "synthetic-fibers": [
    { type: "resource", name: "Nylon", name_zh: "尼龙", wiki: "Nylon" },
    { type: "resource", name: "Rayon", name_zh: "人造丝", wiki: "Rayon" },
    { type: "resource", name: "Polyester", name_zh: "聚酯纤维", wiki: "Polyester" },
    { type: "resource", name: "Spandex", name_zh: "氨纶", wiki: "Spandex" },
    { type: "person", name: "Wallace Carothers", name_zh: "华莱士·卡罗瑟斯", wiki: "Wallace Carothers" },
    { type: "org", name: "DuPont", name_zh: "杜邦公司", wiki: "DuPont" },
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
  "laser": [
    { type: "person", name: "Theodore Maiman", name_zh: "西奥多·梅曼", wiki: "Theodore Maiman" },
    { type: "person", name: "Charles Townes", name_zh: "查尔斯·汤斯", wiki: "Charles H. Townes" },
    { type: "unit", name: "Ruby laser", name_zh: "红宝石激光器", wiki: "Ruby laser" },
    { type: "unit", name: "Helium–neon laser", name_zh: "氦氖激光器", wiki: "Helium–neon laser" },
    { type: "unit", name: "Semiconductor laser diode", name_zh: "半导体激光二极管", wiki: "Laser diode" },
  ],
  "plate-tectonics": [
    { type: "person", name: "Harry Hess", name_zh: "哈里·赫斯", wiki: "Harry Hammond Hess" },
    { type: "person", name: "J. Tuzo Wilson", name_zh: "约翰·图佐·威尔逊", wiki: "J. Tuzo Wilson" },
    { type: "person", name: "Frederick Vine", name_zh: "弗雷德里克·瓦因", wiki: "Frederick Vine" },
    { type: "person", name: "Drummond Matthews", name_zh: "德拉蒙德·马修斯", wiki: "Drummond Matthews" },
    { type: "person", name: "W. Jason Morgan", name_zh: "杰森·摩根", wiki: "W. Jason Morgan" },
    { type: "wonder", name: "Mid-Atlantic Ridge", name_zh: "大西洋中脊", wiki: "Mid-Atlantic Ridge" },
  ],
  "digital-computer": [
    { type: "person", name: "Alan Turing", name_zh: "艾伦·图灵" },
    { type: "person", name: "John von Neumann", name_zh: "约翰·冯·诺依曼" },
    { type: "person", name: "Grace Hopper", name_zh: "葛丽丝·霍普" },
    { type: "unit", name: "ENIAC", name_zh: "埃尼阿克" },
    { type: "unit", name: "Colossus", name_zh: "巨人计算机", wiki: "Colossus computer" },
  ],
  "programming-language": [
    { type: "person", name: "John Backus", name_zh: "约翰·巴科斯" },
    { type: "person", name: "John McCarthy", name_zh: "约翰·麦卡锡" },
    { type: "person", name: "Dennis Ritchie", name_zh: "丹尼斯·里奇" },
    { type: "work", name: "Fortran", name_zh: "Fortran 语言" },
    { type: "work", name: "Lisp", name_zh: "Lisp 语言", wiki: "Lisp (programming language)" },
    { type: "work", name: "C", name_zh: "C 语言", wiki: "C (programming language)" },
  ],
  "mainframe": [
    { type: "unit", name: "IBM System/360", name_zh: "IBM System/360" },
    { type: "org", name: "IBM", name_zh: "国际商业机器公司" },
  ],
  "information-theory": [
    { type: "person", name: "Claude Shannon", name_zh: "克劳德·香农", wiki: "Claude Shannon" },
    { type: "work", name: "A Mathematical Theory of Communication", name_zh: "《通信的数学理论》", wiki: "A Mathematical Theory of Communication" },
    { type: "resource", name: "Bit", name_zh: "比特", wiki: "Bit" },
    { type: "work", name: "Shannon entropy", name_zh: "香农熵", wiki: "Entropy (information theory)" },
    { type: "work", name: "Shannon–Hartley theorem", name_zh: "香农-哈特利定理", wiki: "Shannon–Hartley theorem" },
    { type: "person", name: "Norbert Wiener", name_zh: "诺伯特·维纳", wiki: "Norbert Wiener" },
  ],
  "operating-system": [
    { type: "person", name: "Ken Thompson", name_zh: "肯·汤普森", wiki: "Ken Thompson" },
    { type: "person", name: "Dennis Ritchie", name_zh: "丹尼斯·里奇", wiki: "Dennis Ritchie" },
    { type: "person", name: "Linus Torvalds", name_zh: "林纳斯·托瓦兹", wiki: "Linus Torvalds" },
    { type: "unit", name: "UNIX", name_zh: "UNIX 操作系统", wiki: "Unix" },
    { type: "unit", name: "Linux", name_zh: "Linux 操作系统", wiki: "Linux" },
    { type: "unit", name: "Microsoft Windows", name_zh: "微软 Windows", wiki: "Microsoft Windows" },
    { type: "unit", name: "macOS", name_zh: "macOS", wiki: "MacOS" },
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
  "insulin-therapy": [
    { type: "person", name: "Frederick Banting", name_zh: "弗雷德里克·班廷" },
    { type: "person", name: "Charles Best", name_zh: "查尔斯·贝斯特", wiki: "Charles Best (medical scientist)" },
    { type: "person", name: "J.J.R. Macleod", name_zh: "约翰·麦克劳德" },
    { type: "person", name: "James Collip", name_zh: "詹姆斯·科利普" },
    { type: "resource", name: "Insulin", name_zh: "胰岛素" },
    { type: "org", name: "Connaught Laboratories", name_zh: "康诺特实验室" },
  ],
  "continental-drift": [
    { type: "person", name: "Alfred Wegener", name_zh: "阿尔弗雷德·魏格纳" },
    { type: "person", name: "Harry Hess", name_zh: "哈里·赫斯", wiki: "Harry Hammond Hess" },
    { type: "work", name: "The Origin of Continents and Oceans", name_zh: "《大陆与海洋的起源》" },
    { type: "unit", name: "Pangaea", name_zh: "盘古大陆" },
  ],
  "radio-broadcasting": [
    { type: "org", name: "KDKA Pittsburgh", name_zh: "匹兹堡KDKA电台", wiki: "KDKA (AM)" },
    { type: "org", name: "BBC", name_zh: "英国广播公司" },
    { type: "person", name: "Edward R. Murrow", name_zh: "爱德华·R·默罗" },
    { type: "person", name: "Franklin D. Roosevelt", name_zh: "富兰克林·罗斯福" },
    { type: "work", name: "Fireside Chats", name_zh: "炉边谈话" },
  ],
  "sound-film": [
    { type: "work", name: "The Jazz Singer", name_zh: "《爵士歌手》" },
    { type: "org", name: "Warner Bros.", name_zh: "华纳兄弟" },
    { type: "resource", name: "Vitaphone", name_zh: "维他风" },
    { type: "person", name: "Al Jolson", name_zh: "艾尔·乔森" },
  ],
  "big-bang-cosmology": [
    { type: "person", name: "Edwin Hubble", name_zh: "埃德温·哈勃" },
    { type: "person", name: "Georges Lemaître", name_zh: "乔治·勒梅特" },
    { type: "person", name: "Arno Penzias", name_zh: "阿诺·彭齐亚斯" },
    { type: "person", name: "Robert Wilson", name_zh: "罗伯特·威尔逊", wiki: "Robert Woodrow Wilson" },
    { type: "resource", name: "Hubble's Law", name_zh: "哈勃定律" },
    { type: "resource", name: "Cosmic Microwave Background", name_zh: "宇宙微波背景辐射" },
  ],
  "federal-reserve": [
    { type: "org", name: "U.S. Federal Reserve", name_zh: "美国联邦储备系统" },
    { type: "org", name: "European Central Bank", name_zh: "欧洲中央银行" },
    { type: "org", name: "Bank of Japan", name_zh: "日本银行" },
    { type: "person", name: "Paul Warburg", name_zh: "保罗·沃伯格" },
    { type: "work", name: "Federal Reserve Act", name_zh: "《联邦储备法》" },
  ],
  "russian-revolution": [
    { type: "person", name: "Vladimir Lenin", name_zh: "弗拉基米尔·列宁" },
    { type: "person", name: "Leon Trotsky", name_zh: "列夫·托洛茨基" },
    { type: "person", name: "Joseph Stalin", name_zh: "约瑟夫·斯大林" },
    { type: "org", name: "Bolshevik Party", name_zh: "布尔什维克党", wiki: "Bolsheviks" },
    { type: "unit", name: "Soviet Union", name_zh: "苏联" },
    { type: "work", name: "State and Revolution", name_zh: "《国家与革命》" },
  ],
  "fascism": [
    { type: "person", name: "Benito Mussolini", name_zh: "贝尼托·墨索里尼" },
    { type: "person", name: "Adolf Hitler", name_zh: "阿道夫·希特勒" },
    { type: "org", name: "National Fascist Party", name_zh: "国家法西斯党" },
    { type: "org", name: "NSDAP", name_zh: "纳粹党" },
    { type: "work", name: "The Doctrine of Fascism", name_zh: "《法西斯主义学说》" },
  ],
  "womens-suffrage": [
    { type: "person", name: "Emmeline Pankhurst", name_zh: "艾米琳·潘克赫斯特" },
    { type: "person", name: "Susan B. Anthony", name_zh: "苏珊·B·安东尼" },
    { type: "person", name: "Elizabeth Cady Stanton", name_zh: "伊丽莎白·卡迪·斯坦顿" },
    { type: "work", name: "19th Amendment", name_zh: "美国宪法第十九修正案", wiki: "Nineteenth Amendment to the United States Constitution" },
    { type: "org", name: "WSPU", name_zh: "妇女社会与政治联盟" },
    { type: "org", name: "NAWSA", name_zh: "全美妇女选举权协会" },
  ],
  "keynesian-economics": [
    { type: "person", name: "John Maynard Keynes", name_zh: "约翰·梅纳德·凯恩斯" },
    { type: "person", name: "Joan Robinson", name_zh: "琼·罗宾逊" },
    { type: "work", name: "The General Theory of Employment, Interest and Money", name_zh: "《就业、利息和货币通论》" },
    { type: "work", name: "Bretton Woods Agreement", name_zh: "《布雷顿森林协议》" },
    { type: "resource", name: "Fiscal Policy", name_zh: "财政政策" },
  ],
  "cryptanalysis-bombe": [
    { type: "person", name: "Alan Turing", name_zh: "艾伦·图灵" },
    { type: "person", name: "Marian Rejewski", name_zh: "马里安·雷耶夫斯基" },
    { type: "person", name: "Tommy Flowers", name_zh: "汤米·弗劳尔斯" },
    { type: "unit", name: "Bombe", name_zh: "炸弹机" },
    { type: "unit", name: "Colossus", name_zh: "巨人计算机", wiki: "Colossus computer" },
    { type: "wonder", name: "Bletchley Park", name_zh: "布莱切利庄园" },
  ],
  "strategic-bombing": [
    { type: "person", name: "Giulio Douhet", name_zh: "朱利奥·杜黑" },
    { type: "person", name: "Arthur Harris", name_zh: "亚瑟·哈里斯" },
    { type: "person", name: "Curtis LeMay", name_zh: "柯蒂斯·李梅" },
    { type: "unit", name: "B-29 Superfortress", name_zh: "B-29超级堡垒轰炸机" },
    { type: "unit", name: "Avro Lancaster", name_zh: "阿芙罗兰开斯特轰炸机" },
    { type: "work", name: "The Command of the Air", name_zh: "《制空权》" },
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
    { type: "unit", name: "EUV scanner (ASML NXE/EXE)", name_zh: "极紫外光刻机(ASML NXE/EXE)" , wiki: "Extreme ultraviolet lithography" },
    { type: "unit", name: "FinFET transistor", name_zh: "鳍式场效应晶体管(FinFET)" },
    { type: "unit", name: "Apple M-series chip", name_zh: "苹果M系列芯片" , wiki: "Apple silicon" },
    { type: "unit", name: "NVIDIA H100 / Blackwell GPU", name_zh: "英伟达 H100 / Blackwell GPU" , wiki: "Hopper (microarchitecture)" },
  ],
  "parallel-compute-gpu": [
    { type: "unit", name: "NVIDIA CUDA platform", name_zh: "英伟达 CUDA 平台", wiki: "CUDA" },
    { type: "unit", name: "Google TPU", name_zh: "谷歌 TPU", wiki: "Tensor Processing Unit" },
    { type: "unit", name: "AMD ROCm", name_zh: "AMD ROCm", wiki: "ROCm" },
    { type: "unit", name: "Cerebras wafer-scale engine", name_zh: "Cerebras 晶圆级处理器", wiki: "Cerebras" },
    { type: "person", name: "Ian Buck (CUDA)", name_zh: "伊恩·巴克(CUDA)", wiki: "CUDA" },
    { type: "org", name: "NVIDIA", name_zh: "英伟达", wiki: "Nvidia" },
  ],
  "personal-computer": [
    { type: "unit", name: "Apple II", name_zh: "Apple II" },
    { type: "unit", name: "IBM PC", name_zh: "IBM PC" },
    { type: "unit", name: "Commodore 64", name_zh: "康懋达64" },
    { type: "person", name: "Steve Wozniak", name_zh: "史蒂夫·沃兹尼亚克" },
    { type: "person", name: "Steve Jobs", name_zh: "史蒂夫·乔布斯" },
    { type: "org", name: "Apple", name_zh: "苹果公司" , wiki: "Apple Inc." },
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
    { type: "org", name: "ARPA / DARPA", name_zh: "美国国防高等研究计划署" , wiki: "DARPA" },
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
    { type: "unit", name: "Android", name_zh: "安卓" , wiki: "Android (operating system)" },
    { type: "person", name: "Steve Jobs", name_zh: "史蒂夫·乔布斯" },
    { type: "org", name: "Apple", name_zh: "苹果公司" , wiki: "Apple Inc." },
    { type: "org", name: "Google", name_zh: "谷歌" },
  ],
  "social-media": [
    { type: "org", name: "Facebook (Meta)", name_zh: "Facebook(Meta)" , wiki: "Meta Platforms" },
    { type: "org", name: "Twitter (X)", name_zh: "Twitter(X)" , wiki: "X (social network)" },
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
    { type: "org", name: "Amazon Web Services (AWS)", name_zh: "亚马逊云服务(AWS)" , wiki: "Amazon Web Services" },
    { type: "org", name: "Microsoft Azure", name_zh: "微软Azure" },
    { type: "org", name: "Google Cloud", name_zh: "谷歌云" },
  ],
  "ecommerce": [
    { type: "org", name: "Amazon", name_zh: "亚马逊" , wiki: "Amazon (company)" },
    { type: "org", name: "eBay", name_zh: "eBay" },
    { type: "org", name: "Alibaba", name_zh: "阿里巴巴" , wiki: "Alibaba Group" },
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
    { type: "person", name: "Stanley N. Cohen", name_zh: "斯坦利·科恩" , wiki: "Stanley Norman Cohen" },
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
    { type: "unit", name: "Photovoltaic cell", name_zh: "光伏电池" , wiki: "Solar cell" },
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
    { type: "unit", name: "Tesla Roadster", name_zh: "特斯拉Roadster跑车" , wiki: "Tesla Roadster (first generation)" },
    { type: "unit", name: "Tesla Model S", name_zh: "特斯拉Model S" },
    { type: "person", name: "Elon Musk", name_zh: "埃隆·马斯克" },
    { type: "org", name: "Tesla, Inc.", name_zh: "特斯拉公司" , wiki: "Tesla, Inc." },
    { type: "org", name: "BYD", name_zh: "比亚迪" , wiki: "BYD Auto" },
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
    { type: "unit", name: "Claude", name_zh: "Claude" , wiki: "Claude (language model)" },
    { type: "work", name: "Attention Is All You Need", name_zh: "《Attention Is All You Need》" },
  ],
  "cryptocurrency": [
    { type: "resource", name: "Bitcoin", name_zh: "比特币" },
    { type: "resource", name: "Ether", name_zh: "以太币" , wiki: "Ethereum" },
    { type: "person", name: "Satoshi Nakamoto", name_zh: "中本聪" },
  ],
  "reusable-rocket": [
    { type: "org", name: "SpaceX", name_zh: "SpaceX" },
    { type: "unit", name: "Falcon 9", name_zh: "猎鹰9号" },
    { type: "unit", name: "Starship", name_zh: "星舰" , wiki: "SpaceX Starship" },
    { type: "person", name: "Elon Musk", name_zh: "埃隆·马斯克" },
  ],
  "autonomous-vehicle": [
    { type: "org", name: "Waymo", name_zh: "Waymo" },
    { type: "org", name: "Cruise", name_zh: "Cruise" , wiki: "Cruise (autonomous vehicle)" },
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
    { type: "unit", name: "Sycamore (Google)", name_zh: "悬铃木量子处理器" , wiki: "Sycamore (processor)" },
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
    { type: "unit", name: "HMS Hermes", name_zh: "赫尔墨斯号航空母舰" , wiki: "HMS Hermes (95)" },
    { type: "wonder", name: "Battle of Midway", name_zh: "中途岛海战" },
  ],
  "submarine-warfare": [
    { type: "unit", name: "Type VII U-boat", name_zh: "VII型潜艇" },
    { type: "unit", name: "Type XXI U-boat", name_zh: "XXI型潜艇" },
    { type: "person", name: "Karl Dönitz", name_zh: "卡尔·邓尼茨" },
    { type: "unit", name: "Wolfpack tactics", name_zh: "狼群战术" , wiki: "Wolfpack (naval tactic)" },
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
    { type: "unit", name: "Atlas missile", name_zh: "宇宙神导弹" , wiki: "SM-65 Atlas" },
    { type: "unit", name: "Minuteman III", name_zh: "民兵III型导弹" },
    { type: "unit", name: "Polaris (submarine-launched)", name_zh: "北极星导弹" , wiki: "UGM-27 Polaris" },
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
    { type: "person", name: "Ben Rich (Skunk Works)", name_zh: "本·里奇(臭鼬工厂)" , wiki: "Ben Rich (engineer)" },
    { type: "org", name: "Lockheed Skunk Works", name_zh: "洛克希德臭鼬工厂" },
  ],
  "drone-uav": [
    { type: "unit", name: "MQ-1 Predator", name_zh: "MQ-1捕食者无人机" },
    { type: "unit", name: "MQ-9 Reaper", name_zh: "MQ-9死神无人机" },
    { type: "unit", name: "RQ-4 Global Hawk", name_zh: "RQ-4全球鹰无人机" },
    { type: "unit", name: "Bayraktar TB2", name_zh: "拜拉克塔尔TB2无人机" , wiki: "Bayraktar TB2" },
    { type: "org", name: "General Atomics", name_zh: "通用原子能公司" },
  ],
  "fifth-gen-fighter": [
    { type: "unit", name: "F-22 Raptor", name_zh: "F-22猛禽战斗机" },
    { type: "unit", name: "F-35 Lightning II", name_zh: "F-35闪电II战斗机" },
    { type: "unit", name: "Sukhoi Su-57", name_zh: "苏-57战斗机" },
  ],
  "cyber-warfare": [
    { type: "unit", name: "Stuxnet", name_zh: "震网病毒" , wiki: "Stuxnet" },
    { type: "unit", name: "NotPetya", name_zh: "NotPetya勒索软件" , wiki: "Petya and NotPetya" },
    { type: "org", name: "NSA TAO", name_zh: "美国国安局特定入侵行动办公室" },
    { type: "org", name: "Unit 8200", name_zh: "以色列8200部队" },
  ],
  "hypersonic-weapon": [
    { type: "unit", name: "Avangard", name_zh: "先锋高超音速导弹" , wiki: "Avangard (hypersonic glide vehicle)" },
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
    { type: "person", name: "Alan Hodgkin & Andrew Huxley", name_zh: "霍奇金与赫胥黎" , wiki: "Alan Hodgkin" },
    { type: "person", name: "Wilder Penfield", name_zh: "怀尔德·彭菲尔德" },
    { type: "person", name: "Eric Kandel", name_zh: "埃里克·坎德尔" },
    { type: "work", name: "Hodgkin–Huxley model", name_zh: "霍奇金-赫胥黎方程" , wiki: "Hodgkin–Huxley model" },
  ],
  "gene-therapy": [
    { type: "person", name: "French Anderson", name_zh: "威廉·法兰奇·安德森" },
    { type: "unit", name: "Luxturna", name_zh: "Luxturna基因疗法" },
    { type: "unit", name: "Zolgensma", name_zh: "Zolgensma基因疗法" },
    { type: "unit", name: "Casgevy (CRISPR)", name_zh: "Casgevy(CRISPR疗法)" , wiki: "Exagamglogene autotemcel" },
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
    { type: "unit", name: "BIOS-3 (Soviet)", name_zh: "BIOS-3(苏联生命维持系统)" , wiki: "BIOS-3" },
  ],
  "fusion-power": [
    { type: "org", name: "ITER", name_zh: "国际热核聚变实验堆" },
    { type: "org", name: "Commonwealth Fusion Systems", name_zh: "联邦聚变系统公司" },
    { type: "unit", name: "SPARC tokamak", name_zh: "SPARC托卡马克" },
    { type: "unit", name: "Joint European Torus (JET)", name_zh: "欧洲联合环面装置(JET)" },
    { type: "wonder", name: "National Ignition Facility", name_zh: "国家点火装置" },
  ],
  "humanoid-robot": [
    { type: "unit", name: "Atlas (Boston Dynamics)", name_zh: "阿特拉斯机器人(波士顿动力)" , wiki: "Atlas (robot)" },
    { type: "unit", name: "Tesla Optimus", name_zh: "特斯拉Optimus" , wiki: "Optimus (robot)" },
    { type: "unit", name: "Figure 02", name_zh: "Figure 02机器人" , wiki: "Figure AI" },
    { type: "unit", name: "Unitree H1", name_zh: "宇树H1机器人" , wiki: "Unitree Robotics" },
    { type: "org", name: "Boston Dynamics", name_zh: "波士顿动力" },
  ],
  "agi": [
    { type: "org", name: "OpenAI", name_zh: "OpenAI" },
    { type: "org", name: "Anthropic", name_zh: "Anthropic" },
    { type: "org", name: "Google DeepMind", name_zh: "谷歌DeepMind" },
    { type: "person", name: "Demis Hassabis", name_zh: "戴密斯·哈萨比斯" },
    { type: "person", name: "Stuart Russell", name_zh: "斯图尔特·罗素" , wiki: "Stuart J. Russell" },
    { type: "person", name: "Nick Bostrom", name_zh: "尼克·博斯特罗姆" },
  ],
  "brain-computer-interface": [
    { type: "org", name: "Neuralink", name_zh: "Neuralink" },
    { type: "org", name: "Synchron", name_zh: "Synchron" },
    { type: "unit", name: "Utah array", name_zh: "犹他电极阵列" },
    { type: "unit", name: "N1 Implant (Neuralink)", name_zh: "N1脑机接口(Neuralink)" , wiki: "Neuralink" },
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
    { type: "unit", name: "Starship", name_zh: "星舰" , wiki: "SpaceX Starship" },
    { type: "person", name: "Elon Musk", name_zh: "埃隆·马斯克" },
    { type: "wonder", name: "Olympus Mons", name_zh: "奥林帕斯山" },
    { type: "plant", name: "Mars potato (The Martian)", name_zh: "火星马铃薯" , wiki: false },
  ],
  "asteroid-mining": [
    { type: "unit", name: "OSIRIS-REx mission", name_zh: "OSIRIS-REx任务" },
    { type: "unit", name: "Hayabusa2 mission", name_zh: "隼鸟2号任务" },
    { type: "wonder", name: "Asteroid 16 Psyche", name_zh: "16灵神星" },
    { type: "resource", name: "Platinum-group metals", name_zh: "铂族金属" },
    { type: "resource", name: "Asteroid water ice", name_zh: "小行星水冰" , wiki: "Asteroidal water" },
  ],
  "anti-aging": [
    { type: "org", name: "Altos Labs", name_zh: "Altos实验室" },
    { type: "org", name: "Calico (Alphabet)", name_zh: "Calico" , wiki: "Calico (company)" },
    { type: "person", name: "Aubrey de Grey", name_zh: "奥布里·德格雷" },
    { type: "person", name: "David Sinclair", name_zh: "大卫·辛克莱" },
    { type: "unit", name: "Yamanaka factors (OSKM)", name_zh: "山中因子(OSKM)" , wiki: "Induced pluripotent stem cell" },
  ],
  "lab-grown-meat": [
    { type: "org", name: "Eat Just (GOOD Meat)", name_zh: "Eat Just (GOOD Meat)" , wiki: "Eat Just" },
    { type: "org", name: "UPSIDE Foods", name_zh: "UPSIDE Foods" },
    { type: "person", name: "Mark Post", name_zh: "马克·波斯特" },
    { type: "unit", name: "Cultivated chicken", name_zh: "培育鸡肉" , wiki: "Cultured meat" },
  ],
  "synthetic-biology": [
    { type: "person", name: "Craig Venter", name_zh: "克雷格·文特尔" },
    { type: "unit", name: "Synthetic Mycoplasma (JCVI-syn3.0)", name_zh: "合成支原体" , wiki: "Mycoplasma laboratorium" },
    { type: "work", name: "AlphaFold", name_zh: "AlphaFold蛋白结构预测" },
    { type: "org", name: "Ginkgo Bioworks", name_zh: "Ginkgo Bioworks" },
    { type: "unit", name: "ESM3 protein model", name_zh: "ESM3蛋白质模型" , url: "https://www.evolutionaryscale.ai/blog/esm3-release" },
  ],
  "room-temp-superconductor": [
    { type: "resource", name: "Lanthanum decahydride (LaH10)", name_zh: "氢化镧(LaH10)" },
    { type: "resource", name: "YBCO superconductor", name_zh: "钇钡铜氧超导体" },
    { type: "person", name: "Karl Müller", name_zh: "卡尔·米勒" , wiki: "K. Alex Müller" },
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
  "quantum-internet": [
    { type: "work", name: "Quantum key distribution", name_zh: "量子密钥分发", wiki: "Quantum key distribution" },
    { type: "work", name: "Quantum entanglement", name_zh: "量子纠缠", wiki: "Quantum entanglement" },
    { type: "work", name: "Quantum teleportation", name_zh: "量子隐形传态", wiki: "Quantum teleportation" },
    { type: "unit", name: "Micius satellite", name_zh: "墨子号量子卫星", wiki: "Micius (satellite)" },
    { type: "unit", name: "Quantum repeater", name_zh: "量子中继器", wiki: "Quantum repeater" },
    { type: "person", name: "Stephanie Wehner", name_zh: "斯蒂芬妮·维纳", wiki: "Stephanie Wehner" },
    { type: "org", name: "Quantum Internet Alliance", name_zh: "量子互联网联盟", wiki: "Quantum Internet Alliance" },
  ],
  "carbon-capture-scale": [
    { type: "org", name: "Climeworks", name_zh: "Climeworks" },
    { type: "unit", name: "Orca DAC plant", name_zh: "Orca碳捕集工厂" , wiki: "Climeworks" },
    { type: "unit", name: "Mammoth DAC plant", name_zh: "Mammoth碳捕集工厂" , wiki: "Climeworks" },
    { type: "org", name: "Carbon Engineering", name_zh: "Carbon Engineering" },
  ],
  "fusion-rocket": [
    { type: "unit", name: "Direct Fusion Drive", name_zh: "直接聚变驱动" },
    { type: "unit", name: "Daedalus probe (study)", name_zh: "代达罗斯探测器(研究)" , wiki: "Project Daedalus" },
    { type: "unit", name: "PFRC reactor", name_zh: "PFRC聚变反应堆" , wiki: "Princeton field-reversed configuration" },
  ],
  "space-elevator": [
    { type: "person", name: "Konstantin Tsiolkovsky", name_zh: "康斯坦丁·齐奥尔科夫斯基" },
    { type: "person", name: "Yuri Artsutanov", name_zh: "尤里·阿尔楚塔诺夫" },
    { type: "person", name: "Bradley Edwards", name_zh: "布拉德利·爱德华兹" },
    { type: "resource", name: "Carbon nanotube cable", name_zh: "碳纳米管缆绳" , wiki: "Carbon nanotube" },
  ],
  "post-scarcity": [
    { type: "person", name: "Peter Diamandis", name_zh: "彼得·迪亚曼迪斯" },
    { type: "work", name: "Abundance (book)", name_zh: "《富足》" , wiki: "Abundance: The Future Is Better Than You Think" },
    { type: "work", name: "Universal Basic Income", name_zh: "全民基本收入(UBI)" , wiki: "Universal basic income" },
    { type: "person", name: "John Maynard Keynes (1930 essay)", name_zh: "凯恩斯(1930年论文)" , wiki: "John Maynard Keynes" },
  ],
  "digital-immortality": [
    { type: "person", name: "Hans Moravec", name_zh: "汉斯·莫拉维克" },
    { type: "person", name: "Ray Kurzweil", name_zh: "雷·库兹韦尔" },
    { type: "work", name: "The Singularity Is Near", name_zh: "《奇点临近》" },
    { type: "unit", name: "Whole-brain emulation", name_zh: "全脑仿真" , wiki: "Mind uploading" },
  ],

  // ─── Future Age (social) ───
  "universal-basic-income": [
    { type: "person", name: "Andrew Yang", name_zh: "杨安泽" },
    { type: "person", name: "Milton Friedman (negative income tax)", name_zh: "米尔顿·弗里德曼" , wiki: "Milton Friedman" },
    { type: "org", name: "GiveDirectly", name_zh: "GiveDirectly" },
    { type: "unit", name: "Alaska Permanent Fund", name_zh: "阿拉斯加永久基金" },
    { type: "work", name: "Universal Basic Income (book, Van Parijs)", name_zh: "《全民基本收入》(范帕里斯)" , wiki: "Philippe Van Parijs" },
  ],
  "liquid-democracy": [
    { type: "person", name: "Audrey Tang (Taiwan Digital Minister)", name_zh: "唐凤(台湾数字部长)" , wiki: "Audrey Tang" },
    { type: "unit", name: "vTaiwan platform", name_zh: "vTaiwan平台" },
    { type: "org", name: "e-Estonia", name_zh: "电子爱沙尼亚" },
    { type: "org", name: "Pirate Party", name_zh: "海盗党" },
    { type: "work", name: "Liquid Feedback (software)", name_zh: "Liquid Feedback软件" , wiki: "LiquidFeedback" },
  ],
  "network-state": [
    { type: "person", name: "Balaji Srinivasan", name_zh: "巴拉吉·斯里尼瓦桑" },
    { type: "work", name: "The Network State (book)", name_zh: "《网络国家》" , wiki: "Balaji Srinivasan" },
    { type: "unit", name: "Próspera (Honduras ZEDE)", name_zh: "普罗斯佩拉(洪都拉斯特区)" , wiki: "Próspera" },
    { type: "unit", name: "Zuzalu (pop-up city)", name_zh: "Zuzalu(实验性城邦)" , wiki: false },
  ],
  "ai-governance": [
    { type: "unit", name: "Estonia AI judge (pilot)", name_zh: "爱沙尼亚AI法官(试点)" , url: "https://futurism.com/the-byte/estonia-robot-judge" },
    { type: "work", name: "EU AI Act", name_zh: "欧盟人工智能法案" },
    { type: "org", name: "Singapore Smart Nation", name_zh: "新加坡智慧国家" , wiki: "Smart Nation" },
    { type: "work", name: "Algorithmic Regulation (Tim O'Reilly)", name_zh: "《算法监管》(奥莱利)" , wiki: "Government by algorithm" },
  ],
  "transhumanism": [
    { type: "person", name: "Nick Bostrom", name_zh: "尼克·博斯特罗姆" },
    { type: "person", name: "Ray Kurzweil", name_zh: "雷·库兹韦尔" },
    { type: "person", name: "Max More", name_zh: "马克斯·摩尔" },
    { type: "person", name: "FM-2030", name_zh: "FM-2030" },
    { type: "org", name: "Humanity+ (WTA)", name_zh: "人类+协会" , wiki: "Humanity+" },
  ],
  "longtermism": [
    { type: "person", name: "Derek Parfit", name_zh: "德里克·帕菲特" },
    { type: "person", name: "Toby Ord", name_zh: "托比·奥德" },
    { type: "person", name: "William MacAskill", name_zh: "威廉·麦卡斯基尔" },
    { type: "work", name: "The Precipice (Ord, 2020)", name_zh: "《悬崖》(奥德,2020)" , wiki: "The Precipice: Existential Risk and the Future of Humanity" },
    { type: "work", name: "What We Owe the Future", name_zh: "《我们欠未来的》" },
    { type: "org", name: "80,000 Hours", name_zh: "80,000 Hours" },
  ],
  "generative-art": [
    { type: "org", name: "Midjourney", name_zh: "Midjourney" },
    { type: "unit", name: "Stable Diffusion", name_zh: "Stable Diffusion" },
    { type: "unit", name: "DALL-E", name_zh: "DALL·E" },
    { type: "unit", name: "Sora (OpenAI)", name_zh: "Sora(OpenAI)" , wiki: "Sora (text-to-video model)" },
    { type: "person", name: "Refik Anadol", name_zh: "雷菲克·阿纳多尔" },
    { type: "person", name: "Holly Herndon", name_zh: "霍莉·赫顿" },
  ],
  "metaverse": [
    { type: "work", name: "Snow Crash (Neal Stephenson)", name_zh: "《雪崩》(尼尔·斯蒂芬森)" , wiki: "Snow Crash" },
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
    { type: "work", name: "Hyperloop white paper (Musk 2013)", name_zh: "超回路列车白皮书" , wiki: "Hyperloop" },
    { type: "org", name: "Virgin Hyperloop", name_zh: "维珍超回路" },
    { type: "org", name: "HyperloopTT", name_zh: "HyperloopTT" },
    { type: "org", name: "Boring Company", name_zh: "Boring公司" , wiki: "The Boring Company" },
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
    { type: "unit", name: "Lab-grown bladder (2006)", name_zh: "实验室培育膀胱" , wiki: "Artificial urinary bladder" },
    { type: "org", name: "United Therapeutics", name_zh: "United Therapeutics" },
    { type: "unit", name: "Organoid", name_zh: "类器官" },
  ],
  "sentientism": [
    { type: "person", name: "Peter Singer", name_zh: "彼得·辛格" },
    { type: "work", name: "Animal Liberation (1975)", name_zh: "《动物解放》" , wiki: "Animal Liberation (book)" },
    { type: "person", name: "Jeff Sebo", name_zh: "杰夫·塞博" },
    { type: "person", name: "Donald Watson", name_zh: "唐纳德·沃森" },
    { type: "org", name: "Open Philanthropy (animal welfare)", name_zh: "Open Philanthropy(动物福利)" , wiki: "Open Philanthropy" },
  ],
  "dna-data-storage": [
    { type: "org", name: "Microsoft Research", name_zh: "微软研究院" },
    { type: "org", name: "Catalog Technologies", name_zh: "Catalog Technologies" , wiki: false },
    { type: "org", name: "Twist Bioscience", name_zh: "Twist Bioscience" },
    { type: "person", name: "George Church", name_zh: "乔治·丘奇" },
  ],
  "cancer-cure": [
    { type: "unit", name: "CAR-T cell therapy", name_zh: "CAR-T细胞疗法" },
    { type: "unit", name: "Keytruda (pembrolizumab)", name_zh: "Keytruda(派姆单抗)" , wiki: "Pembrolizumab" },
    { type: "unit", name: "Personalized mRNA cancer vaccine", name_zh: "个性化mRNA癌症疫苗" },
    { type: "person", name: "James Allison", name_zh: "詹姆斯·艾利森" },
  ],
  "ai-judge": [
    { type: "unit", name: "COMPAS recidivism algorithm", name_zh: "COMPAS再犯预测算法" },
    { type: "unit", name: "Estonia AI judge (pilot)", name_zh: "爱沙尼亚AI法官(试点)" , url: "https://futurism.com/the-byte/estonia-robot-judge" },
    { type: "work", name: "Weapons of Math Destruction", name_zh: "《数学杀伤性武器》" },
    { type: "person", name: "Cathy O'Neil", name_zh: "凯西·奥尼尔" },
  ],
  "space-based-solar": [
    { type: "org", name: "Caltech Space Solar Power Project", name_zh: "加州理工太空太阳能项目" , wiki: "Space-based solar power" },
    { type: "work", name: "SOLARIS (ESA)", name_zh: "SOLARIS(欧空局)" , wiki: "Solaris (solar power)" },
    { type: "person", name: "Peter Glaser (concept, 1968)", name_zh: "彼得·格拉泽" , wiki: "Peter Glaser" },
    { type: "unit", name: "Microwave power transmission", name_zh: "微波输电" , wiki: "Wireless power transfer" },
  ],
  "photonic-computing": [
    { type: "org", name: "Lightmatter", name_zh: "Lightmatter" , wiki: false },
    { type: "org", name: "Lightelligence", name_zh: "Lightelligence" },
    { type: "unit", name: "Photonic tensor core", name_zh: "光子张量核" , wiki: "Optical computing" },
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
    { type: "unit", name: "LIGO (advanced)", name_zh: "高级LIGO", wiki: "LIGO" },
    { type: "unit", name: "LISA (ESA-NASA)", name_zh: "LISA(欧空局-NASA)", wiki: "Laser Interferometer Space Antenna" },
    { type: "unit", name: "Einstein Telescope", name_zh: "爱因斯坦望远镜" },
    { type: "unit", name: "NANOGrav (pulsar timing)", name_zh: "NANOGrav脉冲星计时阵列", wiki: "North American Nanohertz Observatory for Gravitational Waves" },
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
    { type: "work", name: "The High Frontier (book)", name_zh: "《高边疆》", wiki: "The High Frontier: Human Colonies in Space" },
  ],
  "artificial-photosynthesis": [
    { type: "person", name: "Daniel Nocera", name_zh: "丹尼尔·诺切拉" },
    { type: "unit", name: "Artificial leaf", name_zh: "人工叶" },
    { type: "unit", name: "Bionic Leaf 2.0", name_zh: "仿生叶 2.0", wiki: "Bionic leaf" },
    { type: "org", name: "Twelve (company)", name_zh: "Twelve公司" },
    { type: "org", name: "Synhelion", name_zh: "Synhelion" },
    { type: "org", name: "Air Company", name_zh: "Air Company" },
  ],
  "genetic-disease-eradication": [
    { type: "unit", name: "Casgevy (CRISPR therapy)", name_zh: "Casgevy(CRISPR疗法)", wiki: "Exagamglogene autotemcel" },
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
    { type: "work", name: "NASA 1980 study (Lunar self-replicating factory)", name_zh: "NASA 1980年自复制工厂研究", wiki: "Self-replicating machine" },
  ],
  "superintelligence": [
    { type: "person", name: "I.J. Good", name_zh: "I·J·古德" },
    { type: "person", name: "Nick Bostrom", name_zh: "尼克·博斯特罗姆" },
    { type: "person", name: "Stuart Russell", name_zh: "斯图尔特·罗素", wiki: "Stuart J. Russell" },
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
    { type: "unit", name: "Statite (solar sail)", name_zh: "光力悬浮卫星", wiki: "Statite" },
    { type: "work", name: "Kardashev scale", name_zh: "卡尔达肖夫等级" },
    { type: "person", name: "Robert Bradbury", name_zh: "罗伯特·布拉德伯里", wiki: "Robert J. Bradbury" },
    { type: "work", name: "Search for Dyson sphere candidates (Tabby's star)", name_zh: "戴森球候选搜索(塔比之星)", wiki: "Tabby's Star" },
  ],
  "matrioshka-brain": [
    { type: "person", name: "Robert Bradbury", name_zh: "罗伯特·布拉德伯里", wiki: "Robert J. Bradbury" },
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
    { type: "work", name: "Project Hyperion", name_zh: "海泊龙计划", wiki: "Project Hyperion (interstellar)" },
    { type: "work", name: "100 Year Starship initiative", name_zh: "百年星舰计划", wiki: "100 Year Starship" },
    { type: "unit", name: "Rama-class habitat (Clarke)", name_zh: "罗摩级栖息地(克拉克)" , wiki: "Rendezvous with Rama" },
    { type: "wonder", name: "Proxima Centauri b", name_zh: "比邻星b" },
  ],
  "galactic-civilization": [
    { type: "work", name: "Kardashev Type III", name_zh: "卡尔达肖夫III型" },
    { type: "work", name: "Drake equation", name_zh: "德雷克方程" },
    { type: "work", name: "Fermi paradox", name_zh: "费米悖论" },
    { type: "work", name: "Great Filter", name_zh: "大过滤器" },
    { type: "person", name: "Carl Sagan (Cosmos)", name_zh: "卡尔·萨根(宇宙)" , wiki: "Carl Sagan" },
  ],
  "speciation": [
    { type: "person", name: "Stephen Hawking", name_zh: "史蒂芬·霍金" },
    { type: "person", name: "Cixin Liu", name_zh: "刘慈欣" },
    { type: "person", name: "Greg Egan", name_zh: "格雷格·伊根" },
    { type: "work", name: "The Diamond Age (Stephenson)", name_zh: "《钻石时代》" },
    { type: "work", name: "Cordwainer Smith's Underpeople", name_zh: "考德怀纳·史密斯笔下的下层人" , wiki: "Cordwainer Smith" },
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
    { type: "resource", name: "Negative-energy density (exotic matter)", name_zh: "负能量密度(奇异物质)", wiki: "Exotic matter" },
  ],
  "kardashev-type-ii": [
    { type: "person", name: "Nikolai Kardashev", name_zh: "尼古拉·卡尔达肖夫" },
    { type: "work", name: "Kardashev Type I (planetary)", name_zh: "卡尔达肖夫I型(行星级)" },
    { type: "work", name: "Kardashev Type II (stellar)", name_zh: "卡尔达肖夫II型(恒星级)" },
    { type: "person", name: "Carl Sagan (extension)", name_zh: "卡尔·萨根(扩展)" , wiki: "Carl Sagan" },
  ],

  // ─── Far Future (civilizational) ───
  "existential-risk-hedge": [
    { type: "person", name: "Toby Ord", name_zh: "托比·奥德" },
    { type: "work", name: "The Precipice", name_zh: "《悬崖》", wiki: "The Precipice: Existential Risk and the Future of Humanity" },
    { type: "person", name: "Nick Bostrom", name_zh: "尼克·博斯特罗姆" },
    { type: "org", name: "Future of Humanity Institute", name_zh: "人类未来研究所" },
    { type: "org", name: "80,000 Hours", name_zh: "80,000 Hours" },
  ],
  "universal-sentient-rights": [
    { type: "work", name: "Universal Declaration of Human Rights (1948)", name_zh: "《世界人权宣言》" },
    { type: "person", name: "Peter Singer", name_zh: "彼得·辛格" },
    { type: "work", name: "Animal Rights movement", name_zh: "动物权利运动" },
    { type: "work", name: "Integrated Information Theory (IIT)", name_zh: "整合信息论" },
    { type: "person", name: "Eleanor Roosevelt (UDHR drafter)", name_zh: "埃莉诺·罗斯福", wiki: "Eleanor Roosevelt" },
  ],
  "pleistocene-restored": [
    { type: "org", name: "Colossal Biosciences", name_zh: "Colossal Biosciences" },
    { type: "wonder", name: "Pleistocene Park (Yakutia)", name_zh: "更新世公园(雅库特)" },
    { type: "person", name: "Sergey Zimov", name_zh: "谢尔盖·齐莫夫" },
    { type: "animal", name: "Woolly mammoth (revived)", name_zh: "猛犸象(复活)" },
    { type: "animal", name: "Thylacine (revived)", name_zh: "袋狼(复活)" },
    { type: "animal", name: "Dodo (revived)", name_zh: "渡渡鸟(复活)" },
  ],
  "lingua-galactica": [
    { type: "person", name: "L. L. Zamenhof", name_zh: "拉扎鲁·拉扎洛维奇·扎门霍夫" },
    { type: "work", name: "Esperanto", name_zh: "世界语" },
    { type: "work", name: "Lojban", name_zh: "逻辑语" },
    { type: "work", name: "Loglan", name_zh: "逻辑语前身" },
    { type: "org", name: "Universal Esperanto Association", name_zh: "国际世界语协会" },
  ],
  "post-human-aesthetics": [
    { type: "person", name: "Greg Egan", name_zh: "格雷格·伊根" },
    { type: "work", name: "Permutation City", name_zh: "《置换城市》" },
    { type: "work", name: "Diaspora (Egan novel)", name_zh: "《海移》(伊根)" },
    { type: "person", name: "Ted Chiang", name_zh: "特德·姜" },
    { type: "person", name: "Olaf Stapledon", name_zh: "奥拉夫·斯特普尔顿" },
    { type: "work", name: "Last and First Men", name_zh: "《最后和最初的人》" },
  ],
  "engineered-planetary-biosphere": [
    { type: "work", name: "Gene drive", name_zh: "基因驱动" },
    { type: "work", name: "Stratospheric aerosol injection", name_zh: "平流层气溶胶注入" },
    { type: "work", name: "Anthropocene (term)", name_zh: "人类世" },
    { type: "person", name: "Paul Crutzen (Anthropocene)", name_zh: "保罗·克鲁岑", wiki: "Paul J. Crutzen" },
    { type: "org", name: "IPCC Geoengineering reports", name_zh: "IPCC地球工程报告", wiki: "Geoengineering" },
  ],
  "interstellar-treaty": [
    { type: "work", name: "Outer Space Treaty (1967)", name_zh: "《外层空间条约》" },
    { type: "work", name: "Antarctic Treaty (1959)", name_zh: "《南极条约》" },
    { type: "work", name: "Moon Treaty (1979)", name_zh: "《月球协定》" },
    { type: "org", name: "United Nations Office for Outer Space Affairs", name_zh: "联合国外空事务办公室" },
  ],
  "time-dilation-cultures": [
    { type: "person", name: "Robin Hanson", name_zh: "罗宾·汉森" },
    { type: "work", name: "The Age of Em", name_zh: "《模拟人类时代》" },
    { type: "person", name: "Greg Egan", name_zh: "格雷格·伊根" },
    { type: "work", name: "Diaspora (Egan)", name_zh: "《海移》(伊根)" },
    { type: "work", name: "Subjective time-dilation", name_zh: "主观时间膨胀" },
  ],
  "end-time-philosophy": [
    { type: "work", name: "Heat death of the universe", name_zh: "宇宙热寂" },
    { type: "work", name: "The Last Question (Asimov, 1956)", name_zh: "《最后的问题》(阿西莫夫)" },
    { type: "work", name: "Last and First Men (Stapledon)", name_zh: "《最后和最初的人》" },
    { type: "person", name: "Lee Smolin", name_zh: "李·斯莫林" },
    { type: "work", name: "Cosmological natural selection", name_zh: "宇宙学自然选择" },
  ],
  "galactic-ecology": [
    { type: "work", name: "Directed panspermia", name_zh: "定向胚种论" },
    { type: "person", name: "Carl Sagan (panspermia)", name_zh: "卡尔·萨根(胚种论)" , wiki: "Carl Sagan" },
    { type: "person", name: "Francis Crick (panspermia)", name_zh: "弗朗西斯·克里克" , wiki: "Francis Crick" },
    { type: "work", name: "Eon (Greg Bear)", name_zh: "《永世》(格雷格·贝尔)" },
    { type: "person", name: "Cordwainer Smith", name_zh: "考德怀纳·史密斯" },
  ],

  // ─── Future Age (late) ───
  "artificial-womb": [
    { type: "unit", name: "Biobag (CHOP, 2017)", name_zh: "Biobag生物袋", wiki: "Artificial womb" },
    { type: "work", name: "EctoLife (concept)", name_zh: "EctoLife概念" , url: "https://www.designboom.com/technology/hashem-al-ghaili-ectolife-the-worlds-first-artificial-womb-facility-12-14-2022/" },
    { type: "work", name: "Brave New World (Huxley)", name_zh: "《美丽新世界》(赫胥黎)" },
    { type: "person", name: "Aldous Huxley (literary precursor)", name_zh: "奥尔德斯·赫胥黎", wiki: "Aldous Huxley" },
  ],
  "closed-cycle-cities": [
    { type: "wonder", name: "NEOM (Saudi Arabia)", name_zh: "NEOM新城" },
    { type: "wonder", name: "Songdo IBD (Korea)", name_zh: "松岛国际商务区" },
    { type: "wonder", name: "Masdar City (UAE)", name_zh: "马斯达尔城" },
    { type: "wonder", name: "Biosphere 2", name_zh: "生物圈二号" },
    { type: "person", name: "Vincent Callebaut", name_zh: "文森特·卡勒博" },
  ],
  "personalized-medicine": [
    { type: "work", name: "Whole-genome sequencing at birth", name_zh: "新生儿全基因组测序" },
    { type: "work", name: "Pharmacogenomics", name_zh: "药物基因组学" },
    { type: "org", name: "Isomorphic Labs", name_zh: "Isomorphic Labs" },
    { type: "org", name: "Insilico Medicine", name_zh: "Insilico Medicine" },
    { type: "unit", name: "AlphaFold-derived drug design", name_zh: "AlphaFold药物设计" },
  ],
  "printable-organs-on-demand": [
    { type: "org", name: "Prellis Biologics", name_zh: "Prellis Biologics" },
    { type: "org", name: "United Therapeutics", name_zh: "United Therapeutics" },
    { type: "org", name: "Organovo", name_zh: "Organovo" },
    { type: "resource", name: "Bioink", name_zh: "生物墨水" },
    { type: "person", name: "Anthony Atala (continuation)", name_zh: "安东尼·阿塔拉", wiki: "Anthony Atala" },
  ],
  "ai-coordination-treaty": [
    { type: "work", name: "Bletchley Declaration (2023)", name_zh: "布莱切利宣言", wiki: "AI Safety Summit" },
    { type: "work", name: "EU AI Act", name_zh: "欧盟人工智能法案" },
    { type: "org", name: "International Atomic Energy Agency (model)", name_zh: "国际原子能机构(模板)", wiki: "International Atomic Energy Agency" },
    { type: "person", name: "Stuart Russell", name_zh: "斯图尔特·罗素", wiki: "Stuart J. Russell" },
    { type: "person", name: "Yoshua Bengio", name_zh: "约书亚·本吉奥" },
  ],
  "direct-ai-democracy": [
    { type: "unit", name: "vTaiwan platform", name_zh: "vTaiwan平台", wiki: "Digital democracy in Taiwan" },
    { type: "unit", name: "Pol.is", name_zh: "Pol.is", wiki: "Pol.is" },
    { type: "person", name: "Audrey Tang", name_zh: "唐凤" },
    { type: "person", name: "Colin Megill (Pol.is)", name_zh: "科林·梅吉尔", wiki: "Pol.is" },
    { type: "work", name: "Deliberative democracy", name_zh: "审议民主" },
  ],
  "lunar-industrial-base": [
    { type: "resource", name: "Helium-3 (lunar)", name_zh: "氦-3(月球)", wiki: "Helium-3" },
    { type: "unit", name: "Mass driver (electromagnetic launch)", name_zh: "电磁质量驱动器", wiki: "Mass driver" },
    { type: "resource", name: "Lunar regolith", name_zh: "月壤" },
    { type: "org", name: "Moon Village (ESA)", name_zh: "月球村(欧空局)", wiki: "Moonbase" },
    { type: "work", name: "ISRU (in-situ resource utilization)", name_zh: "原位资源利用", wiki: "In situ resource utilization" },
  ],
  "asteroid-belt-settlement": [
    { type: "wonder", name: "Ceres (dwarf planet)", name_zh: "谷神星" },
    { type: "wonder", name: "4 Vesta", name_zh: "灶神星" },
    { type: "work", name: "The Expanse (Corey, novels)", name_zh: "《苍穹浩瀚》" },
    { type: "unit", name: "Belters (cultural identity)", name_zh: "带客(文化身份)" , wiki: false },
  ],
  "memory-editing": [
    { type: "person", name: "Karim Nader", name_zh: "卡里姆·纳德" },
    { type: "person", name: "Susumu Tonegawa", name_zh: "利根川进" },
    { type: "work", name: "Optogenetics", name_zh: "光遗传学" },
    { type: "work", name: "Eternal Sunshine of the Spotless Mind", name_zh: "《暖暖内含光》" },
    { type: "work", name: "Total Recall (Dick / Verhoeven)", name_zh: "《全面回忆》(迪克 / 范霍文)", wiki: "Total Recall (1990 film)" },
  ],
  "cybernetic-enhancement": [
    { type: "person", name: "Hugh Herr", name_zh: "休·赫尔" },
    { type: "person", name: "Neil Harbisson (cyborg artist)", name_zh: "尼尔·哈比森" },
    { type: "work", name: "DARPA HAPTIX program", name_zh: "DARPA HAPTIX项目" },
    { type: "unit", name: "Powered exoskeleton", name_zh: "动力外骨骼" },
    { type: "unit", name: "Bionic limb", name_zh: "仿生肢体" },
  ],
  "orbital-ring": [
    { type: "person", name: "Paul Birch", name_zh: "保罗·伯奇", wiki: false },
    { type: "person", name: "Isaac Arthur (futurist)", name_zh: "艾萨克·亚瑟", wiki: "Isaac Arthur" },
    { type: "unit", name: "Skyhook (megastructure)", name_zh: "天钩", wiki: "Skyhook (structure)" },
    { type: "unit", name: "Lofstrom loop", name_zh: "洛夫斯特罗姆环", wiki: "Launch loop" },
  ],
  "universal-disease-eradication": [
    { type: "wonder", name: "Smallpox eradication (1980)", name_zh: "天花根除" },
    { type: "wonder", name: "Polio eradication (in progress)", name_zh: "脊髓灰质炎根除" },
    { type: "work", name: "Gene drive (Anopheles)", name_zh: "基因驱动(按蚊)" },
    { type: "org", name: "Bill & Melinda Gates Foundation", name_zh: "比尔及梅琳达·盖茨基金会" },
    { type: "org", name: "World Health Organization (WHO)", name_zh: "世界卫生组织" },
  ],

  // ─── Future / Far-Future weapons ───
  "cyber-kinetic-warfare": [
    { type: "unit", name: "Stuxnet", name_zh: "震网病毒" , wiki: "Stuxnet" },
    { type: "unit", name: "NotPetya", name_zh: "NotPetya 蠕虫" , wiki: "Petya and NotPetya" },
    { type: "org", name: "U.S. Cyber Command", name_zh: "美国网络司令部" , wiki: "United States Cyber Command" },
    { type: "work", name: "Tallinn Manual", name_zh: "《塔林手册》" , wiki: "Tallinn Manual" },
  ],
  "directed-energy-weapons": [
    { type: "unit", name: "HELIOS Laser", name_zh: "HELIOS 高能激光" , url: "https://www.lockheedmartin.com/en-us/news/features/2021/more-than-a-laser-helios-is-an-integrated-weapon-system.html" },
    { type: "unit", name: "DragonFire", name_zh: "龙火激光武器" , url: "https://www.gov.uk/government/news/boost-for-armed-forces-as-new-laser-weapon-takes-down-high-speed-drones" },
    { type: "unit", name: "Iron Beam", name_zh: "铁束激光" , wiki: "Iron Beam" },
    { type: "org", name: "U.S. Naval Research Laboratory", name_zh: "美国海军研究实验室" , wiki: "United States Naval Research Laboratory" },
  ],
  "drone-swarms": [
    { type: "unit", name: "Bayraktar TB2", name_zh: "拜拉克塔尔 TB2" , wiki: "Bayraktar TB2" },
    { type: "unit", name: "Switchblade 600", name_zh: "弹簧刀 600 巡飞弹" , wiki: "AeroVironment Switchblade" },
    { type: "org", name: "Pentagon Replicator Initiative", name_zh: "五角大楼复制者计划" , url: "https://www.diu.mil/latest/implementing-the-department-of-defense-replicator-initiative-to-accelerate" },
    { type: "org", name: "Anduril Industries", name_zh: "Anduril 工业" , wiki: "Anduril Industries" },
  ],
  "anti-satellite-warfare": [
    { type: "unit", name: "Fengyun-1C ASAT Test", name_zh: "风云一号 C 反卫星试验" , wiki: "2007 Chinese anti-satellite missile test" },
    { type: "unit", name: "Mission Shakti", name_zh: "印度沙克提行动" , wiki: "Mission Shakti" },
    { type: "org", name: "U.S. Space Force", name_zh: "美国太空军" , wiki: "United States Space Force" },
    { type: "org", name: "China PLA Strategic Support Force", name_zh: "中国人民解放军战略支援部队" , wiki: "People's Liberation Army Strategic Support Force" },
  ],
  "engineered-pathogen-defense": [
    { type: "org", name: "BARDA", name_zh: "美国生物医学高级研究开发管理局" , wiki: "Biomedical Advanced Research and Development Authority" },
    { type: "org", name: "DARPA Pandemic Prevention Platform", name_zh: "DARPA 大流行病预防平台" , url: "https://www.darpa.mil/program/pandemic-prevention-platform" },
    { type: "resource", name: "Metagenomic biosurveillance", name_zh: "宏基因组生物监测" , wiki: "Metagenomics" },
    { type: "work", name: "Biological Weapons Convention", name_zh: "《禁止生物武器公约》" , wiki: "Biological Weapons Convention" },
  ],
  "strategic-memetic-warfare": [
    { type: "unit", name: "AI persuasion campaign", name_zh: "AI 说服运动" , wiki: false },
    { type: "org", name: "Internet Research Agency", name_zh: "互联网研究机构" , wiki: "Internet Research Agency" },
    { type: "resource", name: "Synthetic media saturation", name_zh: "合成媒体饱和攻击" , wiki: "Synthetic media" },
    { type: "work", name: "Active Measures doctrine", name_zh: "积极措施学说" , wiki: "Active measures" },
  ],
  "self-replicating-combat-drones": [
    { type: "unit", name: "Von Neumann combat probe", name_zh: "冯·诺依曼战斗探测器" , wiki: "Von Neumann probe" },
    { type: "resource", name: "Autonomous weapons accord", name_zh: "自主武器公约" , wiki: false },
    { type: "work", name: "Convention on Self-Replicating Systems", name_zh: "《自复制系统公约》" , wiki: false },
  ],
  "planetary-defense-system": [
    { type: "unit", name: "DART Spacecraft", name_zh: "DART 双小行星撞击试验" , wiki: "Double Asteroid Redirection Test" },
    { type: "unit", name: "NEO Surveyor", name_zh: "近地天体测量探测器" , wiki: "NEO Surveyor" },
    { type: "org", name: "UN Office for Outer Space Affairs", name_zh: "联合国外层空间事务厅" , wiki: "United Nations Office for Outer Space Affairs" },
    { type: "wonder", name: "Solar System Defense Grid", name_zh: "太阳系防御网格" , wiki: false },
  ],
  "relativistic-kinetic-weapon": [
    { type: "unit", name: "Casaba-Howitzer", name_zh: "卡萨巴榴弹炮" , wiki: "Casaba-Howitzer" },
    { type: "unit", name: "Project Longshot", name_zh: "长射计划" , wiki: "Project Longshot" },
    { type: "resource", name: "Interstellar deterrence", name_zh: "星际威慑" , wiki: false },
  ],
  "antimatter-weapon": [
    { type: "resource", name: "Positron annihilation device", name_zh: "正电子湮灭装置" , wiki: "Positron annihilation" },
    { type: "resource", name: "Antiproton arsenal", name_zh: "反质子军火库" , wiki: "Antiproton" },
    { type: "org", name: "Air Force Research Laboratory", name_zh: "美国空军研究实验室" , wiki: "Air Force Research Laboratory" },
  ],

  // ─── Far Future (2500-2700 fill) ───
  "black-hole-engineering": [
    { type: "resource", name: "Penrose process", name_zh: "彭罗斯过程" , wiki: "Penrose process" },
    { type: "resource", name: "Hawking-radiation harvester", name_zh: "霍金辐射收集器" , wiki: "Hawking radiation" },
    { type: "unit", name: "Kerr power plant", name_zh: "克尔黑洞电站" , wiki: "Kerr metric" },
    { type: "work", name: "Black-hole bomb", name_zh: "黑洞炸弹理论" , wiki: "Black hole bomb" },
  ],
  "galactic-communication-network": [
    { type: "unit", name: "Neutrino relay station", name_zh: "中微子中继站" , wiki: false },
    { type: "resource", name: "Long-baseline laser link", name_zh: "长基线激光通信" , wiki: "Free-space optical communication" },
    { type: "work", name: "Galactic Asynchronous Protocol", name_zh: "《银河异步协议》" , wiki: false },
    { type: "wonder", name: "Sagittarius A* relay hub", name_zh: "人马座 A* 中继枢纽" , wiki: "Sagittarius A*" },
  ],
  "pre-warp-interstellar-trade": [
    { type: "resource", name: "Slow-trade contract", name_zh: "慢速贸易合约" , wiki: false },
    { type: "resource", name: "Light-lag arbitrage", name_zh: "光速延迟套利" , wiki: false },
    { type: "org", name: "Interstellar Mercantile Consortium", name_zh: "星际商业联合体" , wiki: false },
    { type: "unit", name: "Sub-light freighter", name_zh: "亚光速货船" , wiki: false },
  ],
  "pan-galactic-coordination-ai": [
    { type: "unit", name: "Galactic Mind substrate", name_zh: "银河心智基质" , wiki: false },
    { type: "resource", name: "Inter-instance value reconciliation", name_zh: "实例间价值校准" , wiki: false },
    { type: "work", name: "Pan-Galactic Coordination Treaty", name_zh: "《泛银河协调条约》" , wiki: false },
  ],
  "femto-engineering": [
    { type: "resource", name: "Designer atomic nucleus", name_zh: "定制原子核" , wiki: "Synthetic element" },
    { type: "resource", name: "Nuclear-isomer battery", name_zh: "核同质异能素电池" , wiki: "Nuclear isomer" },
    { type: "unit", name: "Femto-fabricator", name_zh: "飞米制造机" , wiki: "Femtotechnology" },
  ],
  "vacuum-energy-extraction": [
    { type: "unit", name: "Casimir-cavity generator", name_zh: "卡西米尔腔发电机" , wiki: "Casimir effect" },
    { type: "resource", name: "Zero-point energy cell", name_zh: "零点能电池" , wiki: "Zero-point energy" },
    { type: "resource", name: "Dynamical Casimir emitter", name_zh: "动态卡西米尔发射器" , wiki: false },
  ],
  "strange-quark-matter": [
    { type: "resource", name: "Strange-matter ingot", name_zh: "奇异物质锭" , wiki: "Strange matter" },
    { type: "resource", name: "Color-flavor-locked phase", name_zh: "色味锁定相" , wiki: "Color–flavor locking" },
    { type: "unit", name: "Quark-matter hull", name_zh: "夸克物质船体" , wiki: "Quark star" },
  ],
  "dark-energy-engineering": [
    { type: "resource", name: "Negative-energy field", name_zh: "负能量场" , wiki: "Negative energy" },
    { type: "resource", name: "Cosmological-constant modulator", name_zh: "宇宙学常数调制器" , wiki: "Cosmological constant" },
    { type: "unit", name: "Alcubierre precursor coil", name_zh: "阿尔库别雷前驱线圈" , wiki: "Alcubierre drive" },
  ],

  // ─── Arts & Entertainment (atomic / information) ───
  "abstract-expressionism": [
    { type: "person", name: "Jackson Pollock", name_zh: "杰克逊·波洛克", wiki: "Jackson Pollock" },
    { type: "person", name: "Mark Rothko", name_zh: "马克·罗斯科", wiki: "Mark Rothko" },
    { type: "person", name: "Willem de Kooning", name_zh: "威廉·德·库宁", wiki: "Willem de Kooning" },
    { type: "work", name: "Number 1A, 1948", name_zh: "《1A 号,1948》", wiki: "Number 1A, 1948" },
    { type: "org", name: "New York School", name_zh: "纽约画派", wiki: "New York School (art)" },
  ],
  "lp-vinyl-record": [
    { type: "resource", name: "33⅓ rpm microgroove", name_zh: "33⅓ 转长播放唱片", wiki: "LP record" },
    { type: "resource", name: "45 rpm single", name_zh: "45 转单曲唱片", wiki: "Single (music)" },
    { type: "org", name: "Columbia Records", name_zh: "哥伦比亚唱片公司", wiki: "Columbia Records" },
    { type: "work", name: "Sgt. Pepper's Lonely Hearts Club Band", name_zh: "《佩珀军士的孤独之心俱乐部乐队》", wiki: "Sgt. Pepper's Lonely Hearts Club Band" },
  ],
  "color-television": [
    { type: "resource", name: "NTSC standard", name_zh: "NTSC 制式", wiki: "NTSC" },
    { type: "resource", name: "PAL standard", name_zh: "PAL 制式", wiki: "PAL" },
    { type: "org", name: "RCA", name_zh: "美国无线电公司", wiki: "RCA" },
    { type: "unit", name: "RCA CT-100", name_zh: "RCA CT-100 彩色电视机", wiki: "RCA CT-100" },
  ],
  "video-games": [
    { type: "work", name: "Pong", name_zh: "《乓》", wiki: "Pong" },
    { type: "work", name: "Space Invaders", name_zh: "《太空侵略者》", wiki: "Space Invaders" },
    { type: "work", name: "Pac-Man", name_zh: "《吃豆人》", wiki: "Pac-Man" },
    { type: "unit", name: "Magnavox Odyssey", name_zh: "美格福斯奥德赛", wiki: "Magnavox Odyssey" },
    { type: "unit", name: "Atari 2600", name_zh: "雅达利 2600", wiki: "Atari 2600" },
    { type: "org", name: "Nintendo", name_zh: "任天堂", wiki: "Nintendo" },
  ],
  "cgi-cinema": [
    { type: "work", name: "Jurassic Park", name_zh: "《侏罗纪公园》", wiki: "Jurassic Park (film)" },
    { type: "work", name: "Terminator 2: Judgment Day", name_zh: "《终结者2:审判日》", wiki: "Terminator 2: Judgment Day" },
    { type: "work", name: "Toy Story", name_zh: "《玩具总动员》", wiki: "Toy Story" },
    { type: "org", name: "Industrial Light & Magic", name_zh: "工业光魔", wiki: "Industrial Light & Magic" },
    { type: "org", name: "Pixar", name_zh: "皮克斯", wiki: "Pixar" },
  ],
  "anime-globalization": [
    { type: "work", name: "Akira", name_zh: "《阿基拉》", wiki: "Akira (1988 film)" },
    { type: "work", name: "Spirited Away", name_zh: "《千与千寻》", wiki: "Spirited Away" },
    { type: "work", name: "Neon Genesis Evangelion", name_zh: "《新世纪福音战士》", wiki: "Neon Genesis Evangelion" },
    { type: "work", name: "Pokémon", name_zh: "《精灵宝可梦》", wiki: "Pokémon" },
    { type: "org", name: "Studio Ghibli", name_zh: "吉卜力工作室", wiki: "Studio Ghibli" },
    { type: "org", name: "Crunchyroll", name_zh: "Crunchyroll", wiki: "Crunchyroll" },
  ],

  // ─── Near Future / Far Future arts & entertainment ───
  "synthetic-performers": [
    { type: "unit", name: "Hatsune Miku", name_zh: "初音未来", wiki: "Hatsune Miku" },
    { type: "unit", name: "Lil Miquela", name_zh: "Lil Miquela", wiki: "Lil Miquela" },
    { type: "unit", name: "Kizuna AI", name_zh: "绊爱", wiki: "Kizuna AI" },
    { type: "resource", name: "Vocaloid", name_zh: "VOCALOID", wiki: "Vocaloid" },
    { type: "org", name: "Crypton Future Media", name_zh: "克里普敦未来媒体", wiki: "Crypton Future Media" },
  ],
  "procedural-infinite-worlds": [
    { type: "work", name: "No Man's Sky", name_zh: "《无人深空》", wiki: "No Man's Sky" },
    { type: "work", name: "Minecraft", name_zh: "《我的世界》", wiki: "Minecraft" },
    { type: "work", name: "Dwarf Fortress", name_zh: "《矮人要塞》", wiki: "Dwarf Fortress" },
    { type: "resource", name: "Procedural generation", name_zh: "程序化生成", wiki: "Procedural generation" },
  ],
  "bio-art": [
    { type: "person", name: "Eduardo Kac", name_zh: "爱德华多·卡茨", wiki: "Eduardo Kac" },
    { type: "work", name: "GFP Bunny", name_zh: "《GFP 兔子》", wiki: "GFP Bunny" },
    { type: "person", name: "Stelarc", name_zh: "斯特拉克", wiki: "Stelarc" },
    { type: "org", name: "SymbioticA", name_zh: "SymbioticA 实验室", wiki: "SymbioticA" },
    { type: "resource", name: "Transgenic art", name_zh: "转基因艺术", wiki: "Transgenic art" },
  ],
  "mind-linked-collective-art": [
    { type: "resource", name: "Hive mind", name_zh: "蜂巢思维", wiki: "Hive mind" },
    { type: "resource", name: "Telepathy", name_zh: "心灵感应", wiki: "Telepathy" },
    { type: "work", name: "Sleep No More", name_zh: "《不眠之夜》", wiki: "Sleep No More (2011 play)" },
    { type: "unit", name: "Collective-consciousness installation", name_zh: "集体意识装置", wiki: false },
  ],
  "engineered-sensory-modalities": [
    { type: "resource", name: "Synesthesia", name_zh: "联觉", wiki: "Synesthesia" },
    { type: "resource", name: "Sensory substitution", name_zh: "感官替代", wiki: "Sensory substitution" },
    { type: "person", name: "Neil Harbisson", name_zh: "尼尔·哈维森", wiki: "Neil Harbisson" },
    { type: "unit", name: "Magnetoreception implant", name_zh: "磁感受器植入", wiki: false },
  ],
  "ai-native-art-forms": [
    { type: "resource", name: "AI art", name_zh: "AI 艺术", wiki: "AI art" },
    { type: "resource", name: "Generative art", name_zh: "生成艺术", wiki: "Generative art" },
    { type: "unit", name: "Substrate-specific composition", name_zh: "基质特定作品", wiki: false },
    { type: "work", name: "AI-incomprehensible artwork", name_zh: "AI 不可理解作品", wiki: false },
  ],
  "stellar-scale-spectacle": [
    { type: "resource", name: "Shkadov thruster", name_zh: "什卡多夫推进器", wiki: "Shkadov thruster" },
    { type: "resource", name: "Variable star", name_zh: "变星", wiki: "Variable star" },
    { type: "unit", name: "Modulated supergiant performance", name_zh: "调制超巨星表演", wiki: false },
    { type: "wonder", name: "Galactic light-show installation", name_zh: "银河光秀装置", wiki: false },
  ],
  "pan-galactic-festival": [
    { type: "resource", name: "Cultural festival", name_zh: "文化节", wiki: "Festival" },
    { type: "unit", name: "Synchronized civilization rite", name_zh: "同步文明仪式", wiki: false },
    { type: "work", name: "Galactic Anthem", name_zh: "《银河颂歌》", wiki: false },
    { type: "wonder", name: "Pan-Galactic Coordination Ceremony", name_zh: "泛银河协调典礼", wiki: false },
  ],

  // ─── Culture / Philosophy / Sociology ───
  "bauhaus": [
    { type: "person", name: "Walter Gropius", name_zh: "瓦尔特·格罗皮乌斯", wiki: "Walter Gropius" },
    { type: "person", name: "László Moholy-Nagy", name_zh: "拉斯洛·莫霍利-纳吉", wiki: "László Moholy-Nagy" },
    { type: "person", name: "Mies van der Rohe", name_zh: "密斯·凡·德罗", wiki: "Ludwig Mies van der Rohe" },
    { type: "work", name: "Bauhaus Manifesto", name_zh: "《包豪斯宣言》", wiki: "Bauhaus" },
    { type: "unit", name: "Wassily Chair", name_zh: "瓦西里椅", wiki: "Wassily Chair" },
    { type: "org", name: "Bauhaus-Universität Weimar", name_zh: "魏玛包豪斯大学", wiki: "Bauhaus-Universität Weimar" },
  ],
  "frankfurt-school": [
    { type: "person", name: "Theodor Adorno", name_zh: "西奥多·阿多诺", wiki: "Theodor W. Adorno" },
    { type: "person", name: "Max Horkheimer", name_zh: "马克斯·霍克海默", wiki: "Max Horkheimer" },
    { type: "person", name: "Herbert Marcuse", name_zh: "赫伯特·马尔库塞", wiki: "Herbert Marcuse" },
    { type: "person", name: "Walter Benjamin", name_zh: "瓦尔特·本雅明", wiki: "Walter Benjamin" },
    { type: "person", name: "Jürgen Habermas", name_zh: "于尔根·哈贝马斯", wiki: "Jürgen Habermas" },
    { type: "work", name: "Dialectic of Enlightenment", name_zh: "《启蒙辩证法》", wiki: "Dialectic of Enlightenment" },
    { type: "org", name: "Institute for Social Research", name_zh: "社会研究所", wiki: "Institute for Social Research" },
  ],
  "universal-human-rights": [
    { type: "work", name: "Universal Declaration of Human Rights", name_zh: "《世界人权宣言》", wiki: "Universal Declaration of Human Rights" },
    { type: "person", name: "Eleanor Roosevelt", name_zh: "埃莉诺·罗斯福", wiki: "Eleanor Roosevelt" },
    { type: "org", name: "United Nations Human Rights Commission", name_zh: "联合国人权委员会", wiki: "United Nations Commission on Human Rights" },
    { type: "work", name: "International Covenant on Civil and Political Rights", name_zh: "《公民权利和政治权利国际公约》", wiki: "International Covenant on Civil and Political Rights" },
    { type: "org", name: "Amnesty International", name_zh: "国际特赦组织", wiki: "Amnesty International" },
  ],
  "cybernetics": [
    { type: "person", name: "Norbert Wiener", name_zh: "诺伯特·维纳", wiki: "Norbert Wiener" },
    { type: "person", name: "Claude Shannon", name_zh: "克劳德·香农", wiki: "Claude Shannon" },
    { type: "work", name: "Cybernetics: or Control and Communication in the Animal and the Machine", name_zh: "《控制论》", wiki: "Cybernetics: Or Control and Communication in the Animal and the Machine" },
    { type: "org", name: "Macy Conferences", name_zh: "梅西会议", wiki: "Macy conferences" },
    { type: "unit", name: "Project Cybersyn", name_zh: "赛博协同工程", wiki: "Project Cybersyn" },
  ],
  "neoliberalism": [
    { type: "person", name: "Milton Friedman", name_zh: "米尔顿·弗里德曼", wiki: "Milton Friedman" },
    { type: "person", name: "Friedrich Hayek", name_zh: "弗里德里希·哈耶克", wiki: "Friedrich Hayek" },
    { type: "person", name: "Margaret Thatcher", name_zh: "玛格丽特·撒切尔", wiki: "Margaret Thatcher" },
    { type: "person", name: "Ronald Reagan", name_zh: "罗纳德·里根", wiki: "Ronald Reagan" },
    { type: "work", name: "Capitalism and Freedom", name_zh: "《资本主义与自由》", wiki: "Capitalism and Freedom" },
    { type: "org", name: "Mont Pelerin Society", name_zh: "朝圣山学社", wiki: "Mont Pelerin Society" },
    { type: "resource", name: "Washington Consensus", name_zh: "华盛顿共识", wiki: "Washington Consensus" },
  ],
  "degrowth-economics": [
    { type: "person", name: "Herman Daly", name_zh: "赫尔曼·戴利", wiki: "Herman Daly" },
    { type: "person", name: "Nicholas Georgescu-Roegen", name_zh: "尼古拉斯·乔治斯库-罗根", wiki: "Nicholas Georgescu-Roegen" },
    { type: "person", name: "Jason Hickel", name_zh: "贾森·希克尔", wiki: "Jason Hickel" },
    { type: "work", name: "Less Is More", name_zh: "《少即是多》", wiki: "Jason Hickel" },
    { type: "work", name: "Doughnut Economics", name_zh: "《甜甜圈经济学》", wiki: "Doughnut (economic model)" },
    { type: "resource", name: "Steady-state economy", name_zh: "稳态经济", wiki: "Steady-state economy" },
  ],
  "solarpunk": [
    { type: "resource", name: "Solarpunk aesthetic", name_zh: "太阳朋克美学", wiki: "Solarpunk" },
    { type: "work", name: "Solarpunk: Ecological and Fantastical Stories", name_zh: "《太阳朋克:生态与奇幻故事集》", wiki: "Solarpunk" },
    { type: "unit", name: "Photovoltaic façade", name_zh: "光伏外立面", wiki: "Photovoltaics" },
    { type: "org", name: "Sunrise Movement", name_zh: "日出运动", wiki: "Sunrise Movement" },
  ],
  "constructed-religions": [
    { type: "resource", name: "Religion of Humanity", name_zh: "人性宗教", wiki: "Religion of Humanity" },
    { type: "org", name: "Bahá'í Faith", name_zh: "巴哈伊信仰", wiki: "Bahá'í Faith" },
    { type: "resource", name: "New religious movement", name_zh: "新兴宗教运动", wiki: "New religious movement" },
    { type: "work", name: "Posthuman liturgy", name_zh: "后人类礼仪", wiki: false },
  ],
  "substrate-pluralism": [
    { type: "person", name: "David Chalmers", name_zh: "大卫·查尔默斯", wiki: "David Chalmers" },
    { type: "person", name: "Susan Schneider", name_zh: "苏珊·施奈德", wiki: "Susan Schneider (philosopher)" },
    { type: "resource", name: "Substrate independence", name_zh: "基质独立性", wiki: "Substrate independence" },
    { type: "work", name: "Substrate-pluralism charter", name_zh: "基质多元主义宪章", wiki: false },
  ],
  "galactic-citizenship": [
    { type: "resource", name: "Cosmopolitanism", name_zh: "世界主义", wiki: "Cosmopolitanism" },
    { type: "work", name: "Galactic Constitution", name_zh: "《银河宪法》", wiki: false },
    { type: "org", name: "Pan-Galactic Civic Tribunal", name_zh: "泛银河公民法庭", wiki: false },
  ],
  "speciation-ethics": [
    { type: "work", name: "Last and First Men", name_zh: "《最后和最初的人》", wiki: "Last and First Men" },
    { type: "work", name: "Star Maker", name_zh: "《造星者》", wiki: "Star Maker (novel)" },
    { type: "resource", name: "Posthuman speciation", name_zh: "后人类物种分化", wiki: "Speciation" },
    { type: "work", name: "Inter-species moral covenant", name_zh: "种间道德盟约", wiki: false },
  ],

  // ─── More warfare (enlightenment / industrial) ───
  "linear-infantry-tactics": [
    { type: "person", name: "Frederick the Great", name_zh: "腓特烈大帝", wiki: "Frederick the Great" },
    { type: "unit", name: "Prussian Line Infantry", name_zh: "普鲁士线列步兵", wiki: "Prussian Army" },
    { type: "work", name: "Reglement of 1743", name_zh: "《1743 年训练条令》", wiki: false },
    { type: "resource", name: "Volley fire", name_zh: "齐射", wiki: "Volley fire" },
  ],
  "standardized-field-artillery": [
    { type: "person", name: "Jean-Baptiste de Gribeauval", name_zh: "让-巴蒂斯特·德·格里博瓦尔", wiki: "Jean-Baptiste Vaquette de Gribeauval" },
    { type: "unit", name: "12-pounder field gun", name_zh: "12 磅野战炮", wiki: "12-pounder long gun" },
    { type: "resource", name: "Gribeauval system", name_zh: "格里博瓦尔体系", wiki: "Gribeauval system" },
    { type: "org", name: "École d'application de l'artillerie", name_zh: "炮兵应用学校", wiki: false },
  ],
  "ironclad-warship": [
    { type: "unit", name: "HMS Warrior", name_zh: "HMS 勇士号", wiki: "HMS Warrior (1860)" },
    { type: "unit", name: "USS Monitor", name_zh: "美国海军舰艇监视者号", wiki: "USS Monitor" },
    { type: "unit", name: "CSS Virginia", name_zh: "CSS 弗吉尼亚号", wiki: "CSS Virginia" },
    { type: "unit", name: "La Gloire", name_zh: "光荣号", wiki: "French ironclad Gloire" },
    { type: "work", name: "Battle of Hampton Roads", name_zh: "汉普顿锚地海战", wiki: "Battle of Hampton Roads" },
  ],
  "bolt-action-rifle": [
    { type: "person", name: "Paul Mauser", name_zh: "保罗·毛瑟", wiki: "Paul Mauser" },
    { type: "unit", name: "Mauser Model 1898", name_zh: "毛瑟 1898 步枪", wiki: "Mauser Model 1898" },
    { type: "unit", name: "Lee-Enfield", name_zh: "李-恩菲尔德步枪", wiki: "Lee–Enfield" },
    { type: "unit", name: "Mosin-Nagant", name_zh: "莫辛-纳甘步枪", wiki: "Mosin–Nagant" },
    { type: "unit", name: "Dreyse Needle Gun", name_zh: "德赖斯针发枪", wiki: "Dreyse needle gun" },
  ],
  "high-explosives": [
    { type: "person", name: "Alfred Nobel", name_zh: "阿尔弗雷德·诺贝尔", wiki: "Alfred Nobel" },
    { type: "resource", name: "Dynamite", name_zh: "硝化甘油炸药", wiki: "Dynamite" },
    { type: "resource", name: "TNT", name_zh: "三硝基甲苯", wiki: "TNT" },
    { type: "resource", name: "Nitroglycerin", name_zh: "硝化甘油", wiki: "Nitroglycerin" },
    { type: "org", name: "Nobel Industries", name_zh: "诺贝尔工业", wiki: "Nobel Industries" },
  ],
  "modern-quick-firing-artillery": [
    { type: "unit", name: "French 75mm", name_zh: "法国 75 毫米速射炮", wiki: "Canon de 75 modèle 1897" },
    { type: "unit", name: "Krupp 77mm", name_zh: "克虏伯 77 毫米炮", wiki: "7.7 cm FK 96" },
    { type: "unit", name: "British 18-pounder", name_zh: "英军 18 磅野战炮", wiki: "Ordnance QF 18-pounder" },
    { type: "resource", name: "Hydropneumatic recoil", name_zh: "液气缓冲后座装置", wiki: "Recoil" },
  ],
  "dreadnought-battleship": [
    { type: "unit", name: "HMS Dreadnought", name_zh: "HMS 无畏号", wiki: "HMS Dreadnought (1906)" },
    { type: "unit", name: "SMS Bayern", name_zh: "SMS 巴伐利亚号", wiki: "SMS Bayern" },
    { type: "unit", name: "USS Texas", name_zh: "USS 德克萨斯号", wiki: "USS Texas (BB-35)" },
    { type: "work", name: "Battle of Jutland", name_zh: "日德兰海战", wiki: "Battle of Jutland" },
    { type: "person", name: "John Fisher", name_zh: "约翰·费舍尔", wiki: "John Fisher, 1st Baron Fisher" },
  ],

  // ─── Fusion power decomposition ───
  "inertial-confinement-fusion": [
    { type: "unit", name: "National Ignition Facility", name_zh: "国家点火装置", wiki: "National Ignition Facility" },
    { type: "org", name: "Lawrence Livermore National Laboratory", name_zh: "劳伦斯利弗莫尔国家实验室", wiki: "Lawrence Livermore National Laboratory" },
    { type: "resource", name: "Inertial confinement fusion", name_zh: "惯性约束聚变", wiki: "Inertial confinement fusion" },
    { type: "unit", name: "Laser Mégajoule", name_zh: "兆焦耳激光装置", wiki: "Laser Mégajoule" },
  ],
  "magnetic-confinement-fusion": [
    { type: "unit", name: "ITER", name_zh: "国际热核聚变实验堆", wiki: "ITER" },
    { type: "unit", name: "Joint European Torus", name_zh: "欧洲联合环", wiki: "Joint European Torus" },
    { type: "unit", name: "SPARC", name_zh: "SPARC 紧凑型托卡马克", wiki: "SPARC (tokamak)" },
    { type: "unit", name: "EAST", name_zh: "东方超环", wiki: "Experimental Advanced Superconducting Tokamak" },
    { type: "resource", name: "Tokamak", name_zh: "托卡马克", wiki: "Tokamak" },
    { type: "resource", name: "Stellarator", name_zh: "仿星器", wiki: "Stellarator" },
    { type: "org", name: "Commonwealth Fusion Systems", name_zh: "联邦聚变系统公司", wiki: "Commonwealth Fusion Systems" },
  ],
  "tritium-breeding": [
    { type: "resource", name: "Tritium", name_zh: "氚", wiki: "Tritium" },
    { type: "resource", name: "Lithium-6", name_zh: "锂-6", wiki: "Lithium-6" },
    { type: "resource", name: "Tritium breeding ratio", name_zh: "氚增殖比", wiki: "Breeder reactor" },
    { type: "unit", name: "ITER Test Blanket Module", name_zh: "ITER 试验包层模块", wiki: "ITER" },
  ],

  // ─── Particle physics & fusion engineering ───
  "cyclotron": [
    { type: "person", name: "Ernest Lawrence", name_zh: "欧内斯特·劳伦斯", wiki: "Ernest Lawrence" },
    { type: "unit", name: "184-inch Cyclotron", name_zh: "184 英寸回旋加速器", wiki: "184-inch Cyclotron" },
    { type: "org", name: "Lawrence Berkeley National Laboratory", name_zh: "劳伦斯伯克利国家实验室", wiki: "Lawrence Berkeley National Laboratory" },
    { type: "resource", name: "Carbon-14", name_zh: "碳-14", wiki: "Carbon-14" },
  ],
  "synchrotron": [
    { type: "unit", name: "Cosmotron", name_zh: "宇宙级加速器", wiki: "Cosmotron" },
    { type: "unit", name: "Bevatron", name_zh: "高能质子同步加速器", wiki: "Bevatron" },
    { type: "unit", name: "Tevatron", name_zh: "万亿电子伏特加速器", wiki: "Tevatron" },
    { type: "org", name: "Brookhaven National Laboratory", name_zh: "布鲁克黑文国家实验室", wiki: "Brookhaven National Laboratory" },
    { type: "org", name: "Fermilab", name_zh: "费米国家加速器实验室", wiki: "Fermilab" },
    { type: "resource", name: "Antiproton", name_zh: "反质子", wiki: "Antiproton" },
  ],
  "quantum-electrodynamics": [
    { type: "person", name: "Richard Feynman", name_zh: "理查德·费曼", wiki: "Richard Feynman" },
    { type: "person", name: "Julian Schwinger", name_zh: "朱利安·施温格", wiki: "Julian Schwinger" },
    { type: "person", name: "Shin'ichirō Tomonaga", name_zh: "朝永振一郎", wiki: "Shin'ichirō Tomonaga" },
    { type: "resource", name: "Feynman diagram", name_zh: "费曼图", wiki: "Feynman diagram" },
    { type: "resource", name: "Renormalization", name_zh: "重正化", wiki: "Renormalization" },
  ],
  "standard-model": [
    { type: "person", name: "Steven Weinberg", name_zh: "史蒂文·温伯格", wiki: "Steven Weinberg" },
    { type: "person", name: "Sheldon Glashow", name_zh: "谢尔顿·格拉肖", wiki: "Sheldon Lee Glashow" },
    { type: "person", name: "Abdus Salam", name_zh: "阿卜杜勒·萨拉姆", wiki: "Abdus Salam" },
    { type: "resource", name: "Quantum chromodynamics", name_zh: "量子色动力学", wiki: "Quantum chromodynamics" },
    { type: "resource", name: "Electroweak interaction", name_zh: "电弱相互作用", wiki: "Electroweak interaction" },
    { type: "resource", name: "Higgs mechanism", name_zh: "希格斯机制", wiki: "Higgs mechanism" },
  ],
  "string-theory": [
    { type: "person", name: "Edward Witten", name_zh: "爱德华·威滕", wiki: "Edward Witten" },
    { type: "person", name: "Michael Green", name_zh: "迈克尔·格林", wiki: "Michael Green (physicist)" },
    { type: "person", name: "John Schwarz", name_zh: "约翰·施瓦茨", wiki: "John Henry Schwarz" },
    { type: "resource", name: "M-theory", name_zh: "M 理论", wiki: "M-theory" },
    { type: "resource", name: "Superstring theory", name_zh: "超弦理论", wiki: "Superstring theory" },
    { type: "resource", name: "AdS/CFT correspondence", name_zh: "AdS/CFT 对应", wiki: "AdS/CFT correspondence" },
  ],
  "lhc": [
    { type: "unit", name: "ATLAS experiment", name_zh: "ATLAS 实验", wiki: "ATLAS experiment" },
    { type: "unit", name: "CMS experiment", name_zh: "CMS 实验", wiki: "Compact Muon Solenoid" },
    { type: "unit", name: "ALICE experiment", name_zh: "ALICE 实验", wiki: "ALICE experiment" },
    { type: "unit", name: "LHCb", name_zh: "LHCb 实验", wiki: "LHCb experiment" },
    { type: "org", name: "CERN", name_zh: "欧洲核子研究组织", wiki: "CERN" },
    { type: "resource", name: "Superconducting magnet", name_zh: "超导磁体", wiki: "Superconducting magnet" },
  ],
  "higgs-discovery": [
    { type: "unit", name: "Higgs boson", name_zh: "希格斯玻色子", wiki: "Higgs boson" },
    { type: "person", name: "Peter Higgs", name_zh: "彼得·希格斯", wiki: "Peter Higgs" },
    { type: "person", name: "François Englert", name_zh: "弗朗索瓦·恩格勒特", wiki: "François Englert" },
    { type: "org", name: "ATLAS Collaboration", name_zh: "ATLAS 合作组", wiki: "ATLAS experiment" },
    { type: "work", name: "Higgs boson observation", name_zh: "希格斯玻色子观测", wiki: "Higgs boson" },
  ],
  "higgs-factory": [
    { type: "unit", name: "International Linear Collider", name_zh: "国际直线对撞机", wiki: "International Linear Collider" },
    { type: "unit", name: "Future Circular Collider", name_zh: "未来环形对撞机", wiki: "Future Circular Collider" },
    { type: "unit", name: "CEPC", name_zh: "中国环形正负电子对撞机", wiki: "Circular Electron Positron Collider" },
    { type: "unit", name: "FCC-ee", name_zh: "FCC-ee 正负电子环", wiki: "Future Circular Collider" },
  ],
  "fusion-materials": [
    { type: "resource", name: "Plasma-facing material", name_zh: "等离子体面对材料", wiki: "Plasma-facing material" },
    { type: "resource", name: "Tungsten armor", name_zh: "钨装甲", wiki: "Tungsten" },
    { type: "resource", name: "Eurofer-97 steel", name_zh: "Eurofer-97 钢", wiki: false },
    { type: "org", name: "IFMIF-DONES", name_zh: "IFMIF-DONES 中子源", wiki: "IFMIF" },
  ],
  "aneutronic-fusion": [
    { type: "resource", name: "Helium-3 fuel cycle", name_zh: "氦-3 燃料循环", wiki: "Helium-3" },
    { type: "resource", name: "Proton-boron-11 reaction", name_zh: "质子-硼-11 反应", wiki: "Aneutronic fusion" },
    { type: "org", name: "TAE Technologies", name_zh: "TAE 技术公司", wiki: "TAE Technologies" },
    { type: "org", name: "Helion Energy", name_zh: "氦聚变能源", wiki: "Helion Energy" },
  ],

  // ─── Interstellar propulsion + quantum precision ───
  "optical-atomic-clock": [
    { type: "person", name: "Jun Ye", name_zh: "叶军", wiki: "Jun Ye (physicist)" },
    { type: "person", name: "David Wineland", name_zh: "戴维·瓦恩兰", wiki: "David J. Wineland" },
    { type: "resource", name: "Optical lattice clock", name_zh: "光晶格钟", wiki: "Optical lattice" },
    { type: "unit", name: "Strontium-87 clock", name_zh: "锶-87 光钟", wiki: "Strontium" },
    { type: "resource", name: "Chronometric geodesy", name_zh: "时频大地测量", wiki: "Chronometric leveling" },
  ],
  "quantum-sensing": [
    { type: "resource", name: "Nitrogen-vacancy center", name_zh: "金刚石氮空位中心", wiki: "Nitrogen-vacancy center" },
    { type: "resource", name: "Atom interferometry", name_zh: "原子干涉术", wiki: "Atom interferometer" },
    { type: "resource", name: "Squeezed light", name_zh: "压缩光", wiki: "Squeezed states of light" },
    { type: "unit", name: "Quantum gravimeter", name_zh: "量子重力仪", wiki: "Gravimeter" },
    { type: "unit", name: "Quantum magnetometer", name_zh: "量子磁力计", wiki: "Magnetometer" },
  ],
  "beamed-sail-propulsion": [
    { type: "org", name: "Breakthrough Starshot", name_zh: "突破摄星计划", wiki: "Breakthrough Starshot" },
    { type: "person", name: "Robert L. Forward", name_zh: "罗伯特·L·福沃德", wiki: "Robert L. Forward" },
    { type: "unit", name: "Lightsail probe", name_zh: "光帆探测器", wiki: "Solar sail" },
    { type: "resource", name: "Phased laser array", name_zh: "相控阵激光", wiki: "Phased array" },
  ],
  "nuclear-pulse-propulsion": [
    { type: "unit", name: "Project Orion", name_zh: "猎户座计划", wiki: "Project Orion (nuclear propulsion)" },
    { type: "unit", name: "Project Daedalus", name_zh: "代达罗斯计划", wiki: "Project Daedalus" },
    { type: "unit", name: "Project Longshot", name_zh: "长射计划", wiki: "Project Longshot" },
    { type: "person", name: "Freeman Dyson", name_zh: "弗里曼·戴森", wiki: "Freeman Dyson" },
    { type: "person", name: "Ted Taylor", name_zh: "西奥多·泰勒", wiki: "Ted Taylor (physicist)" },
  ],
  "bussard-ramjet": [
    { type: "person", name: "Robert W. Bussard", name_zh: "罗伯特·W·巴萨德", wiki: "Robert W. Bussard" },
    { type: "resource", name: "Magnetic ramscoop", name_zh: "磁性冲压舀斗", wiki: false },
    { type: "work", name: "Catalyzed CNO ramjet", name_zh: "催化 CNO 冲压发动机", wiki: false },
    { type: "work", name: "Tau Zero", name_zh: "《时间零》", wiki: "Tau Zero" },
  ],
  "antimatter-propulsion": [
    { type: "resource", name: "Antiproton-catalyzed micro-fusion", name_zh: "反质子催化微聚变", wiki: false },
    { type: "unit", name: "Antimatter rocket", name_zh: "反物质火箭", wiki: "Antimatter rocket" },
    { type: "person", name: "Robert Frisbee", name_zh: "罗伯特·弗里斯比", wiki: false },
    { type: "org", name: "NASA Institute for Advanced Concepts", name_zh: "NASA 先进概念研究院", wiki: "NASA Institute for Advanced Concepts" },
  ],

  // ─── Entropy / thermodynamic computing ───
  "reversible-computing": [
    { type: "person", name: "Rolf Landauer", name_zh: "罗尔夫·兰道尔", wiki: "Rolf Landauer" },
    { type: "person", name: "Charles H. Bennett", name_zh: "查尔斯·H·贝内特", wiki: "Charles H. Bennett (computer scientist)" },
    { type: "person", name: "Edward Fredkin", name_zh: "爱德华·弗雷德金", wiki: "Edward Fredkin" },
    { type: "resource", name: "Landauer's principle", name_zh: "兰道尔原理", wiki: "Landauer's principle" },
    { type: "resource", name: "Toffoli gate", name_zh: "Toffoli 门", wiki: "Toffoli gate" },
    { type: "resource", name: "Adiabatic logic", name_zh: "绝热逻辑", wiki: "Adiabatic logic" },
  ],
  "civilizational-entropy-management": [
    { type: "person", name: "Freeman Dyson", name_zh: "弗里曼·戴森", wiki: "Freeman Dyson" },
    { type: "work", name: "Time Without End", name_zh: "《无终之时》", wiki: "Heat death of the universe" },
    { type: "resource", name: "Black hole thermodynamics", name_zh: "黑洞热力学", wiki: "Black hole thermodynamics" },
    { type: "resource", name: "Bekenstein bound", name_zh: "贝肯斯坦边界", wiki: "Bekenstein bound" },
    { type: "unit", name: "Cascaded-temperature compute shell", name_zh: "级联温度计算壳层", wiki: false },
  ],

  // ─── Mathematics frontier ───
  "univalent-foundations": [
    { type: "person", name: "Vladimir Voevodsky", name_zh: "弗拉基米尔·沃埃沃德斯基", wiki: "Vladimir Voevodsky" },
    { type: "resource", name: "Homotopy type theory", name_zh: "同伦类型论", wiki: "Homotopy type theory" },
    { type: "resource", name: "Univalence axiom", name_zh: "一价公理", wiki: "Univalent foundations" },
    { type: "unit", name: "Coq", name_zh: "Coq 证明助手", wiki: "Coq (software)" },
    { type: "unit", name: "Lean theorem prover", name_zh: "Lean 定理证明器", wiki: "Lean (proof assistant)" },
  ],
  "langlands-program-completion": [
    { type: "person", name: "Robert Langlands", name_zh: "罗伯特·朗兰兹", wiki: "Robert Langlands" },
    { type: "person", name: "Andrew Wiles", name_zh: "安德鲁·怀尔斯", wiki: "Andrew Wiles" },
    { type: "person", name: "Peter Scholze", name_zh: "彼得·朔尔策", wiki: "Peter Scholze" },
    { type: "resource", name: "Langlands program", name_zh: "朗兰兹纲领", wiki: "Langlands program" },
    { type: "resource", name: "Geometric Langlands", name_zh: "几何朗兰兹对应", wiki: "Geometric Langlands correspondence" },
    { type: "resource", name: "Perfectoid space", name_zh: "完美空间", wiki: "Perfectoid space" },
  ],
  "beyond-zfc-foundations": [
    { type: "resource", name: "Zermelo–Fraenkel set theory", name_zh: "策梅洛-弗兰克尔集合论", wiki: "Zermelo–Fraenkel set theory" },
    { type: "resource", name: "Constructive set theory", name_zh: "构造性集合论", wiki: "Constructive set theory" },
    { type: "resource", name: "New Foundations", name_zh: "新基础", wiki: "New Foundations" },
    { type: "resource", name: "Tarski–Grothendieck set theory", name_zh: "塔斯基-格罗滕迪克集合论", wiki: "Tarski–Grothendieck set theory" },
    { type: "person", name: "Saharon Shelah", name_zh: "萨哈龙·谢拉", wiki: "Saharon Shelah" },
  ],
  "continuum-hypothesis-resolution": [
    { type: "resource", name: "Continuum hypothesis", name_zh: "连续统假设", wiki: "Continuum hypothesis" },
    { type: "person", name: "Kurt Gödel", name_zh: "库尔特·哥德尔", wiki: "Kurt Gödel" },
    { type: "person", name: "Paul Cohen", name_zh: "保罗·科恩", wiki: "Paul Cohen" },
    { type: "resource", name: "Forcing", name_zh: "力迫法", wiki: "Forcing (mathematics)" },
    { type: "resource", name: "Martin's Maximum", name_zh: "马丁极大原理", wiki: "Martin's maximum" },
    { type: "resource", name: "Large cardinal", name_zh: "大基数", wiki: "Large cardinal" },
  ],
  "hypercomputation": [
    { type: "resource", name: "Hypercomputation", name_zh: "超计算", wiki: "Hypercomputation" },
    { type: "resource", name: "Oracle machine", name_zh: "神谕机器", wiki: "Oracle machine" },
    { type: "resource", name: "Zeno machine", name_zh: "芝诺机", wiki: "Zeno machine" },
    { type: "resource", name: "Malament–Hogarth spacetime", name_zh: "马拉门-霍加思时空", wiki: "Malament–Hogarth spacetime" },
    { type: "resource", name: "Halting problem", name_zh: "停机问题", wiki: "Halting problem" },
  ],
  "trans-computable-mathematics": [
    { type: "resource", name: "Busy beaver function", name_zh: "繁忙的海狸函数", wiki: "Busy beaver" },
    { type: "resource", name: "Chaitin's constant", name_zh: "蔡廷常数", wiki: "Chaitin's constant" },
    { type: "resource", name: "Arithmetical hierarchy", name_zh: "算术层次", wiki: "Arithmetical hierarchy" },
    { type: "resource", name: "Constructible universe", name_zh: "可构造宇宙", wiki: "Constructible universe" },
  ],

  // ─── Superintelligence downstream ───
  "whole-brain-emulation": [
    { type: "person", name: "Anders Sandberg", name_zh: "安德斯·桑德伯格", wiki: "Anders Sandberg" },
    { type: "person", name: "Henry Markram", name_zh: "亨利·马克拉姆", wiki: "Henry Markram" },
    { type: "resource", name: "Connectome", name_zh: "连接组", wiki: "Connectome" },
    { type: "resource", name: "Connectomics", name_zh: "连接组学", wiki: "Connectomics" },
    { type: "org", name: "Blue Brain Project", name_zh: "蓝脑计划", wiki: "Blue Brain Project" },
    { type: "org", name: "OpenWorm", name_zh: "OpenWorm 项目", wiki: "OpenWorm" },
    { type: "work", name: "Whole Brain Emulation Roadmap", name_zh: "《全脑仿真路线图》", wiki: false },
  ],
  "knowledge-closure": [
    { type: "work", name: "The End of Science", name_zh: "《科学的终结》", wiki: "The End of Science" },
    { type: "person", name: "John Horgan", name_zh: "约翰·霍根", wiki: "John Horgan (journalist)" },
    { type: "resource", name: "Theory of everything", name_zh: "万物理论", wiki: "Theory of everything" },
    { type: "resource", name: "Knowledge graph", name_zh: "知识图谱", wiki: "Knowledge graph" },
  ],
  "subjective-time-compression": [
    { type: "person", name: "Robin Hanson", name_zh: "罗宾·汉森", wiki: "Robin Hanson" },
    { type: "work", name: "The Age of Em", name_zh: "《时代之我》", wiki: "The Age of Em" },
    { type: "resource", name: "Time perception", name_zh: "时间知觉", wiki: "Time perception" },
    { type: "resource", name: "Em (Hanson)", name_zh: "Em (汉森意义上)", wiki: false },
    { type: "resource", name: "Substrate clock-rate", name_zh: "基质时钟速率", wiki: false },
  ],

  // ─── Warfare doctrine & tactics ───
  "phalanx": [
    { type: "unit", name: "Greek hoplite", name_zh: "希腊重装步兵", wiki: "Hoplite" },
    { type: "unit", name: "Macedonian phalanx", name_zh: "马其顿方阵", wiki: "Macedonian phalanx" },
    { type: "resource", name: "Sarissa", name_zh: "萨里沙长矛", wiki: "Sarissa" },
    { type: "work", name: "Battle of Plataea", name_zh: "普拉提亚战役", wiki: "Battle of Plataea" },
  ],
  "roman-legion": [
    { type: "unit", name: "Marian Legion", name_zh: "马略改革后的军团", wiki: "Marian reforms" },
    { type: "unit", name: "Centurion", name_zh: "百夫长", wiki: "Centurion" },
    { type: "resource", name: "Gladius", name_zh: "短剑", wiki: "Gladius" },
    { type: "resource", name: "Pilum", name_zh: "投枪", wiki: "Pilum" },
    { type: "resource", name: "Testudo formation", name_zh: "龟甲阵", wiki: "Testudo formation" },
  ],
  "castle-siege-doctrine": [
    { type: "wonder", name: "Krak des Chevaliers", name_zh: "骑士堡", wiki: "Krak des Chevaliers" },
    { type: "wonder", name: "Caernarfon Castle", name_zh: "卡那封城堡", wiki: "Caernarfon Castle" },
    { type: "unit", name: "Trebuchet", name_zh: "投石机", wiki: "Trebuchet" },
    { type: "unit", name: "Siege tower", name_zh: "攻城塔", wiki: "Siege tower" },
    { type: "resource", name: "Concentric castle design", name_zh: "同心圆式城堡设计", wiki: "Concentric castle" },
  ],
  "pike-square": [
    { type: "unit", name: "Swiss pikemen", name_zh: "瑞士长矛兵", wiki: "Swiss mercenaries" },
    { type: "unit", name: "Landsknecht", name_zh: "德意志雇佣兵", wiki: "Landsknecht" },
    { type: "unit", name: "Spanish tercio", name_zh: "西班牙方阵", wiki: "Tercio" },
    { type: "work", name: "Battle of Nancy", name_zh: "南锡战役", wiki: "Battle of Nancy" },
  ],
  "trench-warfare": [
    { type: "work", name: "Battle of the Somme", name_zh: "索姆河战役", wiki: "Battle of the Somme" },
    { type: "work", name: "Battle of Verdun", name_zh: "凡尔登战役", wiki: "Battle of Verdun" },
    { type: "resource", name: "Barbed wire", name_zh: "带刺铁丝网", wiki: "Barbed wire" },
    { type: "unit", name: "Maxim machine gun nest", name_zh: "马克沁机枪阵地", wiki: "Maxim gun" },
    { type: "resource", name: "Stormtrooper tactics", name_zh: "暴风突击队战术", wiki: "Stormtrooper" },
  ],
  "combined-arms-warfare": [
    { type: "person", name: "John Monash", name_zh: "约翰·莫纳什", wiki: "John Monash" },
    { type: "person", name: "Ferdinand Foch", name_zh: "费迪南·福煦", wiki: "Ferdinand Foch" },
    { type: "person", name: "J.F.C. Fuller", name_zh: "J.F.C. 富勒", wiki: "J. F. C. Fuller" },
    { type: "work", name: "Hundred Days Offensive", name_zh: "百日攻势", wiki: "Hundred Days Offensive" },
    { type: "work", name: "Plan 1919", name_zh: "1919 年计划", wiki: "Plan 1919" },
  ],
  "blitzkrieg": [
    { type: "person", name: "Heinz Guderian", name_zh: "海因茨·古德里安", wiki: "Heinz Guderian" },
    { type: "person", name: "Mikhail Tukhachevsky", name_zh: "米哈伊尔·图哈切夫斯基", wiki: "Mikhail Tukhachevsky" },
    { type: "work", name: "Achtung—Panzer!", name_zh: "《注意—坦克!》", wiki: "Achtung – Panzer!" },
    { type: "work", name: "Battle of France", name_zh: "法国战役", wiki: "Battle of France" },
    { type: "resource", name: "Schwerpunkt", name_zh: "重点突破", wiki: "Schwerpunkt" },
    { type: "resource", name: "Deep battle", name_zh: "大纵深作战", wiki: "Deep operation" },
  ],
  "ballistic-missile-defense": [
    { type: "unit", name: "Safeguard Program", name_zh: "保障计划", wiki: "Safeguard Program" },
    { type: "unit", name: "Strategic Defense Initiative", name_zh: "战略防御计划", wiki: "Strategic Defense Initiative" },
    { type: "unit", name: "Aegis Combat System", name_zh: "宙斯盾作战系统", wiki: "Aegis Combat System" },
    { type: "unit", name: "THAAD", name_zh: "末段高空区域防御系统", wiki: "Terminal High Altitude Area Defense" },
    { type: "work", name: "Anti-Ballistic Missile Treaty", name_zh: "《反弹道导弹条约》", wiki: "Anti-Ballistic Missile Treaty" },
  ],
  "stealth-aircraft-doctrine": [
    { type: "unit", name: "F-117 Nighthawk", name_zh: "F-117 夜鹰", wiki: "Lockheed F-117 Nighthawk" },
    { type: "unit", name: "B-2 Spirit", name_zh: "B-2 幽灵", wiki: "Northrop Grumman B-2 Spirit" },
    { type: "unit", name: "F-22 Raptor", name_zh: "F-22 猛禽", wiki: "Lockheed Martin F-22 Raptor" },
    { type: "unit", name: "F-35 Lightning II", name_zh: "F-35 闪电 II", wiki: "Lockheed Martin F-35 Lightning II" },
    { type: "unit", name: "Chengdu J-20", name_zh: "成都歼-20", wiki: "Chengdu J-20" },
    { type: "resource", name: "Radar-absorbent material", name_zh: "雷达吸波材料", wiki: "Radar-absorbent material" },
  ],
  "network-centric-warfare": [
    { type: "person", name: "Arthur Cebrowski", name_zh: "阿瑟·切布罗夫斯基", wiki: "Arthur K. Cebrowski" },
    { type: "resource", name: "Common operational picture", name_zh: "共同作战图景", wiki: "Common operational picture" },
    { type: "resource", name: "JADC2", name_zh: "联合全域指挥控制", wiki: "Joint All-Domain Command and Control" },
    { type: "resource", name: "Sensor-shooter loop", name_zh: "传感器-射手回路", wiki: false },
  ],
  "layered-air-missile-defense": [
    { type: "unit", name: "Iron Dome", name_zh: "铁穹", wiki: "Iron Dome" },
    { type: "unit", name: "Patriot missile", name_zh: "爱国者导弹", wiki: "MIM-104 Patriot" },
    { type: "unit", name: "Arrow 3", name_zh: "箭-3 反导拦截弹", wiki: "Arrow 3" },
    { type: "unit", name: "SM-3 interceptor", name_zh: "SM-3 拦截弹", wiki: "RIM-161 Standard Missile 3" },
    { type: "resource", name: "Multi-tier intercept", name_zh: "多层拦截", wiki: false },
  ],
  "ai-decision-loop-compression": [
    { type: "person", name: "John Boyd", name_zh: "约翰·博伊德", wiki: "John Boyd (military strategist)" },
    { type: "resource", name: "OODA loop", name_zh: "OODA 循环", wiki: "OODA loop" },
    { type: "resource", name: "Lethal autonomous weapon", name_zh: "致命自主武器", wiki: "Lethal autonomous weapon" },
    { type: "work", name: "Stop Killer Robots campaign", name_zh: "禁止杀人机器人运动", wiki: "Campaign to Stop Killer Robots" },
  ],

  // ─── Shelter & architecture (gap fill) ───
  "mammoth-bone-hut": [
    { type: "wonder", name: "Mezhirich", name_zh: "梅日里奇遗址", wiki: "Mezhirich" },
    { type: "wonder", name: "Dolní Věstonice", name_zh: "下维斯特尼采", wiki: "Dolní Věstonice" },
    { type: "resource", name: "Mammoth-bone framework", name_zh: "猛犸骨架", wiki: false },
    { type: "unit", name: "Gravettian camp", name_zh: "格拉维特文化营地", wiki: "Gravettian" },
  ],
  "roman-insula": [
    { type: "unit", name: "Insula", name_zh: "罗马公寓 (insula)", wiki: "Insula (building)" },
    { type: "unit", name: "Domus", name_zh: "罗马宅邸 (domus)", wiki: "Domus" },
    { type: "wonder", name: "Ostia Antica", name_zh: "奥斯蒂亚古城", wiki: "Ostia Antica" },
    { type: "resource", name: "Opus latericium", name_zh: "罗马混凝土砖工", wiki: "Opus latericium" },
  ],
  "renaissance-dome": [
    { type: "person", name: "Filippo Brunelleschi", name_zh: "菲利波·布鲁内莱斯基", wiki: "Filippo Brunelleschi" },
    { type: "person", name: "Andrea Palladio", name_zh: "安德烈亚·帕拉第奥", wiki: "Andrea Palladio" },
    { type: "person", name: "Leon Battista Alberti", name_zh: "莱昂·巴蒂斯塔·阿尔伯蒂", wiki: "Leon Battista Alberti" },
    { type: "wonder", name: "Florence Cathedral", name_zh: "佛罗伦萨大教堂", wiki: "Florence Cathedral" },
    { type: "wonder", name: "St. Peter's Basilica", name_zh: "圣彼得大教堂", wiki: "St. Peter's Basilica" },
    { type: "work", name: "De re aedificatoria", name_zh: "《论建筑》", wiki: "De re aedificatoria" },
  ],
  "iron-frame-construction": [
    { type: "person", name: "Abraham Darby III", name_zh: "亚伯拉罕·达比三世", wiki: "Abraham Darby III" },
    { type: "person", name: "Joseph Paxton", name_zh: "约瑟夫·帕克斯顿", wiki: "Joseph Paxton" },
    { type: "wonder", name: "The Iron Bridge", name_zh: "铁桥", wiki: "The Iron Bridge" },
    { type: "wonder", name: "Crystal Palace", name_zh: "水晶宫", wiki: "The Crystal Palace" },
    { type: "wonder", name: "Eiffel Tower", name_zh: "埃菲尔铁塔", wiki: "Eiffel Tower" },
  ],
  "reinforced-concrete": [
    { type: "person", name: "Joseph Monier", name_zh: "约瑟夫·莫尼耶", wiki: "Joseph Monier" },
    { type: "person", name: "François Hennebique", name_zh: "弗朗索瓦·埃内比克", wiki: "François Hennebique" },
    { type: "person", name: "Auguste Perret", name_zh: "奥古斯特·佩雷", wiki: "Auguste Perret" },
    { type: "wonder", name: "Fallingwater", name_zh: "流水别墅", wiki: "Fallingwater" },
    { type: "resource", name: "Hennebique system", name_zh: "埃内比克体系", wiki: "Hennebique construction company" },
  ],
  "suburban-tract-housing": [
    { type: "wonder", name: "Levittown", name_zh: "莱维敦", wiki: "Levittown, New York" },
    { type: "person", name: "William Levitt", name_zh: "威廉·莱维特", wiki: "William Levitt" },
    { type: "org", name: "Federal Housing Administration", name_zh: "美国联邦住房管理局", wiki: "Federal Housing Administration" },
    { type: "work", name: "GI Bill", name_zh: "《退伍军人权利法案》", wiki: "G.I. Bill" },
    { type: "resource", name: "Single-family zoning", name_zh: "单户住宅分区", wiki: "Single-family zoning" },
  ],
  "parametric-architecture": [
    { type: "person", name: "Zaha Hadid", name_zh: "扎哈·哈迪德", wiki: "Zaha Hadid" },
    { type: "person", name: "Frank Gehry", name_zh: "弗兰克·盖里", wiki: "Frank Gehry" },
    { type: "wonder", name: "Walt Disney Concert Hall", name_zh: "沃尔特·迪士尼音乐厅", wiki: "Walt Disney Concert Hall" },
    { type: "wonder", name: "Heydar Aliyev Center", name_zh: "海达尔·阿利耶夫中心", wiki: "Heydar Aliyev Center" },
    { type: "unit", name: "Grasshopper 3D", name_zh: "Grasshopper 参数化设计", wiki: "Grasshopper 3D" },
    { type: "resource", name: "Building information modeling", name_zh: "建筑信息模型", wiki: "Building information modeling" },
  ],
  "smart-building": [
    { type: "wonder", name: "The Edge (Amsterdam)", name_zh: "Edge 大楼 (阿姆斯特丹)", wiki: "The Edge (building)" },
    { type: "resource", name: "Building management system", name_zh: "建筑管理系统", wiki: "Building management system" },
    { type: "resource", name: "BREEAM", name_zh: "BREEAM 评估体系", wiki: "BREEAM" },
    { type: "resource", name: "Internet of things", name_zh: "物联网", wiki: "Internet of things" },
  ],

  // ─── Subsistence & agriculture (gap fill) ───
  "food-preservation": [
    { type: "resource", name: "Smoking", name_zh: "烟熏", wiki: "Smoking (cooking)" },
    { type: "resource", name: "Drying", name_zh: "干燥", wiki: "Drying" },
    { type: "resource", name: "Fermentation in food processing", name_zh: "食品发酵", wiki: "Fermentation in food processing" },
    { type: "resource", name: "Pemmican", name_zh: "肉干 (pemmican)", wiki: "Pemmican" },
  ],
  "beekeeping": [
    { type: "resource", name: "Apis mellifera", name_zh: "西方蜜蜂", wiki: "Western honey bee" },
    { type: "resource", name: "Honey", name_zh: "蜂蜜", wiki: "Honey" },
    { type: "resource", name: "Beeswax", name_zh: "蜂蜡", wiki: "Beeswax" },
    { type: "resource", name: "Mead", name_zh: "蜂蜜酒", wiki: "Mead" },
    { type: "wonder", name: "Egyptian apiary", name_zh: "古埃及蜂房", wiki: "Beekeeping" },
  ],
  "cheese-dairy-processing": [
    { type: "resource", name: "Rennet", name_zh: "凝乳酶", wiki: "Rennet" },
    { type: "resource", name: "Cheese", name_zh: "奶酪", wiki: "Cheese" },
    { type: "resource", name: "Yogurt", name_zh: "酸奶", wiki: "Yogurt" },
    { type: "resource", name: "Butter", name_zh: "黄油", wiki: "Butter" },
    { type: "resource", name: "Lactase persistence", name_zh: "乳糖酶持久性", wiki: "Lactase persistence" },
  ],
  "salt-production": [
    { type: "wonder", name: "Hallstatt salt mine", name_zh: "哈尔施塔特盐矿", wiki: "Hallstatt" },
    { type: "resource", name: "Salt evaporation pond", name_zh: "盐田", wiki: "Salt evaporation pond" },
    { type: "resource", name: "Salt cod", name_zh: "盐渍鳕鱼", wiki: "Salt cod" },
    { type: "work", name: "Gabelle (salt tax)", name_zh: "盐税 (gabelle)", wiki: "Gabelle" },
  ],
  "latifundia": [
    { type: "work", name: "De Agricultura (Cato)", name_zh: "《论农业》(老加图)", wiki: "De agri cultura" },
    { type: "work", name: "Rerum Rusticarum (Varro)", name_zh: "《论农事》(瓦罗)", wiki: "Marcus Terentius Varro" },
    { type: "resource", name: "Roman grain trade", name_zh: "罗马粮食贸易", wiki: "Cura Annonae" },
    { type: "unit", name: "Slave-worked estate", name_zh: "奴隶庄园", wiki: "Slavery in ancient Rome" },
  ],
  "sugar-plantation": [
    { type: "resource", name: "Sugarcane", name_zh: "甘蔗", wiki: "Sugarcane" },
    { type: "wonder", name: "Saint-Domingue", name_zh: "圣多明各", wiki: "Saint-Domingue" },
    { type: "resource", name: "Triangular trade", name_zh: "三角贸易", wiki: "Triangular trade" },
    { type: "org", name: "Royal African Company", name_zh: "皇家非洲公司", wiki: "Royal African Company" },
  ],
  "canning": [
    { type: "person", name: "Nicolas Appert", name_zh: "尼古拉·阿佩尔", wiki: "Nicolas Appert" },
    { type: "person", name: "Bryan Donkin", name_zh: "布莱恩·东金", wiki: "Bryan Donkin" },
    { type: "resource", name: "Tin can", name_zh: "马口铁罐", wiki: "Tin can" },
    { type: "resource", name: "Mason jar", name_zh: "梅森罐", wiki: "Mason jar" },
  ],
  "mechanical-reaper": [
    { type: "person", name: "Cyrus McCormick", name_zh: "塞勒斯·麦考密克", wiki: "Cyrus McCormick" },
    { type: "unit", name: "McCormick Reaper", name_zh: "麦考密克收割机", wiki: "Mechanical reaper" },
    { type: "unit", name: "Combine harvester", name_zh: "联合收割机", wiki: "Combine harvester" },
    { type: "org", name: "International Harvester", name_zh: "万国收割机公司", wiki: "International Harvester" },
  ],
  "pasteurization": [
    { type: "person", name: "Louis Pasteur", name_zh: "路易·巴斯德", wiki: "Louis Pasteur" },
    { type: "resource", name: "UHT processing", name_zh: "超高温灭菌", wiki: "Ultra-high-temperature processing" },
    { type: "resource", name: "HTST process", name_zh: "高温短时灭菌", wiki: "Pasteurization" },
    { type: "work", name: "Compulsory pasteurization", name_zh: "强制巴氏消毒法", wiki: "Pasteurization" },
  ],
  "refrigerated-transport": [
    { type: "person", name: "Gustavus Swift", name_zh: "古斯塔夫斯·斯威夫特", wiki: "Gustavus Franklin Swift" },
    { type: "unit", name: "Refrigerator car", name_zh: "冷藏车", wiki: "Refrigerator car" },
    { type: "unit", name: "SS Strathleven", name_zh: "SS 斯特拉斯利文号", wiki: "SS Strathleven" },
    { type: "resource", name: "Cold chain", name_zh: "冷链", wiki: "Cold chain" },
  ],
  "tractor": [
    { type: "unit", name: "Fordson Model F", name_zh: "福特森 F 型拖拉机", wiki: "Fordson" },
    { type: "unit", name: "John Deere Model D", name_zh: "约翰迪尔 D 型", wiki: "John Deere" },
    { type: "org", name: "Caterpillar Inc.", name_zh: "卡特彼勒公司", wiki: "Caterpillar Inc." },
    { type: "resource", name: "Power take-off", name_zh: "动力输出装置", wiki: "Power take-off" },
  ],
  "synthetic-pesticides": [
    { type: "person", name: "Paul Hermann Müller", name_zh: "保罗·赫尔曼·穆勒", wiki: "Paul Hermann Müller" },
    { type: "resource", name: "DDT", name_zh: "DDT", wiki: "DDT" },
    { type: "resource", name: "Glyphosate", name_zh: "草甘膦", wiki: "Glyphosate" },
    { type: "resource", name: "Neonicotinoid", name_zh: "新烟碱类杀虫剂", wiki: "Neonicotinoid" },
    { type: "work", name: "Silent Spring", name_zh: "《寂静的春天》", wiki: "Silent Spring" },
    { type: "work", name: "Stockholm Convention", name_zh: "《斯德哥尔摩公约》", wiki: "Stockholm Convention on Persistent Organic Pollutants" },
  ],
  "industrial-aquaculture": [
    { type: "resource", name: "Atlantic salmon farming", name_zh: "大西洋鲑养殖", wiki: "Salmon as food" },
    { type: "resource", name: "Shrimp farming", name_zh: "对虾养殖", wiki: "Shrimp farming" },
    { type: "resource", name: "Recirculating aquaculture system", name_zh: "循环水养殖", wiki: "Recirculating aquaculture system" },
    { type: "org", name: "Mowi (formerly Marine Harvest)", name_zh: "美威公司", wiki: "Mowi" },
  ],
  "frozen-food-supply-chain": [
    { type: "person", name: "Clarence Birdseye", name_zh: "克拉伦斯·伯兹艾", wiki: "Clarence Birdseye" },
    { type: "org", name: "Birds Eye", name_zh: "Birds Eye 鸟眼食品", wiki: "Birds Eye" },
    { type: "unit", name: "TV dinner", name_zh: "电视餐", wiki: "TV dinner" },
    { type: "resource", name: "Flash freezing", name_zh: "快速冷冻", wiki: "Flash freezing" },
  ],
  "gmo": [
    { type: "unit", name: "FlavrSavr tomato", name_zh: "FlavrSavr 番茄", wiki: "FlavrSavr" },
    { type: "unit", name: "Roundup Ready soybean", name_zh: "抗草甘膦大豆", wiki: "Roundup Ready" },
    { type: "unit", name: "Bt corn", name_zh: "Bt 玉米", wiki: "Bt corn" },
    { type: "org", name: "Monsanto", name_zh: "孟山都公司", wiki: "Monsanto" },
    { type: "resource", name: "CRISPR-edited crop", name_zh: "CRISPR 编辑作物", wiki: "Genome editing" },
  ],
  "vertical-farming": [
    { type: "person", name: "Dickson Despommier", name_zh: "迪克森·德斯波米耶", wiki: "Dickson Despommier" },
    { type: "work", name: "The Vertical Farm", name_zh: "《垂直农场》", wiki: "Vertical farming" },
    { type: "org", name: "AeroFarms", name_zh: "AeroFarms 空中农场", wiki: "AeroFarms" },
    { type: "org", name: "Plenty (company)", name_zh: "Plenty 农业公司", wiki: "Plenty (company)" },
    { type: "resource", name: "Aeroponics", name_zh: "气培", wiki: "Aeroponics" },
  ],

  // ─── Post-WWI weapons platforms ───
  "assault-rifle": [
    { type: "unit", name: "StG 44", name_zh: "StG 44 突击步枪", wiki: "StG 44" },
    { type: "unit", name: "AK-47", name_zh: "AK-47 突击步枪", wiki: "AK-47" },
    { type: "unit", name: "M16 rifle", name_zh: "M16 步枪", wiki: "M16 rifle" },
    { type: "person", name: "Mikhail Kalashnikov", name_zh: "米哈伊尔·卡拉什尼科夫", wiki: "Mikhail Kalashnikov" },
    { type: "person", name: "Hugo Schmeisser", name_zh: "雨果·施迈瑟", wiki: "Hugo Schmeisser" },
    { type: "resource", name: "Intermediate cartridge", name_zh: "中间型弹药", wiki: "Intermediate cartridge" },
  ],
  "guided-missile-destroyer": [
    { type: "unit", name: "Arleigh Burke-class destroyer", name_zh: "阿利·伯克级驱逐舰", wiki: "Arleigh Burke-class destroyer" },
    { type: "unit", name: "USS Charles F. Adams", name_zh: "查尔斯·F·亚当斯号", wiki: "USS Charles F. Adams (DDG-2)" },
    { type: "unit", name: "Type 052D destroyer", name_zh: "052D 型驱逐舰", wiki: "Type 052D destroyer" },
    { type: "unit", name: "Aegis Combat System", name_zh: "宙斯盾作战系统", wiki: "Aegis Combat System" },
    { type: "resource", name: "Tomahawk missile", name_zh: "战斧巡航导弹", wiki: "Tomahawk (missile)" },
  ],

  // ─── Air defense + military support ───
  "military-logistics": [
    { type: "person", name: "Helmuth von Moltke the Elder", name_zh: "老毛奇", wiki: "Helmuth von Moltke the Elder" },
    { type: "org", name: "German General Staff", name_zh: "德国总参谋部", wiki: "German General Staff" },
    { type: "work", name: "Berlin Airlift", name_zh: "柏林空运", wiki: "Berlin Blockade" },
    { type: "unit", name: "Red Ball Express", name_zh: "红球快运", wiki: "Red Ball Express" },
  ],
  "anti-aircraft-artillery": [
    { type: "unit", name: "8.8 cm FlaK 36", name_zh: "88 毫米高射炮", wiki: "8.8 cm Flak 18/36/37/41" },
    { type: "unit", name: "Bofors 40 mm", name_zh: "博福斯 40 毫米炮", wiki: "Bofors 40 mm gun" },
    { type: "unit", name: "Phalanx CIWS", name_zh: "密集阵近防系统", wiki: "Phalanx CIWS" },
    { type: "resource", name: "Proximity fuze", name_zh: "近炸引信", wiki: "Proximity fuze" },
  ],
  "combat-medic": [
    { type: "unit", name: "Mobile Army Surgical Hospital", name_zh: "流动军外科医院", wiki: "Mobile army surgical hospital" },
    { type: "unit", name: "Bell UH-1 Iroquois", name_zh: "贝尔 UH-1 直升机", wiki: "Bell UH-1 Iroquois" },
    { type: "resource", name: "Tactical Combat Casualty Care", name_zh: "战术伤员救护", wiki: "Tactical Combat Casualty Care" },
    { type: "resource", name: "Tourniquet", name_zh: "止血带", wiki: "Tourniquet" },
    { type: "resource", name: "Golden hour", name_zh: "黄金救援时间", wiki: "Golden hour (medicine)" },
  ],
  "spy-satellite": [
    { type: "unit", name: "KH-1 Corona", name_zh: "KH-1 科罗娜", wiki: "Corona (satellite)" },
    { type: "unit", name: "KH-11 Kennen", name_zh: "KH-11 凯南", wiki: "KH-11 KENNEN" },
    { type: "unit", name: "Zenit (satellite)", name_zh: "天顶号侦察卫星", wiki: "Zenit (satellite)" },
    { type: "org", name: "National Reconnaissance Office", name_zh: "美国国家侦察局", wiki: "National Reconnaissance Office" },
    { type: "resource", name: "Synthetic-aperture radar", name_zh: "合成孔径雷达", wiki: "Synthetic-aperture radar" },
  ],
  "awacs": [
    { type: "unit", name: "Boeing E-3 Sentry", name_zh: "波音 E-3 哨兵", wiki: "Boeing E-3 Sentry" },
    { type: "unit", name: "Beriev A-50", name_zh: "别里耶夫 A-50", wiki: "Beriev A-50" },
    { type: "unit", name: "KJ-2000", name_zh: "空警-2000", wiki: "KJ-2000" },
    { type: "unit", name: "Lockheed EC-121 Warning Star", name_zh: "EC-121 预警星", wiki: "Lockheed EC-121 Warning Star" },
    { type: "resource", name: "Rotodome", name_zh: "圆盘形雷达罩", wiki: "Rotodome" },
  ],
  "iads": [
    { type: "unit", name: "S-400 missile system", name_zh: "S-400 防空导弹系统", wiki: "S-400 missile system" },
    { type: "unit", name: "Patriot missile", name_zh: "爱国者导弹", wiki: "MIM-104 Patriot" },
    { type: "unit", name: "HQ-9 missile system", name_zh: "红旗-9 防空导弹", wiki: "HQ-9" },
    { type: "org", name: "PVO Strany", name_zh: "苏联国土防空军", wiki: "Soviet Air Defence Forces" },
    { type: "resource", name: "Suppression of Enemy Air Defenses", name_zh: "压制敌防空体系", wiki: "Suppression of Enemy Air Defenses" },
  ],

  // ─── Misc additions ───
  "cell-theory": [
    { type: "person", name: "Matthias Schleiden", name_zh: "马蒂亚斯·施莱登", wiki: "Matthias Jakob Schleiden" },
    { type: "person", name: "Theodor Schwann", name_zh: "泰奥多尔·施旺", wiki: "Theodor Schwann" },
    { type: "person", name: "Rudolf Virchow", name_zh: "鲁道夫·菲尔绍", wiki: "Rudolf Virchow" },
    { type: "resource", name: "Cell (biology)", name_zh: "细胞", wiki: "Cell (biology)" },
    { type: "resource", name: "Mitosis", name_zh: "有丝分裂", wiki: "Mitosis" },
  ],
  "modern-olympics": [
    { type: "person", name: "Pierre de Coubertin", name_zh: "皮埃尔·德·顾拜旦", wiki: "Pierre de Coubertin" },
    { type: "org", name: "International Olympic Committee", name_zh: "国际奥林匹克委员会", wiki: "International Olympic Committee" },
    { type: "work", name: "Athens 1896", name_zh: "1896 年雅典奥运会", wiki: "1896 Summer Olympics" },
    { type: "work", name: "Olympic Charter", name_zh: "《奥林匹克宪章》", wiki: "Olympic Charter" },
  ],
  "civil-aviation": [
    { type: "unit", name: "Douglas DC-3", name_zh: "道格拉斯 DC-3", wiki: "Douglas DC-3" },
    { type: "unit", name: "Boeing 707", name_zh: "波音 707", wiki: "Boeing 707" },
    { type: "unit", name: "Boeing 747", name_zh: "波音 747", wiki: "Boeing 747" },
    { type: "org", name: "KLM", name_zh: "荷兰皇家航空", wiki: "KLM" },
    { type: "org", name: "Pan American World Airways", name_zh: "泛美航空", wiki: "Pan American World Airways" },
    { type: "org", name: "International Civil Aviation Organization", name_zh: "国际民用航空组织", wiki: "International Civil Aviation Organization" },
  ],
  "mobile-internet": [
    { type: "unit", name: "i-mode", name_zh: "i-mode 移动数据服务", wiki: "I-mode" },
    { type: "resource", name: "Wireless Application Protocol", name_zh: "无线应用协议", wiki: "Wireless Application Protocol" },
    { type: "resource", name: "3G", name_zh: "第三代移动通信", wiki: "3G" },
    { type: "unit", name: "iPhone (1st generation)", name_zh: "初代 iPhone", wiki: "IPhone (1st generation)" },
    { type: "unit", name: "Android (operating system)", name_zh: "安卓系统", wiki: "Android (operating system)" },
  ],

  // ─── Realistic Near / Far Future ───
  "engineered-microbiome": [
    { type: "resource", name: "Fecal microbiota transplant", name_zh: "粪便微生物群移植", wiki: "Fecal microbiota transplant" },
    { type: "resource", name: "Human microbiome", name_zh: "人类微生物组", wiki: "Human microbiome" },
    { type: "org", name: "Seres Therapeutics", name_zh: "Seres Therapeutics 公司", wiki: "Seres Therapeutics" },
    { type: "resource", name: "Gut-brain axis", name_zh: "肠脑轴", wiki: "Gut–brain axis" },
  ],
  "geothermal-drilling": [
    { type: "org", name: "Quaise Energy", name_zh: "Quaise 能源公司", wiki: false },
    { type: "resource", name: "Enhanced geothermal system", name_zh: "增强型地热系统", wiki: "Enhanced geothermal system" },
    { type: "resource", name: "Gyrotron drill", name_zh: "回旋管钻机", wiki: "Gyrotron" },
    { type: "unit", name: "Eavor-Loop", name_zh: "Eavor 闭环系统", wiki: false },
  ],
  "senolytic-longevity-therapy": [
    { type: "person", name: "David Sinclair", name_zh: "大卫·辛克莱尔", wiki: "David A. Sinclair" },
    { type: "person", name: "Aubrey de Grey", name_zh: "奥布里·德格雷", wiki: "Aubrey de Grey" },
    { type: "resource", name: "Senolytic", name_zh: "衰老细胞清除剂", wiki: "Senolytic" },
    { type: "resource", name: "Cellular senescence", name_zh: "细胞衰老", wiki: "Cellular senescence" },
    { type: "resource", name: "Yamanaka factors", name_zh: "山中因子", wiki: "Induced pluripotent stem cell" },
    { type: "org", name: "Unity Biotechnology", name_zh: "Unity 生物技术", wiki: "Unity Biotechnology" },
  ],
  "brain-brain-communication": [
    { type: "person", name: "Miguel Nicolelis", name_zh: "米格尔·尼科勒利斯", wiki: "Miguel Nicolelis" },
    { type: "resource", name: "Brain-to-brain interface", name_zh: "脑-脑接口", wiki: "Brain-to-brain interface" },
    { type: "unit", name: "Brainet", name_zh: "脑联网", wiki: false },
    { type: "org", name: "Neuralink", name_zh: "Neuralink 神经链接", wiki: "Neuralink" },
  ],
  "theory-of-consciousness": [
    { type: "person", name: "Giulio Tononi", name_zh: "朱利奥·托诺尼", wiki: "Giulio Tononi" },
    { type: "person", name: "Christof Koch", name_zh: "克里斯托夫·科赫", wiki: "Christof Koch" },
    { type: "person", name: "David Chalmers", name_zh: "大卫·查尔默斯", wiki: "David Chalmers" },
    { type: "resource", name: "Integrated information theory", name_zh: "整合信息论", wiki: "Integrated information theory" },
    { type: "resource", name: "Global workspace theory", name_zh: "全局工作空间理论", wiki: "Global workspace theory" },
    { type: "resource", name: "Hard problem of consciousness", name_zh: "意识难题", wiki: "Hard problem of consciousness" },
  ],
  "asteroid-capture": [
    { type: "unit", name: "Asteroid Redirect Mission", name_zh: "小行星重定向任务", wiki: "Asteroid Redirect Mission" },
    { type: "resource", name: "Gravity tractor", name_zh: "引力拖船", wiki: "Gravity tractor" },
    { type: "resource", name: "Lagrange point", name_zh: "拉格朗日点", wiki: "Lagrange point" },
    { type: "unit", name: "Distant retrograde orbit", name_zh: "远逆行轨道", wiki: "Distant retrograde orbit" },
  ],
  "bose-einstein-engineering": [
    { type: "person", name: "Eric Cornell", name_zh: "埃里克·康奈尔", wiki: "Eric Allin Cornell" },
    { type: "person", name: "Carl Wieman", name_zh: "卡尔·威曼", wiki: "Carl Wieman" },
    { type: "resource", name: "Bose–Einstein condensate", name_zh: "玻色-爱因斯坦凝聚态", wiki: "Bose–Einstein condensate" },
    { type: "resource", name: "Atom laser", name_zh: "原子激光", wiki: "Atom laser" },
    { type: "resource", name: "Superfluid", name_zh: "超流体", wiki: "Superfluid" },
  ],
  "anti-senescence-cellular-substrate": [
    { type: "resource", name: "Cellular senescence", name_zh: "细胞衰老", wiki: "Cellular senescence" },
    { type: "resource", name: "Theseus's ship paradox", name_zh: "忒修斯之船悖论", wiki: "Ship of Theseus" },
    { type: "unit", name: "Hybrid bio-synthetic cell", name_zh: "混合生物-合成细胞", wiki: false },
    { type: "resource", name: "Molecular nanomedicine", name_zh: "分子纳米医学", wiki: "Nanomedicine" },
  ],
};
