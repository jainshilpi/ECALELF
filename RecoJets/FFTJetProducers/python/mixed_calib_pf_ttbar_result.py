# Generated Tue Jul 05 01:58:24 PM CDT 2011 by user igv with script generate_pileup_calibration.tcl
import FWCore.ParameterSet.Config as cms

uncertaintyZones = (-1.0e21, -1.0e20, 8.02333524916e-05, 0.000574887089897, 0.00166339741554)

calibrationCurve = cms.PSet(
   Class = cms.string("LinInterpolatedTable1D"),
   xmin = cms.double(8.02333524916e-05),
   xmax = cms.double(0.0262760131586),
   leftExtrapolationLinear = cms.bool(False),
   rightExtrapolationLinear = cms.bool(True),
   data = cms.vdouble((0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.00859210360795, 0.0223596692085, 0.0541835650802, 0.103220455348, 0.12001530081, 0.137428015471, 0.163469940424, 0.185542061925, 0.204979881644, 0.223764330149, 0.242792025208, 0.262098163366, 0.281670063734, 0.302229017019, 0.322533875704, 0.343597441912, 0.364600479603, 0.386141657829, 0.408728569746, 0.430707722902, 0.45277351141, 0.474644869566, 0.49660935998, 0.518838465214, 0.541296064854, 0.563513040543, 0.585679769516, 0.607681155205, 0.629758119583, 0.651776194572, 0.674069464207, 0.696533203125, 0.718949377537, 0.741799652576, 0.764667034149, 0.788338661194, 0.811930596828, 0.836040377617, 0.860642910004, 0.885528385639, 0.910239458084, 0.934288084507, 0.958390653133, 0.981845200062, 1.00504374504, 1.02734494209, 1.04956364632, 1.07172966003, 1.09378802776, 1.115852952, 1.13797008991, 1.16021811962, 1.18257331848, 1.20501291752, 1.22728216648, 1.25056266785, 1.27360987663, 1.29664862156, 1.31969106197, 1.34215307236, 1.36447119713, 1.38673901558, 1.40874755383, 1.43096673489, 1.45408308506, 1.47732436657, 1.50126719475, 1.52579391003, 1.5512752533, 1.57693994045, 1.60305678844, 1.62872779369, 1.65313374996, 1.67643809319, 1.69936442375, 1.7222673893, 1.74549508095, 1.76914179325, 1.79300701618, 1.81675243378, 1.84052562714, 1.86492943764, 1.88946449757, 1.91421341896, 1.9393901825, 1.96436035633, 1.98887598515, 2.01318311691, 2.03569364548, 2.05751037598, 2.07945418358, 2.10128760338, 2.12281394005, 2.14465093613, 2.16700410843, 2.19034790993, 2.21390962601, 2.23819684982, 2.26317715645, 2.28830909729, 2.31405973434, 2.3395152092, 2.36451101303, 2.38906574249, 2.41393971443, 2.43829870224, 2.46270775795, 2.48715376854, 2.51162362099, 2.5363111496, 2.56106328964, 2.58589267731, 2.61108517647, 2.63610005379, 2.66081166267, 2.6843662262, 2.7072827816, 2.72865962982, 2.75024652481, 2.77149343491, 2.79295969009, 2.81441140175, 2.83716678619, 2.85951328278, 2.88334870338, 2.90662145615, 2.93185782433, 2.95761442184, 2.9830365181, 3.00774216652, 3.03305435181, 3.05673408508, 3.07980513573, 3.10271525383, 3.12557005882, 3.14839267731, 3.17128038406, 3.194190979, 3.21786928177, 3.24199676514, 3.26721119881, 3.29269790649, 3.318171978, 3.34319257736, 3.36789441109, 3.39296627045, 3.41735005379, 3.442070961, 3.46560001373, 3.48908209801, 3.51229381561, 3.53572535515, 3.55894970894, 3.5821352005, 3.60636591911, 3.63157010078, 3.65775108337, 3.68417525291, 3.71053028107, 3.73704791069, 3.7636115551, 3.79006910324, 3.81520295143, 3.84057760239, 3.86491036415, 3.88854050636, 3.91189837456, 3.93529057503, 3.95739626884, 3.97898077965, 4.00083494186, 4.02249574661, 4.04434490204, 4.0662560463, 4.08814525604, 4.11061429977, 4.1334605217, 4.1564874649, 4.17956638336, 4.20255184174, 4.22600603104, 4.25021791458, 4.27451848984, 4.29876089096, 4.32276058197, 4.3469543457, 4.37104463577, 4.39523029327, 4.41929531097, 4.44304466248, 4.46654891968, 4.49073314667, 4.51413488388, 4.53752851486, 4.5608754158, 4.58408117294, 4.60735225677, 4.63061714172, 4.6534948349, 4.67597293854, 4.69869422913, 4.72095632553, 4.74350690842, 4.76624822617, 4.7888174057, 4.81129264832, 4.83386611938, 4.85649728775, 4.87912225723, 4.90269899368, 4.92608451843, 4.95061254501, 4.97453355789, 4.99840831757, 5.02297687531, 5.04739570618, 5.0718960762, 5.09685087204, 5.12125730515, 5.14604902267, 5.17098236084, 5.1961016655, 5.22091722488, 5.24553871155, 5.27014923096, 5.2948384285, 5.31937980652, 5.34364366531, 5.36824989319, 5.39247131348, 5.41667938232, 5.44117641449, 5.46541166306, 5.48957204819, 5.51351928711, 5.53736543655, 5.56154251099, 5.585542202, 5.60953044891, 5.63357686996, 5.65779829025, 5.68182945251, 5.70585775375, 5.72972488403, 5.75372028351, 5.77776432037, 5.80138063431, 5.82513856888, 5.84887552261, 5.87267827988, 5.89644289017, 5.92024278641, 5.94397687912, 5.96777629852, 5.99159145355, 6.01526975632, 6.03894329071, 6.06271648407, 6.08658123016, 6.11047363281, 6.13423013687, 6.15806913376, 6.18229389191, 6.20648384094, 6.23129749298, 6.25574541092, 6.2798705101, 6.30468034744, 6.32936477661, 6.35399436951, 6.3780875206, 6.40243339539, 6.42694807053, 6.45145845413, 6.4757900238, 6.5001745224, 6.52447938919, 6.54865694046, 6.57296085358, 6.59716510773, 6.62124109268, 6.64557123184, 6.66920518875, 6.69316005707, 6.71694374084, 6.74068498611, 6.76477766037, 6.78861904144, 6.81200027466, 6.83600282669, 6.85937976837, 6.88186407089, 6.90536355972, 6.92913675308, 6.9524064064, 6.97569513321, 6.99898672104, 7.02274751663, 7.04668855667, 7.07063007355, 7.09457111359, 7.11851215363, 7.1424536705, 7.16639471054, 7.19033622742, 7.21427726746, 7.23821878433, 7.26215982437, 7.28610086441, 7.31004238129, 7.33398342133, 7.3579249382, 7.38186597824, 7.40580701828, 7.42974853516, 7.4536895752, 7.47763109207, 7.50157213211, 7.52551317215, 7.54945468903, 7.57339572906, 7.59733724594, 7.62127828598, 7.64521980286, 7.6691608429, 7.69310188293, 7.71704339981, 7.74098443985, 7.76492595673, 7.78886699677, 7.8128080368, 7.83674955368, 7.86069059372, 7.8846321106, 7.90857315063, 7.93251466751, 7.95645570755, 7.98039674759, 8.00433826447, 8.0282793045, 8.05222034454, 8.07616233826, 8.1001033783, 8.12404441833, 8.14798545837, 8.17192649841, 8.19586849213, 8.21980953217, 8.2437505722, 8.26769161224, 8.29163265228, 8.315574646, 8.33951568604, 8.36345672607, 8.38739776611, 8.41133880615, 8.43528079987, 8.4592218399, 8.48316287994, 8.50710391998, 8.53104496002, 8.55498695374, 8.57892799377, 8.60286903381, 8.62681007385, 8.65075111389, 8.6746931076, 8.69863414764, 8.72257518768, 8.74651622772, 8.77045822144, 8.79439926147, 8.81834030151, 8.84228134155, 8.86622238159, 8.89016437531, 8.91410541534, 8.93804645538, 8.96198749542, 8.98592853546, 9.00987052917, 9.03381156921, 9.05775260925, 9.08169364929, 9.10563468933, 9.12957668304, 9.15351772308, 9.17745876312, 9.20139980316, 9.2253408432, 9.24928283691, 9.27322387695, 9.29716491699, 9.32110595703, 9.34504699707, 9.36898899078, 9.39293003082, 9.41687107086, 9.4408121109, 9.46475410461, 9.48869514465, 9.51263618469, 9.53657722473, 9.56051826477, 9.58446025848, 9.60840129852, 9.63234233856, 9.6562833786, 9.68022441864, 9.70416641235, 9.72810745239, 9.75204849243, 9.77598953247, 9.79993057251, 9.82387256622, 9.84781360626, 9.8717546463, 9.89569568634, 9.91963672638, 9.94357872009, 9.96751976013, 9.99146080017, 10.0154018402, 10.0393428802, 10.063284874, 10.087225914, 10.111166954, 10.1351079941, 10.1590499878, 10.1829910278, 10.2069320679, 10.2308731079, 10.2548141479, 10.2787561417, 10.3026971817, 10.3266382217, 10.3505792618, 10.3745203018, 10.3984622955, 10.4224033356, 10.4463443756, 10.4702854156, 10.4942264557, 10.5181684494, 10.5421094894, 10.5660505295, 10.5899915695, 10.6139326096, 10.6378746033, 10.6618156433, 10.6857566833, 10.7096977234, 10.7336387634, 10.7575807571, 10.7815217972, 10.8054628372, 10.8294038773, 10.853345871, 10.877286911, 10.901227951, 10.9251689911, 10.9491100311, 10.9730520248, 10.9969930649, 11.0209341049, 11.044875145, 11.068816185, 11.0927581787, 11.1166992188, 11.1406402588, 11.1645812988, 11.1885223389, 11.2124643326, 11.2364053726, 11.2603464127, 11.2842874527, 11.3082284927, 11.3321704865, 11.3561115265, 11.3800525665, 11.4039936066, 11.4279346466, 11.4518766403, 11.4758176804, 11.4997587204, 11.5236997604, 11.5476417542, 11.5715827942, 11.5955238342, 11.6194648743))
)

