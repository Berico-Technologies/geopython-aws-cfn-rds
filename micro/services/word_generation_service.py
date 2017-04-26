import json
import random
from micro.services.mapping_service import MappingService

coordinate_dictionary = {
    "a": (0.004368251, [[0.00370444605847009, 0.00131335747285277], [0, 0.00130189349184917],
                        [0.000720838354309805, -0.000891747138247467], [0.00373497352930974, -0.000976924110652533],
                        [0.00394600280252, 0.00110081275855123], [0.00436825055593992, -0.00131335747285277]]),
    "b": (0.003655132, [[0, 0.00206922485694605], [0.000734326854740175, -0.00206922485695316],
                        [0.00365513222942004, -0.00181022367175387], [0.00342608069873007, -0.000214397760856855],
                        [0.000407775754130313, -4.26235852515333E-05]]),
    "c": (0.004006262, [[0.00361518535917993, 0.00101823929870193], [0, 0.000749231048700949],
                        [0.000314109528869899, -0.00101823929870193], [0.00400626243063984, -0.000748113920202798]]),
    "d": (0.003859748, [[0.00300822755169028, -0.000127574347352777], [0, -0.000171406405755192],
                        [0.000313746859850195, -0.00193889946755377], [0.00385974773822007, -0.00184402598025457],
                        [0.00244913095729027, 0.00193889946754666]]),
    "e": (0.003704318, [[0.00050393897525991, -0.00019268459370636], [0.00350614966603002, -1.94877761998669E-05],
                        [0.00075850429323987, 0.000977978974596283], [0, -0.000977978974603388],
                        [0.00370431778928015, -0.000967480322003667]]),
    "f": (0.002194638, [[0, -0.0016684757079517], [0.000618053186479894, 0.00166847570794459],
                        [0.00219463842979994, 0.000956490119648379], [0.000620043868719833, 0.00162528346224633],
                        [0.000375199710339835, 0.000238672687743247], [0.00130281911332997, 0.000208854280145943]]),
    "g": (0.002790785, [[0.00223664739436025, 0.0017016616966572], [0.000078840058399976, 0.00162736668095675],
                        [0, -1.61667781455321E-05], [0.00224475979632022, -0.000156723017944671],
                        [0.00245616017149031, 0.00196414646155318], [0.00279078478180006, -0.00196414646154608],
                        [0.000995016713610131, -0.00151456659674665]]),
    "h": (0.002925207, [[0.000437075141830334, 0.00196969020539939], [0, -0.00196969020539939],
                        [0.00015227172497001, -0.000238666116601394], [0.00292520707309007, -0.000112434290898022],
                        [0.00253943780110033, -0.00180358154980098]]),
    "i": (0.00020409, [[0, -0.00114681297299768], [0.000204089695809984, 0.00114681297300478]]),
    "j": (0.001970038, [[0.00184627803852022, 0.00176361607095288], [0.0019700382434702, -0.000957530741651169],
                        [0, -0.00176361607095288]]),
    "k": (0.002457248, [[0.000666147402089923, 0.00201450758525112], [0, -0.00201450758525112],
                        [0.000318999161430078, -0.000540459327353915], [0.00245724824808002, -3.46133216524436E-05],
                        [0.000479151572169823, -0.000667842176952149], [0.00238523118370981, -0.0018509097961541]]),
    "l": (0.000391599, [[0, 0.00176927337015087], [0.000391598501150003, -0.00176927337015087]]),
    "m": (0.003856657, [[0, -0.00106423473220474], [0.000752974804969941, 0.00106423473219763],
                        [0.00173121236404983, -8.88884533054579E-05], [0.00314812537458975, 0.0010116547709984],
                        [0.00385665680527003, -0.00100970899350017]]),
    "n": (0.002855511, [[0, -0.00073261096629551], [5.92744937000234E-06, 0.000780225696999537],
                        [0.00285551149913976, 0.000908726069802412], [0.00270944482723978, -0.000908726069795307]]),
    "o": (0.00308908, [[0.00308907959625992, 0.000909793109499901], [0, 0.00095084363050546],
                       [0.000239308396900118, -0.000860933028796751], [0.00294465409522982, -0.000950843630498355],
                       [0.00293887228270018, 0.000821145092601228]]),
    "p": (0.004025586, [[0, -0.00168673665429964], [0.000151161020589985, 0.00168673665429964],
                        [0.00402558572250999, 0.00135443014389836], [0.0031584765136401, 8.83385022945049E-05],
                        [0.00013858182053994, 0.000303471925697352]]),
    "q": (0.004839691, [[0.00254391303145995, 0.00173724299385469], [0.000228135277420272, 0.00174670513365527],
                        [0, 1.45288204578264E-05], [0.00316602460158988, -2.57636710472298E-05],
                        [0.00262906379701988, 0.00156559876845819], [0.00370895431194018, -0.00174670513364816],
                        [0.00483969109634996, -0.00116837179874807]]),
    "r": (0.00317019, [[0.000303372094839993, -0.000880630345150735], [0, 0.000670924808055418],
                       [0.00253719813894993, 0.000880630345150735], [0.0031701896911196, 0.000544039702255361]]),
    "s": (0.004164147, [[0.00226145508135023, 0.00148401062484993], [0.00010789810998002, 0.00132322435855059],
                        [8.25520200100627E-05, 0.000199110124448509], [0.00416414711488011, 0.000387730157150656],
                        [0.00324701465704003, -0.00148401062484993], [0, -0.00135804240024839]]),
    "t": (0.002392849, [[0.000797136697379575, -0.00147131825055169], [0.00104805453628964, 0.00147131825055169],
                        [0.00108172786313965, 0.000737045914647183], [0, 0.000764703727249127],
                        [0.00239284933735995, 0.000755896724150773]]),
    "u": (0.003586933, [[0, 0.0012282743610541], [0.000347871497800245, -0.00131677296194965],
                        [0.00326859524845036, -0.00105882533434709], [0.00316017698240012, 0.00131677296194965],
                        [0.0035869331135201, -0.00127037353854575]]),
    "v": (0.002851695, [[0, 0.00126385223614989], [0.00173954159027989, -0.00134778102025024],
                        [0.00285169535468999, 0.00134778102025024]]),
    "w": (0.004619723, [[0, 0.00123248627054551], [0.00135751284750985, -0.00147109465035555],
                        [0.00240853115517004, 0.000877786939845748], [0.00358030107600982, -0.00113692675455468],
                        [0.00461972302477998, 0.00147109465034845]]),
    "x": (0.004394238, [[0.000481325012150258, -0.00110823309579899], [0.00439423830236985, 0.00110823309579899],
                        [0.00274427141073019, 4.75780036026663E-05], [0, 0.00100275802969918],
                        [0.00432767628191, -0.000837641928796984]]),
    "y": (0.003178249, [[1.21944046598266E-05, 0.00157764252605119], [0.00140305887411962, -0.000174760508748761],
                        [0.00317824857483995, 0.00153589873265503], [0, -0.00157764252604409]]),
    "z": (0.004012499, [[0, 0.000939181491347085], [0.00401249864997988, 0.000952423673545866],
                        [0.000160543960920023, -0.000917045763451085], [0.00378917325743977, -0.000952423673552971]])
}


