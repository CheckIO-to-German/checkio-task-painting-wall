#TESTS is a dict with all you tests.
#Keys for this will be categories' names.
#Each test is dict with
#	"input" -- input data for user function
#	"answer" -- your right answer
#	"explanation" -- not necessary key, it's using for additional info in animation.

TESTS = {
    "Short By Hand 1 (Example)": [
        {
            "input": [5, [[1, 5], [11, 15], [2, 14], [21, 25]]],
            "answer": 1
        },
        {
            "input": [6, [[1, 5], [11, 15], [2, 14], [21, 25]]],
            "answer": 2
        },
        {
            "input": [11, [[1, 5], [11, 15], [2, 14], [21, 25]]],
            "answer": 3
        },
        {
            "input": [16, [[1, 5], [11, 15], [2, 14], [21, 25]]],
            "answer": 4
        },
        {
            "input": [21, [[1, 5], [11, 15], [2, 14], [21, 25]]],
            "answer": -1
        }
    ],
    "Short By Hand 2": [
        {
            "input": [5, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]],
            "answer": 2
        },
        {
            "input": [15, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]],
            "answer": 3
        },
        {
            "input": [20, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]],
            "answer": 4
        },
        {
            "input": [30, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]],
            "answer": 6
        },
        {
            "input": [35, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]],
            "answer": -1
        }
    ],
    "Short Generated 1": [
        {
            "input": [1000, [[8598, 9442], [4221, 4432], [4864, 5415], [1315, 1960], [9577, 10482], [8147, 8346],
                             [6063, 6836],
                             [24, 606], [6170, 7131], [1397, 2020], [4690, 5651], [5267, 5464], [8422, 8886],
                             [5547, 5738],
                             [5722, 6511], [6605, 6905], [1321, 2242], [9335, 9993], [1626, 1887], [4699, 4926]]],
            "answer": 2
        },
        {
            "input": [5000, [[8598, 9442], [4221, 4432], [4864, 5415], [1315, 1960], [9577, 10482], [8147, 8346],
                             [6063, 6836],
                             [24, 606], [6170, 7131], [1397, 2020], [4690, 5651], [5267, 5464], [8422, 8886],
                             [5547, 5738],
                             [5722, 6511], [6605, 6905], [1321, 2242], [9335, 9993], [1626, 1887], [4699, 4926]]],
            "answer": 9
        },
        {
            "input": [5400, [[8598, 9442], [4221, 4432], [4864, 5415], [1315, 1960], [9577, 10482], [8147, 8346],
                             [6063, 6836],
                             [24, 606], [6170, 7131], [1397, 2020], [4690, 5651], [5267, 5464], [8422, 8886],
                             [5547, 5738],
                             [5722, 6511], [6605, 6905], [1321, 2242], [9335, 9993], [1626, 1887], [4699, 4926]]],
            "answer": 11
        },
        {
            "input": [5700, [[8598, 9442], [4221, 4432], [4864, 5415], [1315, 1960], [9577, 10482], [8147, 8346],
                             [6063, 6836],
                             [24, 606], [6170, 7131], [1397, 2020], [4690, 5651], [5267, 5464], [8422, 8886],
                             [5547, 5738],
                             [5722, 6511], [6605, 6905], [1321, 2242], [9335, 9993], [1626, 1887], [4699, 4926]]],
            "answer": 14
        },
        {
            "input": [6000, [[8598, 9442], [4221, 4432], [4864, 5415], [1315, 1960], [9577, 10482], [8147, 8346],
                             [6063, 6836],
                             [24, 606], [6170, 7131], [1397, 2020], [4690, 5651], [5267, 5464], [8422, 8886],
                             [5547, 5738],
                             [5722, 6511], [6605, 6905], [1321, 2242], [9335, 9993], [1626, 1887], [4699, 4926]]],
            "answer": 15
        },
        {
            "input": [6500, [[8598, 9442], [4221, 4432], [4864, 5415], [1315, 1960], [9577, 10482], [8147, 8346],
                             [6063, 6836],
                             [24, 606], [6170, 7131], [1397, 2020], [4690, 5651], [5267, 5464], [8422, 8886],
                             [5547, 5738],
                             [5722, 6511], [6605, 6905], [1321, 2242], [9335, 9993], [1626, 1887], [4699, 4926]]],
            "answer": -1
        }
    ],
    "Short Generated 2": [
        {
            "input": [30000,
                      [[53013, 58178], [66996, 70770], [46244, 50076], [69373, 79267], [3343, 9935], [80414, 82602],
                       [61293, 68007], [50771, 53974], [34296, 43518], [92413, 100031], [17305, 19487], [84654, 87021],
                       [17333, 21892], [93387, 99456], [92406, 97098], [37781, 42924], [98927, 100960], [86738, 89338],
                       [48177, 52067], [28524, 32583]]],
            "answer": 6
        },
        {
            "input": [57000,
                      [[53013, 58178], [66996, 70770], [46244, 50076], [69373, 79267], [3343, 9935], [80414, 82602],
                       [61293, 68007], [50771, 53974], [34296, 43518], [92413, 100031], [17305, 19487], [84654, 87021],
                       [17333, 21892], [93387, 99456], [92406, 97098], [37781, 42924], [98927, 100960], [86738, 89338],
                       [48177, 52067], [28524, 32583]]],
            "answer": 11
        },
        {
            "input": [68000,
                      [[53013, 58178], [66996, 70770], [46244, 50076], [69373, 79267], [3343, 9935], [80414, 82602],
                       [61293, 68007], [50771, 53974], [34296, 43518], [92413, 100031], [17305, 19487], [84654, 87021],
                       [17333, 21892], [93387, 99456], [92406, 97098], [37781, 42924], [98927, 100960], [86738, 89338],
                       [48177, 52067], [28524, 32583]]],
            "answer": 20
        },
        {
            "input": [70000,
                      [[53013, 58178], [66996, 70770], [46244, 50076], [69373, 79267], [3343, 9935], [80414, 82602],
                       [61293, 68007], [50771, 53974], [34296, 43518], [92413, 100031], [17305, 19487], [84654, 87021],
                       [17333, 21892], [93387, 99456], [92406, 97098], [37781, 42924], [98927, 100960], [86738, 89338],
                       [48177, 52067], [28524, 32583]]],
            "answer": -1
        }
    ],
    "Large By Hand": [
        {
            "input": [10000000000000, [[183456789012345, 193456789078479], [163456789034827, 173456789028737],
                                       [103456789038198, 113456789073490], [123456789073249, 203456789073621]]],
            "answer": 1
        },
        {
            "input": [20000000000000, [[183456789012345, 193456789078479], [163456789034827, 173456789028737],
                                       [103456789038198, 113456789073490], [123456789073249, 203456789073621]]],
            "answer": 2
        },
        {
            "input": [30000000000000, [[183456789012345, 193456789078479], [163456789034827, 173456789028737],
                                       [103456789038198, 113456789073490], [123456789073249, 203456789073621]]],
            "answer": 3
        },
        {
            "input": [50000000000000, [[183456789012345, 193456789078479], [163456789034827, 173456789028737],
                                       [103456789038198, 113456789073490], [123456789073249, 203456789073621]]],
            "answer": 4
        },
        {
            "input": [100000000000000, [[183456789012345, 193456789078479], [163456789034827, 173456789028737],
                                        [103456789038198, 113456789073490], [123456789073249, 203456789073621]]],
            "answer": -1
        }
    ],
    "Large Generated 1": [
        {
            "input": [464578738600000, [[618092831212219, 692920328043160], [784541961979258, 849250239149590],
                                        [153212679000591, 170403813123184], [397402071388980, 494330805397679],
                                        [947688880896887, 1031315325383029], [935301256930565, 986287435347942],
                                        [15780649536663, 68473689252834], [526775205748614, 588991194047996],
                                        [655862607385363, 673910180521194], [773094918999390, 841619268667280],
                                        [155080217158458, 163523868832795], [619408007658049, 621341345909422],
                                        [187242353118947, 253984595396399], [620306694433414, 710742874379812],
                                        [268250344952342, 301251875692343], [493812097589401, 585287020679206],
                                        [660549666775455, 686382635470395], [953288849899107, 981074697686018],
                                        [752283881298002, 800681840076545], [628408208573475, 664503152611721]]],
            "answer": 8
        },
        {
            "input": [623032679900000, [[618092831212219, 692920328043160], [784541961979258, 849250239149590],
                                        [153212679000591, 170403813123184], [397402071388980, 494330805397679],
                                        [947688880896887, 1031315325383029], [935301256930565, 986287435347942],
                                        [15780649536663, 68473689252834], [526775205748614, 588991194047996],
                                        [655862607385363, 673910180521194], [773094918999390, 841619268667280],
                                        [155080217158458, 163523868832795], [619408007658049, 621341345909422],
                                        [187242353118947, 253984595396399], [620306694433414, 710742874379812],
                                        [268250344952342, 301251875692343], [493812097589401, 585287020679206],
                                        [660549666775455, 686382635470395], [953288849899107, 981074697686018],
                                        [752283881298002, 800681840076545], [628408208573475, 664503152611721]]],
            "answer": 16
        },
        {
            "input": [650000000000000, [[618092831212219, 692920328043160], [784541961979258, 849250239149590],
                                        [153212679000591, 170403813123184], [397402071388980, 494330805397679],
                                        [947688880896887, 1031315325383029], [935301256930565, 986287435347942],
                                        [15780649536663, 68473689252834], [526775205748614, 588991194047996],
                                        [655862607385363, 673910180521194], [773094918999390, 841619268667280],
                                        [155080217158458, 163523868832795], [619408007658049, 621341345909422],
                                        [187242353118947, 253984595396399], [620306694433414, 710742874379812],
                                        [268250344952342, 301251875692343], [493812097589401, 585287020679206],
                                        [660549666775455, 686382635470395], [953288849899107, 981074697686018],
                                        [752283881298002, 800681840076545], [628408208573475, 664503152611721]]],
            "answer": -1
        }
    ],
    "Large Generated 2": [
        {
            "input": [409810512978000, [[858310018365524, 902063077244091], [932665378449117, 1028409672338264],
                                        [882165278163239, 957945652291761], [155331862264691, 231608087199557],
                                        [309323812898016, 328794059405147], [311727991597994, 391226174154816],
                                        [826415306967097, 893972043882819], [170753995991478, 221100797836809],
                                        [472995836315594, 478902758061898], [779003863306990, 822734502976504],
                                        [539843675072188, 554844466580541], [977564633426502, 991018537238369],
                                        [889461015856698, 901719104033374], [268288887276466, 292053591549963],
                                        [87698520389374, 109261297832598], [650723837467456, 729926149124749],
                                        [627448683684809, 644021001384284], [264317870081369, 322309330307873],
                                        [238729907671924, 290743490959244], [938382837602825, 955450166170994]]],
            "answer": 10
        },
        {
            "input": [612742616513000, [[858310018365524, 902063077244091], [932665378449117, 1028409672338264],
                                        [882165278163239, 957945652291761], [155331862264691, 231608087199557],
                                        [309323812898016, 328794059405147], [311727991597994, 391226174154816],
                                        [826415306967097, 893972043882819], [170753995991478, 221100797836809],
                                        [472995836315594, 478902758061898], [779003863306990, 822734502976504],
                                        [539843675072188, 554844466580541], [977564633426502, 991018537238369],
                                        [889461015856698, 901719104033374], [268288887276466, 292053591549963],
                                        [87698520389374, 109261297832598], [650723837467456, 729926149124749],
                                        [627448683684809, 644021001384284], [264317870081369, 322309330307873],
                                        [238729907671924, 290743490959244], [938382837602825, 955450166170994]]],
            "answer": 19
        },
        {
            "input": [620000000000000, [[858310018365524, 902063077244091], [932665378449117, 1028409672338264],
                                        [882165278163239, 957945652291761], [155331862264691, 231608087199557],
                                        [309323812898016, 328794059405147], [311727991597994, 391226174154816],
                                        [826415306967097, 893972043882819], [170753995991478, 221100797836809],
                                        [472995836315594, 478902758061898], [779003863306990, 822734502976504],
                                        [539843675072188, 554844466580541], [977564633426502, 991018537238369],
                                        [889461015856698, 901719104033374], [268288887276466, 292053591549963],
                                        [87698520389374, 109261297832598], [650723837467456, 729926149124749],
                                        [627448683684809, 644021001384284], [264317870081369, 322309330307873],
                                        [238729907671924, 290743490959244], [938382837602825, 955450166170994]]],
            "answer": -1
        }
    ],
}