uncertaintyCurve = cms.PSet(
   Class = cms.string("LinInterpolatedTable1D"),
   xmin = cms.double(8.02333524916e-05),
   xmax = cms.double(0.0262760131586),
   leftExtrapolationLinear = cms.bool(False),
   rightExtrapolationLinear = cms.bool(True),
   data = cms.vdouble((0.0, 0.0987078025937, 0.128971979022, 0.166080102324, 0.203273147345, 0.235639765859, 0.265795320272, 0.295376360416, 0.324564874172, 0.354021847248, 0.373264819384, 0.387517631054, 0.383715540171, 0.362968206406, 0.374353438616, 0.385052591562, 0.387225925922, 0.393340229988, 0.402494460344, 0.412599623203, 0.421848982573, 0.430912584066, 0.439813494682, 0.447598844767, 0.454941183329, 0.46102103591, 0.466716140509, 0.471569061279, 0.475270777941, 0.479212105274, 0.483101665974, 0.476743519306, 0.48465821147, 0.492223471403, 0.48801150918, 0.48000523448, 0.484795063734, 0.489413589239, 0.494474053383, 0.500382721424, 0.505401134491, 0.509634196758, 0.513231694698, 0.517105937004, 0.519902944565, 0.522519767284, 0.525511860847, 0.528483092785, 0.531530022621, 0.534397363663, 0.537242770195, 0.54014724493, 0.543184876442, 0.546205699444, 0.549639225006, 0.553067028522, 0.556916236877, 0.560789465904, 0.56451189518, 0.567835748196, 0.570257484913, 0.572588682175, 0.574765861034, 0.577228367329, 0.579786717892, 0.581635773182, 0.583858847618, 0.585919141769, 0.587932825089, 0.589021146297, 0.589863717556, 0.590281248093, 0.590850830078, 0.591509222984, 0.591866970062, 0.592277884483, 0.593545019627, 0.594845056534, 0.596583247185, 0.598800599575, 0.601028203964, 0.603899538517, 0.607359349728, 0.610045492649, 0.613029301167, 0.615809738636, 0.618233382702, 0.618407785892, 0.618781626225, 0.618621170521, 0.617960572243, 0.617243289948, 0.616976201534, 0.617047011852, 0.618507444859, 0.62051576376, 0.622158706188, 0.624407887459, 0.627856731415, 0.630912840366, 0.63316899538, 0.635006427765, 0.635371506214, 0.635783433914, 0.635686814785, 0.635098993778, 0.633914113045, 0.632316350937, 0.632089316845, 0.633064091206, 0.633939743042, 0.636424601078, 0.639037370682, 0.641542077065, 0.643901526928, 0.645216703415, 0.646670460701, 0.648048639297, 0.648946046829, 0.6496322155, 0.650563299656, 0.651668787003, 0.652770578861, 0.654419779778, 0.6558842659, 0.657486498356, 0.65958738327, 0.661837756634, 0.664436519146, 0.66666328907, 0.66813147068, 0.669020116329, 0.670351624489, 0.671076357365, 0.671459376812, 0.671795904636, 0.672463357449, 0.672040462494, 0.672025680542, 0.671521961689, 0.67156046629, 0.671782016754, 0.672374427319, 0.672780990601, 0.673403084278, 0.674681127071, 0.676304101944, 0.677380502224, 0.679163336754, 0.680887281895, 0.682089805603, 0.683906376362, 0.684135735035, 0.683880031109, 0.684958100319, 0.685959815979, 0.686950623989, 0.68803358078, 0.689358234406, 0.691250443459, 0.6934877038, 0.696110546589, 0.698679208755, 0.700643479824, 0.702413082123, 0.703874111176, 0.704173266888, 0.70506131649, 0.704187750816, 0.702845275402, 0.701166570187, 0.699763476849, 0.699540436268, 0.698905348778, 0.6991558671, 0.699468970299, 0.700853466988, 0.702447652817, 0.704074263573, 0.705694556236, 0.706726431847, 0.707369148731, 0.707400143147, 0.707520246506, 0.708290874958, 0.708254337311, 0.70790296793, 0.708305239677, 0.707754194736, 0.707803845406, 0.708282232285, 0.709816396236, 0.710784137249, 0.712134301662, 0.713589191437, 0.715847611427, 0.717848062515, 0.719937682152, 0.722159862518, 0.723895967007, 0.725962936878, 0.727874755859, 0.728931903839, 0.729771375656, 0.730096459389, 0.73062312603, 0.730727612972, 0.731314659119, 0.731410861015, 0.732020437717, 0.732460439205, 0.732880830765, 0.732944846153, 0.733292222023, 0.733581483364, 0.733994245529, 0.734717428684, 0.735400855541, 0.736207485199, 0.737323999405, 0.73829627037, 0.739247143269, 0.740039825439, 0.741125047207, 0.742231488228, 0.743446707726, 0.744723200798, 0.745957612991, 0.747466683388, 0.749047040939, 0.750371217728, 0.751564085484, 0.752598583698, 0.753852367401, 0.755274891853, 0.756497621536, 0.758364200592, 0.760038018227, 0.761293172836, 0.762499511242, 0.764403402805, 0.766243159771, 0.767984807491, 0.770038723946, 0.771979928017, 0.774037122726, 0.776078402996, 0.778511464596, 0.780505120754, 0.782068431377, 0.784453094006, 0.78633338213, 0.787587344646, 0.788916349411, 0.789696216583, 0.790830254555, 0.791582167149, 0.791925370693, 0.792821884155, 0.793401479721, 0.793413877487, 0.792913496494, 0.792730808258, 0.792901039124, 0.793164014816, 0.792996287346, 0.793347418308, 0.793141484261, 0.793567538261, 0.79458296299, 0.79530787468, 0.794913172722, 0.794952571392, 0.794655621052, 0.795330762863, 0.796242594719, 0.797160148621, 0.798074066639, 0.798842489719, 0.799688160419, 0.800504624844, 0.8012996912, 0.802166938782, 0.803082287312, 0.803956508636, 0.804857730865, 0.805716991425, 0.806605935097, 0.807452738285, 0.808348178864, 0.809272289276, 0.810281932354, 0.811250209808, 0.812218844891, 0.813149809837, 0.814272046089, 0.815392196178, 0.816438317299, 0.817463934422, 0.818466484547, 0.819516718388, 0.820544481277, 0.821602702141, 0.822670698166, 0.823723316193, 0.824783980846, 0.825766682625, 0.826727151871, 0.827744662762, 0.82879948616, 0.82980042696, 0.830754578114, 0.83179795742, 0.832680881023, 0.833862841129, 0.83485352993, 0.835795760155, 0.836766839027, 0.837745845318, 0.838635325432, 0.839582741261, 0.840479552746, 0.84122979641, 0.84212231636, 0.843016684055, 0.843752145767, 0.84456217289, 0.845411777496, 0.846309542656, 0.847201704979, 0.848123788834, 0.848985254765, 0.849894225597, 0.850836455822, 0.851734161377, 0.852646648884, 0.85368347168, 0.854961514473, 0.855969905853, 0.85684555769, 0.857752859592, 0.858959853649, 0.859866440296, 0.860773026943, 0.861679673195, 0.862586259842, 0.863492846489, 0.864399492741, 0.865306079388, 0.866212666035, 0.867119252682, 0.868025898933, 0.86893248558, 0.869839072227, 0.870745718479, 0.871652305126, 0.872558891773, 0.873465538025, 0.874372124672, 0.875278711319, 0.876185357571, 0.877091944218, 0.877998530865, 0.878905117512, 0.879811763763, 0.88071835041, 0.881624937057, 0.882531583309, 0.883438169956, 0.884344756603, 0.885251402855, 0.886157989502, 0.887064576149, 0.887971222401, 0.888877809048, 0.889784395695, 0.890690982342, 0.891597628593, 0.89250421524, 0.893410801888, 0.894317448139, 0.895224034786, 0.896130621433, 0.897037267685, 0.897943854332, 0.898850440979, 0.899757087231, 0.900663673878, 0.901570260525, 0.902476906776, 0.903383493423, 0.90429008007, 0.905196666718, 0.906103312969, 0.907009899616, 0.907916486263, 0.908823132515, 0.909729719162, 0.910636305809, 0.911542952061, 0.912449538708, 0.913356125355, 0.914262771606, 0.915169358253, 0.916075944901, 0.916982531548, 0.917889177799, 0.918795764446, 0.919702351093, 0.920608997345, 0.921515583992, 0.922422170639, 0.923328816891, 0.924235403538, 0.925141990185, 0.926048636436, 0.926955223083, 0.927861809731, 0.928768396378, 0.929675042629, 0.930581629276, 0.931488215923, 0.932394862175, 0.933301448822, 0.934208035469, 0.935114681721, 0.936021268368, 0.936927855015, 0.937834501266, 0.938741087914, 0.939647674561, 0.940554320812, 0.941460907459, 0.942367494106, 0.943274080753, 0.944180727005, 0.945087313652, 0.945993900299, 0.946900546551, 0.947807133198, 0.948713719845, 0.949620366096, 0.950526952744, 0.951433539391, 0.952340185642, 0.953246772289, 0.954153358936, 0.955059945583, 0.955966591835, 0.956873178482, 0.957779765129, 0.958686411381, 0.959592998028, 0.960499584675, 0.961406230927, 0.962312817574, 0.963219404221, 0.964126050472, 0.965032637119, 0.965939223766, 0.966845810413, 0.967752456665, 0.968659043312, 0.969565629959, 0.970472276211, 0.971378862858, 0.972285449505, 0.973192095757, 0.974098682404, 0.975005269051, 0.975911915302, 0.976818501949, 0.977725088596, 0.978631734848, 0.979538321495, 0.980444908142, 0.981351494789, 0.982258141041, 0.983164727688, 0.984071314335, 0.984977960587, 0.985884547234, 0.986791133881, 0.987697780132, 0.988604366779, 0.989510953426, 0.990417599678, 0.991324186325, 0.992230772972, 0.993137359619, 0.994044005871, 0.994950592518, 0.995857179165, 0.996763825417, 0.997670412064, 0.998576998711, 0.999483644962, 1.000390172, 1.00129687786, 1.00220346451))
)