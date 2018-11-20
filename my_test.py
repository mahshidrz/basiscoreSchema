import copy

my_dict = {'root': {
    'properties': {'@LID': '2', '@MId': '10', '@usedForId': '1290136', '@script': '', '@helpUrl': '/PrpHelpUrl.aspx', '@submitClass': 'submit_xml', '@uiType': 'form',
                   '@multi': 'false', '@submitImageUrl': '/images/submit/submit.png', '@errorUrl': '/xmlerror_print.json', 'property': [
            {'@question': 'Hotel Name', '@prpid': '1360', '@multi': 'false', 'answers': {'answer': {'@valueId': '13383134',
                                                                                                    'part': {'@v_minlength': '2', '@v_maxlength': '100', '@v_required': 'true',
                                                                                                             '@class': 'CSS_150', '@type': 'text', '@order': '3',
                                                                                                             '#text': 'JA Hatta Fort Hotel'}}}},
            {'@question': 'star rating', '@prpid': '1361', '@multi': 'false',
             'answers': {'answer': {'@valueId': '13383135', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true', '#text': '4'}}}},
            {'@question': 'Accommodation', '@prpid': '73571', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=73571', '@value': '0'}}}},
            {'@question': 'Accommodation', '@prpid': '2675', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@class': 'CSS_137', '@type': 'select', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2675', '@value': '0'}}}},
            {'@question': 'view', '@prpid': '1375', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@class': 'CSS_137', '@type': 'select', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1375', '@value': '0'}}}},
            {'@question': 'location', '@prpid': '1364', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                                  'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                           '@type': 'checkList', '@order': '3',
                                                                                                           '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1364', '@value': '0'}}}},
            {'@question': 'Number of Rooms', '@prpid': '1365', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'number of floors', '@prpid': '1366', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'facilities', '@prpid': '1367', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1367', '@value': '0'}}}},
            {'@question': 'room type', '@prpid': '73584', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=73584', '@value': '0'}}}},
            {'@question': 'room type', '@prpid': '73572', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=73572', '@value': '0'}}}},
            {'@question': 'room facilities', '@prpid': '1369', '@multi': 'false', 'answers': {'answer': [
                {'@valueId': '13383136', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1369', '@value': '155850'}},
                {'@valueId': '13383148', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1369', '@value': '155850'}}]}},
            {'@question': 'bed type', '@prpid': '73573', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=73573', '@value': '0'}}}},
            {'@question': 'facility Beach', '@prpid': '2652', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                                        'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                                 '@type': 'checkList', '@order': '3',
                                                                                                                 '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2652', '@value': '0'}}}},
            {'@question': 'Bed height', '@prpid': '73574', '@multi': 'true',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_132', '@type': 'text', '@order': '3'}}}},
            {'@question': 'internet services', '@prpid': '1368', '@multi': 'false', 'answers': {'answer': {'@valueId': '0', 'part': {'@v_minlength': '2', '@v_maxlength': '4000',
                                                                                                                                     '@class': 'CSS_140', '@type': 'checkList',
                                                                                                                                     '@order': '3',
                                                                                                                                     '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1368',
                                                                                                                                     '@value': '0'}}}},
            {'@question': 'Pillow material', '@prpid': '73575', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@class': 'CSS_137', '@type': 'select', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=73575', '@value': '0'}}}},
            {'@question': 'TV', '@prpid': '1370', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                            'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                     '@type': 'checkList', '@order': '3',
                                                                                                     '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1370', '@value': '0'}}}},
            {'@question': 'Cosmetic services', '@prpid': '73576', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=73576', '@value': '0'}}}},
            {'@question': 'Bathroom', '@prpid': '1371', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                                  'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                           '@type': 'checkList', '@order': '3',
                                                                                                           '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1371', '@value': '0'}}}},
            {'@question': 'ventilation system', '@prpid': '1372', '@multi': 'false', 'answers': {'answer': [
                {'@valueId': '13383137', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1372', '@value': '2096'}},
                {'@valueId': '13383149', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1372', '@value': '2096'}}]}},
            {'@question': 'country', '@prpid': '10000005', '@multi': 'false', 'answers': {'answer': [{'@valueId': '1002248',
                                                                                                      'part': {'@type': 'textList', '@order': '3', '@class': 'CSS_199',
                                                                                                               '@url': '/jsonsearch/jsonsearch.htm?mid2=10&Prpid=10000005&lid=2',
                                                                                                               '@text': 'United Arab Emirates', '@value': '1002248'}},
                                                                                                     {'@valueId': '1002248',
                                                                                                      'part': {'@type': 'textList', '@order': '3', '@class': 'CSS_199',
                                                                                                               '@url': '/jsonsearch/jsonsearch.htm?mid2=10&Prpid=10000005&lid=2',
                                                                                                               '@text': 'United Arab Emirates', '@value': '1002248'}},
                                                                                                     {'@valueId': '0',
                                                                                                      'part': {'@type': 'textList', '@order': '3', '@class': 'CSS_199',
                                                                                                               '@url': '/jsonsearch/jsonsearch.htm?mid2=10&Prpid=10000005&lid=2',
                                                                                                               '@text': '', '@value': '0'}}]}},
            {'@question': 'city', '@prpid': '10000006', '@multi': 'false', 'answers': {'answer': [{'@valueId': '1176288',
                                                                                                   'part': {'@type': 'textList', '@order': '3', '@class': 'CSS_199',
                                                                                                            '@url': '/jsonsearch/jsonsearch.htm?mid2=10&Prpid=10000006&lid=2',
                                                                                                            '@text': 'Hatta', '@value': '1176288'}}, {'@valueId': '1176288',
                                                                                                                                                      'part': {'@type': 'textList',
                                                                                                                                                               '@order': '3',
                                                                                                                                                               '@class': 'CSS_199',
                                                                                                                                                               '@url': '/jsonsearch/jsonsearch.htm?mid2=10&Prpid=10000006&lid=2',
                                                                                                                                                               '@text': 'Hatta',
                                                                                                                                                               '@value': '1176288'}},
                                                                                                  {'@valueId': '0',
                                                                                                   'part': {'@type': 'textList', '@order': '3', '@class': 'CSS_199',
                                                                                                            '@url': '/jsonsearch/jsonsearch.htm?mid2=10&Prpid=10000006&lid=2',
                                                                                                            '@text': '', '@value': '0'}}]}},
            {'@question': 'holding company', '@prpid': '10000011', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                                             'part': {'@type': 'textList', '@order': '3', '@class': 'CSS_199',
                                                                                                                      '@url': '/jsonsearch/jsonsearch.htm?mid2=1&Prpid=10000011&lid=2',
                                                                                                                      '@text': '', '@value': '0'}}}},
            {'@question': 'housekeeping', '@prpid': '2676', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2676', '@value': '0'}}}},
            {'@question': 'TV channels', '@prpid': '73577', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=73577', '@value': '0'}}}},
            {'@question': 'Special Features', '@prpid': '1373', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                                          'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                                   '@type': 'checkList', '@order': '3',
                                                                                                                   '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1373', '@value': '0'}}}},
            {'@question': 'parking', '@prpid': '2651', '@multi': 'false', 'answers': {'answer': [
                {'@valueId': '13383140', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2651', '@value': '2193'}},
                {'@valueId': '13383152', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2651', '@value': '2193'}}]}},
            {'@question': 'sport and entertainment', '@prpid': '1374', '@multi': 'false', 'answers': {'answer': [
                {'@valueId': '13383141', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1374', '@value': '2207'}},
                {'@valueId': '13383153', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=1374', '@value': '2207'}}]}},
            {'@question': 'shuttle', '@prpid': '2671', '@multi': 'false', 'answers': {'answer': [{'@valueId': '13383142',
                                                                                                  'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                           '@type': 'checkList', '@order': '3',
                                                                                                           '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2671', '@value': '2243'}},
                                                                                                 {'@valueId': '13383154',
                                                                                                  'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                           '@type': 'checkList', '@order': '3',
                                                                                                           '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2671', '@value': '2243'}}]}},
            {'@question': 'facilities for disabled', '@prpid': '2653', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2653', '@value': '0'}}}},
            {'@question': 'Smoking Area', '@prpid': '2657', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                                      'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                               '@type': 'checkList', '@order': '3',
                                                                                                               '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2657', '@value': '0'}}}},
            {'@question': 'breakfast service', '@prpid': '2654', '@multi': 'false', 'answers': {'answer': {'@valueId': '0', 'part': {'@v_minlength': '2', '@v_maxlength': '4000',
                                                                                                                                     '@class': 'CSS_140', '@type': 'checkList',
                                                                                                                                     '@order': '3',
                                                                                                                                     '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2654',
                                                                                                                                     '@value': '0'}}}},
            {'@question': 'Lunch service', '@prpid': '2655', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                                       'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                                '@type': 'checkList', '@order': '3',
                                                                                                                '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2655', '@value': '0'}}}},
            {'@question': 'dinner service', '@prpid': '2656', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                                        'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                                 '@type': 'checkList', '@order': '3',
                                                                                                                 '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2656', '@value': '0'}}}},
            {'@question': 'year built', '@prpid': '2659', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@class': 'CSS_136', '@type': 'text', '@order': '3'}}}},
            {'@question': 'number of buildings/towers', '@prpid': '2658', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'number of resturantS', '@prpid': '2660', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'number of outdoor pools', '@prpid': '2661', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'number of indoor pools', '@prpid': '2662', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'number of bars', '@prpid': '2663', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'number of meeting room', '@prpid': '2664', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'meeting facilites size', '@prpid': '2665', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_128', '@type': 'text', '@order': '3'}}}},
            {'@question': 'pet maximum weight', '@prpid': '2666', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_131', '@type': 'text', '@order': '2', '@v_number': 'true'}}}},
            {'@question': 'Number of coffee shops', '@prpid': '73578', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'Maximum number of pets per room', '@prpid': '2667', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'number of Conference hall', '@prpid': '73579', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'check in', '@prpid': '1376', '@multi': 'true',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_minlength': '5', '@v_maxlength': '8', '@class': 'CSS_166', '@type': 'text', '@order': '3'}}}},
            {'@question': 'check out', '@prpid': '1377', '@multi': 'true', 'answers': {'answer': {'@valueId': '0', 'part': {'@class': 'CSS_166', '@type': 'text', '@order': '3'}}}},
            {'@question': 'Minimum check-in age is', '@prpid': '2672', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_min': '1', '@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'Room Dimensions', '@prpid': '73580', '@multi': 'true',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_132', '@type': 'text', '@order': '3'}}}},
            {'@question': 'payment type', '@prpid': '2668', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                                      'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_140',
                                                                                                               '@type': 'checkList', '@order': '3',
                                                                                                               '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2668', '@value': '0'}}}},
            {'@question': 'accessible Debit cards', '@prpid': '2669', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=2669', '@value': '0'}}}},
            {'@question': 'GPS', '@prpid': '1378', '@multi': 'false', 'answers': {'answer': {'@valueId': '0',
                                                                                             'part': [{'@class': 'CSS_250', '@type': 'text', '@order': '4', '@caption': ''},
                                                                                                      {'@v_maxlength': '4000', '@class': 'CSS_250', '@type': 'text', '@order': '3',
                                                                                                       '@caption': ''}]}}},
            {'@question': 'Number of pool bar', '@prpid': '73581', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'Address', '@prpid': '1379', '@multi': 'false',
             'answers': {'answer': {'@valueId': '13383143', 'part': {'@class': 'css_244', '@type': 'largeText', '@order': '3', '#text': 'Dubai-Hatta Road/P.O. Box 9277/Hatta'}}}},
            {'@question': 'Number of tennis court', '@prpid': '73582', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@class': 'css_130', '@type': 'text', '@order': '1', '@v_number': 'true'}}}},
            {'@question': 'Postal Code', '@prpid': '2673', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_128', '@type': 'text', '@order': '3'}}}},
            {'@question': 'Phone', '@prpid': '1380', '@multi': 'true', 'answers': {'answer': [
                {'@valueId': '13383144', 'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'css_241', '@type': 'text', '@order': '3', '#text': '+97148099333'}},
                {'@valueId': '13383155', 'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'css_241', '@type': 'text', '@order': '3', '#text': '+97148099333'}}]}},
            {'@question': 'Fax', '@prpid': '1381', '@multi': 'false', 'answers': {'answer': {'@valueId': '13383145',
                                                                                             'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'css_241',
                                                                                                      '@type': 'text', '@order': '3', '#text': '+97148523561'}}}},
            {'@question': 'Website', '@prpid': '1382', '@multi': 'false', 'answers': {'answer': {'@valueId': '13383146',
                                                                                                 'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_250',
                                                                                                          '@type': 'text', '@order': '3',
                                                                                                          '#text': 'https://www.jaresortshotels.com/propertyoverview/dubai/ja-hatta-fort-hotel'}}}},
            {'@question': 'Email', '@prpid': '1383', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_minlength': '2', '@v_maxlength': '4000', '@class': 'CSS_250', '@type': 'text', '@order': '3'}}}},
            {'@question': 'Voltage', '@prpid': '73583', '@multi': 'false', 'answers': {
                'answer': {'@valueId': '0', 'part': {'@class': 'CSS_140', '@type': 'checkList', '@order': '3', '@url': '/PrpfixUrl.aspx?Lid=2&Prpid=73583', '@value': '0'}}}},
            {'@question': 'Original Photo', '@prpid': '54283', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@v_minlength': '10', '@v_maxlength': '1000', '@class': 'CSS_159', '@type': 'text', '@order': '3'}}}},
            {'@question': 'Description', '@prpid': '7305', '@multi': 'false',
             'answers': {'answer': {'@valueId': '0', 'part': {'@class': 'CSS_144', '@type': 'text', '@order': '4'}}}}, {'@question': 'GIATA', '@prpid': '73547', '@multi': 'false',
                                                                                                                        'answers': {'answer': {'@valueId': '13383147',
                                                                                                                                               'part': {'@v_min': '1',
                                                                                                                                                        '@class': 'css_130',
                                                                                                                                                        '@type': 'text',
                                                                                                                                                        '@order': '1',
                                                                                                                                                        '@v_number': 'true',
                                                                                                                                                        '#text': '13829'}}}}]}}}
# try:
update_data = {'Hotel Name': 'Sheraton Hotel Tirana', 'Address': 'Sheshi Italia', 'Phone': '003554274707', 'Fax': ' 355 4 227 4711', 'Email': 'RESERVATION.TIRANA@SHERATON.COM',
               'Description': 'Right next to Heathrow Airport and just off the A4 road, this Premier Inn features modern rooms, a 24-hour front desk, and a Costa Coffee shop. Heathrow Terminal 5 is just 1 mile away and parking is available.\n\nEvery bright room at Premier Inn Heathrow Airport Terminal 5 includes cosy Hypnos beds and a modern private bathroom and hairdryer. Guests can relax in their room with a flat-screen TV and free tea and coffee.\n\nThe M25 motorway is just 3 minutes’ drive away, and the M4 is 5 minutes away by car. Heathrow Airport Terminal 5 Rail Station is also a 5-minute drive away, and Longford Village is less than half a mile from the Premier Inn.\n\nThe Thyme Restaurant serves an extensive menu with a variety of cuisine which guests can also enjoy in the outdoor eating area. Guests can also relax with a drink at the bar.\n\nNewspapers.Restaurant, Bar.24-hour front desk, Luggage storage, Airport shuttle.Non-smoking rooms, Family rooms, Lift/elevator, Heating, Non-smoking throughout, Air conditioning.',
               'GIATA': 54579, 'star rating': 6, 'hotel facilities': [2369.0, 12923.0, 155815.0], 'internet services': [2076.0],
               'room facilities': [2082.0, 2085.0, 144234.0, 2291.0, 12983.0, 2201.0, 155931.0], 'TV': [2088.0, 2087.0], 'Bathroom': [2091.0, 2094.0],
               'ventilation system': [2096.0], 'Special Features': [2098.0], 'sport and entertainment': [2104.0, 2120.0, 2125.0, 2119.0], 'bed type': [155701.0],
               'Voltage': [155753.0], 'city': {'title': 'Tirana', 'id': 1190087.0}, 'country': {'title': 'Albania', 'id': 1002040.0}}
null_question = []
field_name_list = [item for item in update_data]
removed_property_index = []
for K, properties_list in my_dict.items():
    for x in range(0, len(properties_list['properties']['property'])):
        if type(properties_list['properties']['property'][x]['answers']['answer']) == list:
            for i in properties_list['properties']['property'][x]['answers']['answer']:
                if i['@valueId'] != '0':
                    null_question.append(x)
        else:
            if properties_list['properties']['property'][x]['answers']['answer']['@valueId'] != '0':
                null_question.append(x)

my_dict['root']['properties']['property'] = [item for index, item in enumerate(my_dict['root']['properties']['property']) if index not in null_question]

field_name_list = [item for item in update_data]
removed_property_index = []

for root, properties_list in my_dict.items():
    for property_index in range(0, len(properties_list['properties']['property'])):
        for key, value in update_data.items():
            if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is not list and type(value) is not dict and type(value) is not tuple:
                properties_list['properties']['property'][property_index]['answers']['answer']['part']['#text'] = str(value)
            if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is list:
                new_answer = []
                for i in value:
                    answer = properties_list['properties']['property'][property_index]['answers']['answer']
                    ans = copy.deepcopy(answer)
                    ans['part']['@value'] = str(int(i))
                    new_answer.append(ans)

                properties_list['properties']['property'][property_index]['answers']['answer'] = new_answer
            if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is dict:
                properties_list['properties']['property'][property_index]['answers']['answer']['part']['@text'] = value['title']
                properties_list['properties']['property'][property_index]['answers']['answer']['part']['@value'] = str(int(value['id']))

            if key == properties_list['properties']['property'][property_index]['@question'] and type(value) is tuple:
                properties_list['properties']['property'][property_index]['answers']['answer']['part'][0]['#text'] = str(value[0])
                properties_list['properties']['property'][property_index]['answers']['answer']['part'][1]['#text'] = str(value[1])

        if properties_list['properties']['property'][property_index]['@question'] not in field_name_list:
            removed_property_index.append(property_index)

my_dict['root']['properties']['property'] = [item for index, item in enumerate(my_dict['root']['properties']['property']) if index not in removed_property_index]

print(my_dict)
