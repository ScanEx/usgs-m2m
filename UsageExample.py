import json
from pprint import pprint
from usgsDataTypes import usgsDataTypes
from usgsMethods import usgsMethods
import datetime


def main():
    # In order not to store the login/password in the code - auth with json-formatted text file:
    # {"username": "username", "password": "password"}
    txt_path = r"G:\Scripts\py_test\USGS\m2mAPI\json_pass.txt"
    with open(txt_path, 'r') as file:
        json_data = json.load(file)
        usgs_username = json_data['username']
        usgs_password = json_data['password']

    api = usgsMethods()  # instance created
    api.login(usgs_username, usgs_password)

    # Region of interest coordinate.
    # Examples:
    # 'Point' [lat ,lon]
    # 'Polygon' [[ [lat ,lon], ... ]]

    ROI = [[
        [66.36879999999996471, 58.47166737597581232],
        [66.36220376208370908, 58.47172264237849504],
        [66.35561425042772044, 58.47188838522760079],
        [66.34903818462350955, 58.47216443550075837],
        [66.34248227092905381, 58.47255051168156115],
        [66.3009655263342097, 58.47503602986034821],
        [66.29365762332503209, 58.47549945392734116],
        [65.92982575994977879, 58.50040121768040535],
        [65.92116044639828942, 58.50109957404868055],
        [65.91344997641454029, 58.50188845695328155],
        [65.89131344491795517, 58.50438100352386073],
        [65.87887108715625573, 58.505993818446143],
        [65.61010583511483674, 58.54517827384819384],
        [65.60359256185046206, 58.54618046634800521],
        [65.59870552547772604, 58.54697813373883264],
        [65.5898117006899497, 58.54854626757366987],
        [65.58142741955322208, 58.55024497092750835],
        [65.57319200201919784, 58.5521326919588887],
        [65.56512101804008807, 58.55420586730599553],
        [65.55722973497449857, 58.55646058287794631],
        [65.54953308925513511, 58.55889258106299167],
        [65.54204565860294451, 58.56149726857330506],
        [65.5347816348353831, 58.56426972491675542],
        [65.52775479731911901, 58.56720471147900753],
        [63.86993004824086029, 59.29641208788507356],
        [63.86300895850058623, 59.29950349752573402],
        [63.85635683429177334, 59.30274602624967883],
        [63.84998633004249768, 59.30613354374321489],
        [63.73337587435736395, 59.36986516078417253],
        [59.30035042481136998, 61.88007542830496277],
        [59.29409913688334655, 61.88373122047613606],
        [59.2881901809786882, 61.88751197248944891],
        [59.28263486350937228, 61.89141053216422961],
        [59.27744383407866735, 61.8954195217098686],
        [59.27262706465927522, 61.89953135144043017],
        [59.26819382993915042, 61.90373823390524421],
        [59.26415268888285937, 61.90803219841166083],
        [59.26051146754332422, 61.91240510591160273],
        [59.2572772431666408, 61.91684866423008771],
        [59.2544563296264073, 61.92135444360508245],
        [59.21700477123249584, 61.98210155551953449],
        [59.21462088795362888, 61.98658212948720347],
        [59.21264705649105053, 61.99110663888382078],
        [59.20438424205394767, 62.01071795467896663],
        [59.17086529909852288, 62.09411753577842319],
        [59.16930579638790277, 62.09875813437162151],
        [59.16817929644514606, 62.10342618344463972],
        [58.95711366956237498, 63.00911997926880304],
        [58.95639974413518303, 63.01380594673014457],
        [58.95613615668037255, 63.01850160190792849],
        [58.95627226681028787, 63.02256812622130155],
        [58.95674646968228672, 63.02662941013562659],
        [58.95798366085631415, 63.03443150621893665],
        [59.22432394346253659, 64.5125710304940867],
        [59.22546827945615178, 64.51724128089688293],
        [59.22708489333786019, 64.52188556406611042],
        [59.22917094224959556, 64.52649502395422587],
        [59.3900206528542185, 64.83069127565391909],
        [59.39260058849180268, 64.83525698698935003],
        [59.39564679352417897, 64.83977037759706263],
        [59.39915368292599851, 64.84422282767911838],
        [59.40311478241227405, 64.84860582958987152],
        [59.40752273920952575, 64.85291100427224364],
        [59.41236933460101, 64.85713011747895962],
        [59.41764549823767538, 64.86125509574173975],
        [59.42334132419381376, 64.86527804206087922],
        [59.4294460887506375, 64.86919125127781172],
        [59.43594826987890656, 64.87298722510251991],
        [59.60163125801051365, 64.96795952490867876],
        [59.60747759609881768, 64.97130764719889839],
        [59.84734828479707858, 65.09858383285524042],
        [59.85429360089119655, 65.10225527690306535],
        [59.86161415999481505, 65.10579517332331534],
        [59.86929606278124538, 65.10919673013501097],
        [59.87732469965249038, 65.11245341823644139],
        [59.8856847784271622, 65.11555898424876432],
        [61.68064988740292165, 65.76864342846408817],
        [61.68922129100155871, 65.77174901153819064],
        [61.69811628147374449, 65.77469751668684239],
        [61.70731786967871813, 65.77748327669087303],
        [61.71680845971917506, 65.78010093535243641],
        [61.72656988303504022, 65.78254545810176523],
        [61.73658343376371249, 65.78481214197796589],
        [61.74682990529328208, 65.78689662496520896],
        [61.86070825941783369, 65.80773242844122706],
        [61.87100083584488175, 65.80960771560853573],
        [61.88148153205924018, 65.81129932735524335],
        [61.90937567821106313, 65.81551572396006122],
        [61.90995515750353206, 65.81560293054883459],
        [61.91935293298172382, 65.81692949658736325],
        [61.92886735230808881, 65.81810856419696165],
        [61.93930584858804878, 65.81931337089156386],
        [61.95184356872726994, 65.8206235252111469],
        [61.96452461535000111, 65.82167765214444444],
        [61.97584138061694148, 65.8223948765137834],
        [61.98722417114078098, 65.82290816928775712],
        [61.99865105196562354, 65.82321654120937637],
        [62.01010000000007949, 65.82331939793232323],
        [62.0215489480344786, 65.82321654120937637],
        [62.03297582885932115, 65.82290816928775712],
        [62.04435861938333119, 65.8223948765137834],
        [62.05578859542418968, 65.82166941107175262],
        [62.07377266111598146, 65.82035584418878216],
        [62.08492417246088735, 65.8194375208467477],
        [62.09596725941401019, 65.81832111732285284],
        [62.1068809417505463, 65.81700875613495327],
        [81.11823437599497311, 63.25335642996481056],
        [81.12809951552407028, 63.25184130276210226],
        [81.1378075015838931, 63.25013302076922628],
        [81.14733969150540815, 63.24823486957620844],
        [83.91095562216247572, 62.66684385632510157],
        [83.92011036497854093, 62.66475948436345789],
        [83.92905732488480908, 62.66249289626051677],
        [83.93777935784578403, 62.66004844766337101],
        [83.94625976413925628, 62.65743083489093124],
        [83.95448232088335772, 62.65464508566179802],
        [83.96243131352025557, 62.65169654917781372],
        [83.96780323112488986, 62.64954758720909922],
        [84.3958715365054104, 62.47097589806719498],
        [84.40190980922528752, 62.46835105790898979],
        [84.40774128048155944, 62.46562811247491709],
        [86.08224092620389456, 61.63764928401292309],
        [86.08905118607901841, 61.63424738844503281],
        [86.09554160236098141, 61.63070707439351281],
        [86.10146455467787519, 61.62718164106775021],
        [86.10707052592522359, 61.62354093769414476],
        [86.13361620824116471, 61.60550519893178034],
        [86.13928049028032774, 61.601462144320692],
        [86.14455451514248807, 61.59730125002278101],
        [86.14927138099596959, 61.59317540394408752],
        [86.15360481392190195, 61.5889553164054746],
        [86.15754668527688409, 61.58464905716192561],
        [86.16108962470741517, 61.58026485736598943],
        [86.16363976974389516, 61.57669589634485874],
        [86.16592570003308538, 61.57308652498323909],
        [86.16794469735560824, 61.56944118131667665],
        [86.1696943743884276, 61.56576434604681936],
        [86.17008825926848203, 61.56486370866775815],
        [86.17158532481732891, 61.56110726912697828],
        [86.19106556587900059, 61.50801858068359707],
        [86.19252818252601855, 61.50337263447630676],
        [86.19356492976004347, 61.4987006144073689],
        [86.19417402380526028, 61.49401142357601202],
        [86.19435449763989254, 61.48931399379574714],
        [86.19423659961631756, 61.48618244903889263],
        [86.19392830611093359, 61.48305386617232671],
        [86.19342993505574668, 61.47993089059764316],
        [86.19274196474725613, 61.47681616218505951],
        [86.19161015435679474, 61.47231799165814436],
        [86.19147847903337833, 61.47180497014062439],
        [86.19003968387301029, 61.46630729532319037],
        [86.18822837137923898, 61.46062061954404498],
        [86.18757180270762319, 61.45894939512845667],
        [86.18462276515731446, 61.45175412606772625],
        [86.18273068668577253, 61.44757676573379968],
        [86.18049432778099117, 61.44343860241599486],
        [86.17791733896643791, 61.43934613939137535],
        [86.17500390140486388, 61.4353058055921224],
        [86.17256053345511191, 61.43226557278671862],
        [86.17105043207908466, 61.4304678719637991],
        [86.16788843280579613, 61.42689068956462961],
        [86.1644598899043217, 61.42337037700406199],
        [86.16076933475784472, 61.41991149543338224],
        [86.15682163349242728, 61.41651852492066155],
        [86.15262870337517143, 61.41320096852251709],
        [86.14819009352981993, 61.40995777890060481],
        [86.14307858401639351, 61.40636472329254048],
        [85.87879245313973797, 61.22920939575107013],
        [85.87300793095369045, 61.2254280629964569],
        [85.86688819177305732, 61.22177169728706758],
        [85.86376238652729853, 61.22002326920647874],
        [85.85155425279475594, 61.21333831943354653],
        [85.84577875908479427, 61.21029403575488459],
        [85.83976681510927165, 61.20735844709156481],
        [85.83352724953675761, 61.20453583298552758],
        [85.82149036749916604, 61.19965399151010388],
        [85.81577019626064384, 61.19756507294613357],
        [85.79629503180370875, 61.19068398973394096],
        [85.78615071629559452, 61.18730128771142063],
        [85.77563683818380014, 61.18419343823910594],
        [84.35911104739489019, 60.7789103883587245],
        [84.35762437848956097, 60.77848854562978431],
        [84.34919241054950589, 60.77623516477171961],
        [75.21593927822311798, 58.56473287012534001],
        [75.20770090128104357, 58.56284515544797387],
        [75.19931360791207453, 58.56114645785504536],
        [75.19079324746536486, 58.55963998339808541],
        [75.18215591385455809, 58.55832857494937116],
        [75.17341791586505906, 58.55721470697727682],
        [75.16459574711393543, 58.55630048099919804],
        [75.15570605570411544, 58.55558762172375964],
        [75.1467656136306914, 58.55507747388350026],
        [75.13779128598361012, 58.554770999768607],
        [75.12880000000012615, 58.5546687774599377],
        [66.36879999999996471, 58.47166737597581232],
    ]]

    spatialFilter = usgsDataTypes.SpatialFilterGeoJson(filterType='geojson',
                                                       geoJson=usgsDataTypes.GeoJson(type='Polygon',
                                                                                     coordinates=ROI)
                                                       )

    sceneFilter = usgsDataTypes.SceneFilter(
        acquisitionFilter=usgsDataTypes.AcquisitionFilter(start="2020-07-30",
                                                          end="2020-07-31"),
        cloudCoverFilter=None,
        datasetName='LANDSAT_8_C1',
        ingestFilter=None,
        metadataFilter=None,
        seasonalFilter=None,
        spatialFilter=spatialFilter
    )

    # sceneSearchResult = api.sceneSearch(datasetName='LANDSAT_8_C1', maxResults=1, startingNumber=None,
    #                                     metadataType='full',
    #                                     sortField=None,  # "Acquisition Date", '5e83d0b92ff6b5e8' - doesn't work
    #                                     sortDirection='ASC',
    #                                     sceneFilter=sceneFilter,
    #                                     compareListName=None,
    #                                     bulkListName=None,
    #                                     orderListName=None,
    #                                     excludeListName=None)

    # print('sceneFilter=\n')
    # pprint(sceneFilter)
    #
    # print('sceneSearchResult=\n')
    # pprint(sceneSearchResult)

    downloads = usgsDataTypes.Download(id=None,
                                       displayId=None,
                                       entityId='LC81590182020212LGN00',
                                       datasetId=None,
                                       available=None,
                                       filesize=None,
                                       productId='LC08_L1GT_159018_20200730_20200731_01_RT',
                                       productName=None,
                                       productCode=None,
                                       bulkAvailable=None,
                                       downloadSystem=None,
                                       secondaryDownloads=None,
                                       )

    # print('downloads=\n')
    # pprint(downloads)

    downloadRequest = api.downloadRequest(configurationCode=None,
                                          downloadApplication=None,
                                          downloads=[downloads],
                                          dataPaths=None,
                                          label=None,
                                          returnAvailable=False)

    print('downloadRequest=\n')
    pprint(downloadRequest)

    api.logout()
    print('Done!')


if __name__ == '__main__':
    main()