class WordGenerationService:
    @staticmethod
    def generate_letters(word: str):
        start_x, start_y = WordGenerationService.random_position_around_basel()
        spacing = 0.001
        geojson = WordGenerationService.generate_word(word, start_x, start_y, spacing)
        to_save = {"name": word, "geometry": geojson}
        return MappingService().save_feature_collection(to_save)

    @staticmethod
    def random_position_around_basel():
        min_x = 7.5
        max_x = 7.7
        min_y = 47.4
        max_y = 47.6

        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)

        return x, y

    @staticmethod
    def generate_word(word, start_x, start_y, spacing):
        word = word.lower()
        features = []
        for letter in word:
            feature, width = WordGenerationService.generate_letter(letter, start_x, start_y)
            if feature is not None:
                start_x += (width + spacing)
                features.append(feature)

        geojson = \
            {
                "type": "FeatureCollection",
                "crs": {
                    "type": "name",
                    "properties": {
                        "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                    }
                },
                "features": features
            }

        return geojson

    @staticmethod
    def generate_letter(letter, start_x, start_y):
        letter_properties = coordinate_dictionary.get(letter)
        if letter_properties is None:
            return None, 0

        coordinates_array = []
        width = letter_properties[0]
        offsets = letter_properties[1]

        for offset in offsets:
            coordinates_array.append([offset[0] + start_x, offset[1] + start_y])

        geojson = \
            {
                "type": "Feature",
                "properties": {
                    "letter": letter
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": coordinates_array
                }
            }

        return geojson, width
