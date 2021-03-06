# Description: Transforms a string into a string with special tokens for specific types of named entities.
# Input: Any string.
# Output: The input string, with the below types of named entity substrings replaced by special tokens (<expression type>: "<token>").
# - Times: "TIME"
# - Dates: "DATE"
# - Email addresses: "EMAIL_ADDRESS"
# - Web addresses: "WEB_ADDRESS"
# - Dollar amounts: "DOLLAR_AMOUNT"
#
# Sample input => output: “she spent $149.99 and bought a nice microphone from www.bestdevices.com yesterday” => “she spent DOLLAR_AMOUNT and bought a nice microphone from WEB_ADDRESS DATE”

import re

def ner(input_string):
    output_string = input_string
    
    times = ['\d\d:\d\d:\d\d( AM)?( PM)?',
             '\d\d? [AP]M',
             "\d\d? o'clock",
             '[Ff]ive past [a-z]+',
             '[Tt]en past [a-z]+',
             '[Qq]uarter past [a-z]+',
             '[Tt]wenty past [a-z]+',
             '[Tt]wenty-five past [a-z]+',
             '[Hh]alf past [a-z]+',
             '[Tt]wenty-five to [a-z]+',
             '[Tt]wenty to [a-z]+',
             '[Qq]uarter to [a-z]+',
             '[Tt]en to [a-z]+',
             '[Ff]ive to [a-z]+']
    dates = ['Mon\.|Tue\.|Wed\.|Thu\.|Fri\.|Sat\.|Sun\.',
             'Mondays?|Tuesdays?|Wednesdays?|Thursdays?|Fridays?|Saturdays?|Sundays?',
             '[Tt]oday', '[Yy]esterday', '[Tt]omorrow',
             '[Tt]he day before yesterday', '[Tt]he day after tomorrow',
             '\d\d\d\d[-/]\d\d[-/]\d\d',
             '\d\d[-/]\d\d[-/]\d\d\d\d',
             '\d\d[-/]\d\d[-/]\d\d',
             '\d\d[-/]\d\d',
             'January \d\d?, \d\d\d\d',
             'February \d\d?, \d\d\d\d',
             'March \d\d?, \d\d\d\d',
             'April \d\d?, \d\d\d\d',
             'May \d\d?, \d\d\d\d',
             'June \d\d?, \d\d\d\d',
             'July \d\d?, \d\d\d\d',
             'August \d\d?, \d\d\d\d',
             'September \d\d?, \d\d\d\d',
             'October \d\d?, \d\d\d\d',
             'November \d\d?, \d\d\d\d',
             'December \d\d?, \d\d\d\d',
             'Jan\. \d\d?, \d\d\d\d',
             'Feb\. \d\d?, \d\d\d\d',
             'Mar\. \d\d?, \d\d\d\d',
             'Apr\. \d\d?, \d\d\d\d',
             'Jun\. \d\d?, \d\d\d\d',
             'Jul\. \d\d?, \d\d\d\d',
             'Aug\. \d\d?, \d\d\d\d',
             'Sep\. \d\d?, \d\d\d\d',
             'Sept\. \d\d?, \d\d\d\d',
             'Oct\. \d\d?, \d\d\d\d',
             'Nov\. \d\d?, \d\d\d\d',
             'Dec\. \d\d?, \d\d\d\d']
    emails = ['\S+@\S+']
    webs = ['www\.\S+',
            'https?://\S+'
            '\S+\.com',
            '\S+\.org',
            '\S+\.net',
            '\S+\.int',
            '\S+\.edu',
            '\S+\.gov',
            '\S+\.mil',
            '\S+\.arpa',
            '\S+\.ac',
            '\S+\.ad',
            '\S+\.ae',
            '\S+\.af',
            '\S+\.ag',
            '\S+\.ai',
            '\S+\.al',
            '\S+\.am',
            '\S+\.ao',
            '\S+\.aq',
            '\S+\.ar',
            '\S+\.as',
            '\S+\.at',
            '\S+\.au',
            '\S+\.aw',
            '\S+\.ax',
            '\S+\.az',
            '\S+\.ba',
            '\S+\.bb',
            '\S+\.bd',
            '\S+\.be',
            '\S+\.bf',
            '\S+\.bg',
            '\S+\.bh',
            '\S+\.bi',
            '\S+\.bj',
            '\S+\.bm',
            '\S+\.bn',
            '\S+\.bo',
            '\S+\.bq',
            '\S+\.br',
            '\S+\.bs',
            '\S+\.bt',
            '\S+\.bw',
            '\S+\.by',
            '\S+\.bz',
            '\S+\.ca',
            '\S+\.cc',
            '\S+\.cd',
            '\S+\.cf',
            '\S+\.cg',
            '\S+\.ch',
            '\S+\.ci',
            '\S+\.ck',
            '\S+\.cl',
            '\S+\.cm',
            '\S+\.cn',
            '\S+\.co',
            '\S+\.cr',
            '\S+\.cu',
            '\S+\.cv',
            '\S+\.cw',
            '\S+\.cx',
            '\S+\.cy',
            '\S+\.cz',
            '\S+\.de',
            '\S+\.dj',
            '\S+\.dk',
            '\S+\.dm',
            '\S+\.do',
            '\S+\.dz',
            '\S+\.ec',
            '\S+\.ee',
            '\S+\.eg',
            '\S+\.eh',
            '\S+\.er',
            '\S+\.es',
            '\S+\.et',
            '\S+\.eu',
            '\S+\.fi',
            '\S+\.fj',
            '\S+\.fk',
            '\S+\.fm',
            '\S+\.fo',
            '\S+\.fr',
            '\S+\.ga',
            '\S+\.gd',
            '\S+\.ge',
            '\S+\.gf',
            '\S+\.gg',
            '\S+\.gh',
            '\S+\.gi',
            '\S+\.gl',
            '\S+\.gm',
            '\S+\.gn',
            '\S+\.gp',
            '\S+\.gq',
            '\S+\.gr',
            '\S+\.gs',
            '\S+\.gt',
            '\S+\.gu',
            '\S+\.gw',
            '\S+\.gy',
            '\S+\.hk',
            '\S+\.hm',
            '\S+\.hn',
            '\S+\.hr',
            '\S+\.ht',
            '\S+\.hu',
            '\S+\.id',
            '\S+\.ie',
            '\S+\.il',
            '\S+\.im',
            '\S+\.in',
            '\S+\.io',
            '\S+\.iq',
            '\S+\.ir',
            '\S+\.is',
            '\S+\.it',
            '\S+\.je',
            '\S+\.jm',
            '\S+\.jo',
            '\S+\.jp',
            '\S+\.ke',
            '\S+\.kg',
            '\S+\.kh',
            '\S+\.ki',
            '\S+\.km',
            '\S+\.kn',
            '\S+\.kp',
            '\S+\.kr',
            '\S+\.kw',
            '\S+\.ky',
            '\S+\.kz',
            '\S+\.la',
            '\S+\.lb',
            '\S+\.lc',
            '\S+\.li',
            '\S+\.lk',
            '\S+\.lr',
            '\S+\.ls',
            '\S+\.lt',
            '\S+\.lu',
            '\S+\.lv',
            '\S+\.ly',
            '\S+\.ma',
            '\S+\.mc',
            '\S+\.md',
            '\S+\.me',
            '\S+\.mg',
            '\S+\.mh',
            '\S+\.mk',
            '\S+\.ml',
            '\S+\.mm',
            '\S+\.mn',
            '\S+\.mo',
            '\S+\.mp',
            '\S+\.mq',
            '\S+\.mr',
            '\S+\.ms',
            '\S+\.mt',
            '\S+\.mu',
            '\S+\.mv',
            '\S+\.mw',
            '\S+\.mx',
            '\S+\.my',
            '\S+\.mz',
            '\S+\.na',
            '\S+\.nc',
            '\S+\.ne',
            '\S+\.nf',
            '\S+\.ng',
            '\S+\.ni',
            '\S+\.nl',
            '\S+\.no',
            '\S+\.np',
            '\S+\.nr',
            '\S+\.nu',
            '\S+\.nz',
            '\S+\.om',
            '\S+\.pa',
            '\S+\.pe',
            '\S+\.pf',
            '\S+\.pg',
            '\S+\.ph',
            '\S+\.pk',
            '\S+\.pl',
            '\S+\.pm',
            '\S+\.pn',
            '\S+\.pr',
            '\S+\.ps',
            '\S+\.pt',
            '\S+\.pw',
            '\S+\.py',
            '\S+\.qa',
            '\S+\.re',
            '\S+\.ro',
            '\S+\.rs',
            '\S+\.ru',
            '\S+\.rw',
            '\S+\.sa',
            '\S+\.sb',
            '\S+\.sc',
            '\S+\.sd',
            '\S+\.se',
            '\S+\.sg',
            '\S+\.sh',
            '\S+\.si',
            '\S+\.sk',
            '\S+\.sl',
            '\S+\.sm',
            '\S+\.sn',
            '\S+\.so',
            '\S+\.sr',
            '\S+\.ss',
            '\S+\.st',
            '\S+\.su',
            '\S+\.sv',
            '\S+\.sx',
            '\S+\.sy',
            '\S+\.sz',
            '\S+\.tc',
            '\S+\.td',
            '\S+\.tf',
            '\S+\.tg',
            '\S+\.th',
            '\S+\.tj',
            '\S+\.tk',
            '\S+\.tl',
            '\S+\.tm',
            '\S+\.tn',
            '\S+\.to',
            '\S+\.tr',
            '\S+\.tt',
            '\S+\.tv',
            '\S+\.tw',
            '\S+\.tz',
            '\S+\.ua',
            '\S+\.ug',
            '\S+\.uk',
            '\S+\.us',
            '\S+\.uy',
            '\S+\.uz',
            '\S+\.va',
            '\S+\.vc',
            '\S+\.ve',
            '\S+\.vg',
            '\S+\.vi',
            '\S+\.vn',
            '\S+\.vu',
            '\S+\.wf',
            '\S+\.ws',
            '\S+\.ye',
            '\S+\.yt',
            '\S+\.za',
            '\S+\.zm',
            '\S+\.zw',
            '\S+\.academy',
            '\S+\.accountant',
            '\S+\.accountants',
            '\S+\.active',
            '\S+\.actor',
            '\S+\.ads',
            '\S+\.adult',
            '\S+\.aero',
            '\S+\.africa',
            '\S+\.agency',
            '\S+\.airforce',
            '\S+\.amazon',
            '\S+\.analytics',
            '\S+\.apartments',
            '\S+\.app',
            '\S+\.apple',
            '\S+\.archi',
            '\S+\.army',
            '\S+\.art',
            '\S+\.associates',
            '\S+\.attorney',
            '\S+\.auction',
            '\S+\.audible',
            '\S+\.audio',
            '\S+\.author',
            '\S+\.auto',
            '\S+\.autos',
            '\S+\.aws',
            '\S+\.baby',
            '\S+\.band',
            '\S+\.bank',
            '\S+\.bar',
            '\S+\.barefoot',
            '\S+\.bargains',
            '\S+\.baseball',
            '\S+\.basketball',
            '\S+\.beauty',
            '\S+\.beer',
            '\S+\.best',
            '\S+\.bestbuy',
            '\S+\.bet',
            '\S+\.bible',
            '\S+\.bid',
            '\S+\.bike',
            '\S+\.bingo',
            '\S+\.bio',
            '\S+\.biz',
            '\S+\.black',
            '\S+\.blackfriday',
            '\S+\.blockbuster',
            '\S+\.blog',
            '\S+\.blue',
            '\S+\.boo',
            '\S+\.book',
            '\S+\.boots',
            '\S+\.bot',
            '\S+\.boutique',
            '\S+\.box',
            '\S+\.broadway',
            '\S+\.broker',
            '\S+\.build',
            '\S+\.builders',
            '\S+\.business',
            '\S+\.buy',
            '\S+\.buzz',
            '\S+\.cab',
            '\S+\.cafe',
            '\S+\.call',
            '\S+\.cam',
            '\S+\.camera',
            '\S+\.camp',
            '\S+\.cancerresearch',
            '\S+\.capital',
            '\S+\.car',
            '\S+\.cards',
            '\S+\.care',
            '\S+\.career',
            '\S+\.careers',
            '\S+\.cars',
            '\S+\.case',
            '\S+\.cash',
            '\S+\.casino',
            '\S+\.catering',
            '\S+\.catholic',
            '\S+\.center',
            '\S+\.cern',
            '\S+\.ceo',
            '\S+\.cfd',
            '\S+\.channel',
            '\S+\.chat',
            '\S+\.cheap',
            '\S+\.christmas',
            '\S+\.church',
            '\S+\.circle',
            '\S+\.city',
            '\S+\.claims',
            '\S+\.cleaning',
            '\S+\.click',
            '\S+\.clinic',
            '\S+\.clothing',
            '\S+\.cloud',
            '\S+\.club',
            '\S+\.coach',
            '\S+\.codes',
            '\S+\.coffee',
            '\S+\.college',
            '\S+\.community',
            '\S+\.company',
            '\S+\.compare',
            '\S+\.computer',
            '\S+\.condos',
            '\S+\.construction',
            '\S+\.consulting',
            '\S+\.contact',
            '\S+\.contractors',
            '\S+\.cooking',
            '\S+\.cool',
            '\S+\.coop',
            '\S+\.country',
            '\S+\.coupon',
            '\S+\.coupons',
            '\S+\.courses',
            '\S+\.credit',
            '\S+\.creditcard',
            '\S+\.cruise',
            '\S+\.cricket',
            '\S+\.cruises',
            '\S+\.dad',
            '\S+\.dance',
            '\S+\.data',
            '\S+\.date',
            '\S+\.dating',
            '\S+\.day',
            '\S+\.deal',
            '\S+\.deals',
            '\S+\.degree',
            '\S+\.delivery',
            '\S+\.democrat',
            '\S+\.dental',
            '\S+\.dentist',
            '\S+\.design',
            '\S+\.dev',
            '\S+\.diamonds',
            '\S+\.diet',
            '\S+\.digital',
            '\S+\.direct',
            '\S+\.directory',
            '\S+\.discount',
            '\S+\.diy',
            '\S+\.docs',
            '\S+\.doctor',
            '\S+\.dog',
            '\S+\.domains',
            '\S+\.dot',
            '\S+\.download',
            '\S+\.drive',
            '\S+\.duck',
            '\S+\.earth',
            '\S+\.eat',
            '\S+\.eco',
            '\S+\.education',
            '\S+\.email',
            '\S+\.energy',
            '\S+\.engineer',
            '\S+\.engineering',
            '\S+\.edeka',
            '\S+\.enterprises',
            '\S+\.equipment',
            '\S+\.esq',
            '\S+\.estate',
            '\S+\.events',
            '\S+\.exchange',
            '\S+\.expert',
            '\S+\.exposed',
            '\S+\.express',
            '\S+\.fail',
            '\S+\.faith',
            '\S+\.family',
            '\S+\.fan',
            '\S+\.fans',
            '\S+\.farm',
            '\S+\.fashion',
            '\S+\.fast',
            '\S+\.feedback',
            '\S+\.film',
            '\S+\.final',
            '\S+\.finance',
            '\S+\.financial',
            '\S+\.fire',
            '\S+\.fish',
            '\S+\.fishing',
            '\S+\.fit',
            '\S+\.fitness',
            '\S+\.flights',
            '\S+\.florist',
            '\S+\.flowers',
            '\S+\.fly',
            '\S+\.foo',
            '\S+\.food',
            '\S+\.foodnetwork',
            '\S+\.football',
            '\S+\.forsale',
            '\S+\.forum',
            '\S+\.foundation',
            '\S+\.free',
            '\S+\.frontdoor',
            '\S+\.fun',
            '\S+\.fund',
            '\S+\.furniture',
            '\S+\.futbol',
            '\S+\.fyi',
            '\S+\.gallery',
            '\S+\.game',
            '\S+\.games',
            '\S+\.garden',
            '\S+\.gay',
            '\S+\.gdn',
            '\S+\.gift',
            '\S+\.gifts',
            '\S+\.gives',
            '\S+\.glass',
            '\S+\.gle',
            '\S+\.global',
            '\S+\.gold',
            '\S+\.golf',
            '\S+\.google',
            '\S+\.gop',
            '\S+\.graphics',
            '\S+\.green',
            '\S+\.gripe',
            '\S+\.grocery',
            '\S+\.group',
            '\S+\.guide',
            '\S+\.guitars',
            '\S+\.guru',
            '\S+\.hair',
            '\S+\.hangout',
            '\S+\.health',
            '\S+\.healthcare',
            '\S+\.help',
            '\S+\.here',
            '\S+\.hiphop',
            '\S+\.hiv',
            '\S+\.hockey',
            '\S+\.holdings',
            '\S+\.holiday',
            '\S+\.homegoods',
            '\S+\.homes',
            '\S+\.homesense',
            '\S+\.horse',
            '\S+\.hospital',
            '\S+\.host',
            '\S+\.hosting',
            '\S+\.hot',
            '\S+\.hotels',
            '\S+\.house',
            '\S+\.how',
            '\S+\.ice',
            '\S+\.icu',
            '\S+\.industries',
            '\S+\.info',
            '\S+\.ing',
            '\S+\.ink',
            '\S+\.institute[88]',
            '\S+\.insurance',
            '\S+\.insure',
            '\S+\.international',
            '\S+\.investments',
            '\S+\.jewelry',
            '\S+\.jobs',
            '\S+\.joy',
            '\S+\.kim',
            '\S+\.kitchen',
            '\S+\.land',
            '\S+\.lat',
            '\S+\.law',
            '\S+\.lawyer',
            '\S+\.lease',
            '\S+\.legal',
            '\S+\.lgbt',
            '\S+\.life',
            '\S+\.lifeinsurance',
            '\S+\.lighting',
            '\S+\.like',
            '\S+\.limited',
            '\S+\.limo',
            '\S+\.link',
            '\S+\.live',
            '\S+\.living',
            '\S+\.loan',
            '\S+\.loans',
            '\S+\.locker',
            '\S+\.lol',
            '\S+\.lotto',
            '\S+\.love',
            '\S+\.ltd',
            '\S+\.luxury',
            '\S+\.makeup',
            '\S+\.management',
            '\S+\.map',
            '\S+\.market',
            '\S+\.marketing',
            '\S+\.markets',
            '\S+\.mba',
            '\S+\.med',
            '\S+\.media',
            '\S+\.meet',
            '\S+\.meme',
            '\S+\.memorial',
            '\S+\.men',
            '\S+\.menu',
            '\S+\.mint',
            '\S+\.mobi',
            '\S+\.mobile',
            '\S+\.mobily',
            '\S+\.moe',
            '\S+\.mom',
            '\S+\.money',
            '\S+\.monster',
            '\S+\.mortgage',
            '\S+\.motorcycles',
            '\S+\.mov',
            '\S+\.movie',
            '\S+\.museum',
            '\S+\.music',
            '\S+\.name',
            '\S+\.navy',
            '\S+\.network',
            '\S+\.new',
            '\S+\.news',
            '\S+\.ngo',
            '\S+\.ninja',
            '\S+\.now',
            '\S+\.ntt',
            '\S+\.observer',
            '\S+\.off',
            '\S+\.one',
            '\S+\.ong',
            '\S+\.onl',
            '\S+\.online',
            '\S+\.ooo',
            '\S+\.open',
            '\S+\.organic',
            '\S+\.origins',
            '\S+\.page',
            '\S+\.partners',
            '\S+\.parts',
            '\S+\.party',
            '\S+\.pay',
            '\S+\.pet',
            '\S+\.pharmacy',
            '\S+\.phone',
            '\S+\.photo',
            '\S+\.photography',
            '\S+\.photos',
            '\S+\.physio',
            '\S+\.pics',
            '\S+\.pictures',
            '\S+\.pid',
            '\S+\.pin',
            '\S+\.pink',
            '\S+\.pizza',
            '\S+\.place',
            '\S+\.plumbing',
            '\S+\.plus',
            '\S+\.poker',
            '\S+\.porn',
            '\S+\.post',
            '\S+\.press',
            '\S+\.prime',
            '\S+\.pro',
            '\S+\.productions',
            '\S+\.prof',
            '\S+\.promo',
            '\S+\.properties',
            '\S+\.property',
            '\S+\.protection',
            '\S+\.pub',
            '\S+\.qpon',
            '\S+\.racing',
            '\S+\.radio',
            '\S+\.read',
            '\S+\.realestate',
            '\S+\.realtor',
            '\S+\.realty',
            '\S+\.recipes',
            '\S+\.red',
            '\S+\.rehab',
            '\S+\.reit',
            '\S+\.rent',
            '\S+\.rentals',
            '\S+\.repair',
            '\S+\.report',
            '\S+\.republican',
            '\S+\.rest',
            '\S+\.restaurant',
            '\S+\.review',
            '\S+\.reviews',
            '\S+\.rich',
            '\S+\.rip',
            '\S+\.rocks',
            '\S+\.rodeo',
            '\S+\.room',
            '\S+\.rugby',
            '\S+\.run',
            '\S+\.safe',
            '\S+\.sale',
            '\S+\.save',
            '\S+\.sbi',
            '\S+\.scholarships',
            '\S+\.school',
            '\S+\.science',
            '\S+\.search',
            '\S+\.secure',
            '\S+\.security',
            '\S+\.select',
            '\S+\.services',
            '\S+\.sex',
            '\S+\.sexy',
            '\S+\.shoes',
            '\S+\.shop',
            '\S+\.shopping',
            '\S+\.show',
            '\S+\.showtime',
            '\S+\.silk',
            '\S+\.singles',
            '\S+\.site',
            '\S+\.ski',
            '\S+\.skin',
            '\S+\.sky',
            '\S+\.sling',
            '\S+\.smile',
            '\S+\.sncf',
            '\S+\.soccer',
            '\S+\.social',
            '\S+\.software',
            '\S+\.solar',
            '\S+\.solutions',
            '\S+\.song',
            '\S+\.space',
            '\S+\.spot',
            '\S+\.spreadbetting',
            '\S+\.storage',
            '\S+\.store',
            '\S+\.stream',
            '\S+\.studio',
            '\S+\.study',
            '\S+\.style',
            '\S+\.sucks',
            '\S+\.supplies',
            '\S+\.supply',
            '\S+\.support',
            '\S+\.surf',
            '\S+\.surgery',
            '\S+\.systems',
            '\S+\.talk',
            '\S+\.tattoo',
            '\S+\.tax',
            '\S+\.taxi',
            '\S+\.team',
            '\S+\.tech',
            '\S+\.technology',
            '\S+\.tel',
            '\S+\.tennis',
            '\S+\.theater',
            '\S+\.theatre',
            '\S+\.tickets',
            '\S+\.tips',
            '\S+\.tires',
            '\S+\.today',
            '\S+\.tools',
            '\S+\.top',
            '\S+\.tours',
            '\S+\.town',
            '\S+\.toys',
            '\S+\.trade',
            '\S+\.trading',
            '\S+\.training',
            '\S+\.travel',
            '\S+\.travelersinsurance',
            '\S+\.trust',
            '\S+\.tube',
            '\S+\.tunes',
            '\S+\.uconnect',
            '\S+\.university',
            '\S+\.uno',
            '\S+\.vacations',
            '\S+\.ventures',
            '\S+\.vet',
            '\S+\.video',
            '\S+\.villas',
            '\S+\.vip',
            '\S+\.vision',
            '\S+\.vodka',
            '\S+\.vote',
            '\S+\.voting',
            '\S+\.voyage',
            '\S+\.wang',
            '\S+\.watch',
            '\S+\.watches',
            '\S+\.weather',
            '\S+\.webcam',
            '\S+\.website',
            '\S+\.wed',
            '\S+\.wedding',
            '\S+\.whoswho',
            '\S+\.wiki',
            '\S+\.win',
            '\S+\.wine',
            '\S+\.winners',
            '\S+\.work',
            '\S+\.works',
            '\S+\.world',
            '\S+\.wow',
            '\S+\.wtf',
            '\S+\.xxx',
            '\S+\.xyz',
            '\S+\.yachts',
            '\S+\.yoga',
            '\S+\.you',
            '\S+\.zero',
            '\S+\.zone',
            '\S+\.ren',
            '\S+\.shouji',
            '\S+\.tushu',
            '\S+\.wanggou',
            '\S+\.weibo',
            '\S+\.xihuan',
            '\S+\.xin',
            '\S+\.arte',
            '\S+\.clinique',
            '\S+\.luxe',
            '\S+\.maison',
            '\S+\.moi',
            '\S+\.rsvp',
            '\S+\.sarl',
            '\S+\.epost',
            '\S+\.gmbh',
            '\S+\.haus',
            '\S+\.immobilien',
            '\S+\.jetzt',
            '\S+\.kaufen',
            '\S+\.kinder',
            '\S+\.reise',
            '\S+\.reisen',
            '\S+\.schule',
            '\S+\.versicherung',
            '\S+\.desi',
            '\S+\.shiksha',
            '\S+\.casa',
            '\S+\.immo',
            '\S+\.moda',
            '\S+\.voto',
            '\S+\.bom',
            '\S+\.passagens',
            '\S+\.abogado',
            '\S+\.gratis',
            '\S+\.hoteles',
            '\S+\.juegos',
            '\S+\.ltda',
            '\S+\.soy',
            '\S+\.tienda',
            '\S+\.viajes',
            '\S+\.vuelos',
            '\S+\.capetown',
            '\S+\.durban',
            '\S+\.joburg',
            '\S+\.abudhabi',
            '\S+\.arab',
            '\S+\.asia',
            '\S+\.doha',
            '\S+\.dubai',
            '\S+\.krd',
            '\S+\.kyoto',
            '\S+\.nagoya',
            '\S+\.okinawa',
            '\S+\.osaka',
            '\S+\.ryukyu',
            '\S+\.taipei',
            '\S+\.tatar',
            '\S+\.tokyo',
            '\S+\.yokohama',
            '\S+\.alsace',
            '\S+\.amsterdam',
            '\S+\.bcn',
            '\S+\.barcelona',
            '\S+\.bayern',
            '\S+\.berlin',
            '\S+\.brussels',
            '\S+\.budapest',
            '\S+\.bzh',
            '\S+\.cat',
            '\S+\.cologne',
            '\S+\.corsica',
            '\S+\.cymru',
            '\S+\.eus',
            '\S+\.frl',
            '\S+\.gal',
            '\S+\.gent',
            '\S+\.hamburg',
            '\S+\.helsinki',
            '\S+\.irish',
            '\S+\.ist',
            '\S+\.istanbul',
            '\S+\.koeln',
            '\S+\.london',
            '\S+\.madrid',
            '\S+\.moscow [ru]',
            '\S+\.nrw',
            '\S+\.paris',
            '\S+\.ruhr',
            '\S+\.saarland',
            '\S+\.scot',
            '\S+\.stockholm',
            '\S+\.swiss',
            '\S+\.tirol',
            '\S+\.vlaanderen',
            '\S+\.wales',
            '\S+\.wien',
            '\S+\.zuerich',
            '\S+\.boston',
            '\S+\.miami',
            '\S+\.nyc',
            '\S+\.quebec',
            '\S+\.vegas',
            '\S+\.kiwi',
            '\S+\.melbourne',
            '\S+\.sydney',
            '\S+\.rio',
            '\S+\.aaa',
            '\S+\.aarp',
            '\S+\.abarth',
            '\S+\.abb',
            '\S+\.abbott',
            '\S+\.abbvie',
            '\S+\.abc',
            '\S+\.accenture',
            '\S+\.aco',
            '\S+\.aeg',
            '\S+\.aetna',
            '\S+\.afl',
            '\S+\.agakhan',
            '\S+\.aig',
            '\S+\.aigo',
            '\S+\.airbus',
            '\S+\.airtel',
            '\S+\.akdn',
            '\S+\.alfaromeo',
            '\S+\.alibaba',
            '\S+\.alipay',
            '\S+\.allfinanz',
            '\S+\.allstate',
            '\S+\.ally',
            '\S+\.alstom',
            '\S+\.americanexpress',
            '\S+\.amex',
            '\S+\.amica',
            '\S+\.android',
            '\S+\.anz',
            '\S+\.aol',
            '\S+\.aquarelle',
            '\S+\.aramco',
            '\S+\.audi',
            '\S+\.auspost',
            '\S+\.axa',
            '\S+\.azure',
            '\S+\.baidu',
            '\S+\.bananarepublic',
            '\S+\.barclaycard',
            '\S+\.barclays',
            '\S+\.bauhaus',
            '\S+\.bbc',
            '\S+\.bbt',
            '\S+\.bbva',
            '\S+\.bcg',
            '\S+\.bentley',
            '\S+\.bharti',
            '\S+\.bing',
            '\S+\.blanco',
            '\S+\.bloomberg',
            '\S+\.bms',
            '\S+\.bmw',
            '\S+\.bnl',
            '\S+\.bnpparibas',
            '\S+\.boehringer',
            '\S+\.bond',
            '\S+\.booking',
            '\S+\.bosch',
            '\S+\.bostik',
            '\S+\.bradesco',
            '\S+\.bridgestone',
            '\S+\.brother',
            '\S+\.bugatti',
            '\S+\.cal',
            '\S+\.calvinklein',
            '\S+\.canon',
            '\S+\.capitalone',
            '\S+\.caravan',
            '\S+\.cartier',
            '\S+\.cba',
            '\S+\.cbn',
            '\S+\.cbre',
            '\S+\.cbs',
            '\S+\.cfa',
            '\S+\.chanel',
            '\S+\.chase',
            '\S+\.chintai',
            '\S+\.chrome',
            '\S+\.chrysler',
            '\S+\.cipriani',
            '\S+\.cisco',
            '\S+\.citadel',
            '\S+\.citi',
            '\S+\.citic',
            '\S+\.clubmed',
            '\S+\.comcast',
            '\S+\.commbank',
            '\S+\.creditunion',
            '\S+\.crown',
            '\S+\.crs',
            '\S+\.csc',
            '\S+\.cuisinella',
            '\S+\.dabur',
            '\S+\.datsun',
            '\S+\.dealer',
            '\S+\.dell',
            '\S+\.deloitte',
            '\S+\.delta',
            '\S+\.dhl',
            '\S+\.discover',
            '\S+\.dish',
            '\S+\.dnp',
            '\S+\.dodge',
            '\S+\.dunlop',
            '\S+\.dupont',
            '\S+\.dvag',
            '\S+\.emerck',
            '\S+\.epson',
            '\S+\.ericsson',
            '\S+\.erni',
            '\S+\.esurance',
            '\S+\.etisalat',
            '\S+\.eurovision',
            '\S+\.everbank',
            '\S+\.extraspace',
            '\S+\.fage',
            '\S+\.fairwinds',
            '\S+\.farmers',
            '\S+\.fedex',
            '\S+\.ferrari',
            '\S+\.ferrero',
            '\S+\.fiat',
            '\S+\.fidelity',
            '\S+\.firestone',
            '\S+\.firmdale',
            '\S+\.flickr',
            '\S+\.flir',
            '\S+\.flsmidth',
            '\S+\.ford',
            '\S+\.fox',
            '\S+\.fresenius',
            '\S+\.forex',
            '\S+\.frogans',
            '\S+\.frontier',
            '\S+\.fujitsu',
            '\S+\.fujixerox',
            '\S+\.gallo',
            '\S+\.gallup',
            '\S+\.gap',
            '\S+\.gbiz',
            '\S+\.gea',
            '\S+\.genting',
            '\S+\.giving',
            '\S+\.globo',
            '\S+\.gmail',
            '\S+\.gmo',
            '\S+\.gmx',
            '\S+\.godaddy',
            '\S+\.goldpoint',
            '\S+\.goodyear',
            '\S+\.goog',
            '\S+\.grainger',
            '\S+\.guardian',
            '\S+\.gucci',
            '\S+\.hbo',
            '\S+\.hdfc',
            '\S+\.hdfcbank',
            '\S+\.hermes',
            '\S+\.hisamitsu',
            '\S+\.hitachi',
            '\S+\.hkt',
            '\S+\.honda',
            '\S+\.honeywell',
            '\S+\.hotmail',
            '\S+\.hsbc',
            '\S+\.hughes',
            '\S+\.hyatt',
            '\S+\.hyundai',
            '\S+\.ibm',
            '\S+\.ieee',
            '\S+\.ifm',
            '\S+\.ikano',
            '\S+\.imdb',
            '\S+\.infiniti',
            '\S+\.intel',
            '\S+\.intuit',
            '\S+\.ipiranga',
            '\S+\.iselect',
            '\S+\.itau',
            '\S+\.itv',
            '\S+\.iveco',
            '\S+\.jaguar',
            '\S+\.java',
            '\S+\.jcb',
            '\S+\.jcp',
            '\S+\.jeep',
            '\S+\.jpmorgan',
            '\S+\.juniper',
            '\S+\.kddi',
            '\S+\.kerryhotels',
            '\S+\.kerrylogistics',
            '\S+\.kerryproperties',
            '\S+\.kfh',
            '\S+\.kia',
            '\S+\.kindle',
            '\S+\.komatsu',
            '\S+\.kpmg',
            '\S+\.kred',
            '\S+\.kuokgroup',
            '\S+\.lacaixa',
            '\S+\.ladbrokes',
            '\S+\.lamborghini',
            '\S+\.lancaster',
            '\S+\.lancia',
            '\S+\.lancome',
            '\S+\.landrover',
            '\S+\.lanxess',
            '\S+\.lasalle',
            '\S+\.latrobe',
            '\S+\.lds',
            '\S+\.leclerc',
            '\S+\.lego',
            '\S+\.liaison',
            '\S+\.lexus',
            '\S+\.lidl',
            '\S+\.lifestyle',
            '\S+\.lilly',
            '\S+\.lincoln',
            '\S+\.linde',
            '\S+\.lipsy',
            '\S+\.lixil',
            '\S+\.locus',
            '\S+\.lotte',
            '\S+\.lpl',
            '\S+\.lplfinancial',
            '\S+\.lundbeck',
            '\S+\.lupin',
            '\S+\.macys',
            '\S+\.maif',
            '\S+\.man',
            '\S+\.mango',
            '\S+\.marriott',
            '\S+\.maserati',
            '\S+\.mattel',
            '\S+\.mckinsey',
            '\S+\.metlife',
            '\S+\.microsoft',
            '\S+\.mini',
            '\S+\.mit',
            '\S+\.mitsubishi',
            '\S+\.mlb',
            '\S+\.mma',
            '\S+\.monash',
            '\S+\.mormon',
            '\S+\.moto',
            '\S+\.movistar',
            '\S+\.msd',
            '\S+\.mtn',
            '\S+\.mtr',
            '\S+\.mutual',
            '\S+\.nadex',
            '\S+\.nationwide',
            '\S+\.natura',
            '\S+\.nba',
            '\S+\.nec',
            '\S+\.netflix',
            '\S+\.neustar',
            '\S+\.newholland',
            '\S+\.nexus',
            '\S+\.nfl',
            '\S+\.nhk',
            '\S+\.nico',
            '\S+\.nike',
            '\S+\.nikon',
            '\S+\.nissan',
            '\S+\.nissay',
            '\S+\.nokia',
            '\S+\.northwesternmutual',
            '\S+\.norton',
            '\S+\.nra',
            '\S+\.obi',
            '\S+\.office',
            '\S+\.omega',
            '\S+\.oracle',
            '\S+\.orange',
            '\S+\.otsuka',
            '\S+\.ovh',
            '\S+\.panasonic',
            '\S+\.pccw',
            '\S+\.pfizer',
            '\S+\.philips',
            '\S+\.piaget',
            '\S+\.pictet',
            '\S+\.ping',
            '\S+\.pioneer',
            '\S+\.play',
            '\S+\.playstation',
            '\S+\.pohl',
            '\S+\.politie',
            '\S+\.praxi',
            '\S+\.prod',
            '\S+\.progressive',
            '\S+\.pru',
            '\S+\.prudential',
            '\S+\.pwc',
            '\S+\.quest',
            '\S+\.qvc',
            '\S+\.redstone',
            '\S+\.reliance',
            '\S+\.rexroth',
            '\S+\.ricoh',
            '\S+\.rmit',
            '\S+\.rocher',
            '\S+\.rogers',
            '\S+\.rwe',
            '\S+\.safety',
            '\S+\.sakura',
            '\S+\.samsung',
            '\S+\.sandvik',
            '\S+\.sandvikcoromant',
            '\S+\.sanofi',
            '\S+\.sap',
            '\S+\.saxo',
            '\S+\.sbs',
            '\S+\.sca',
            '\S+\.scb',
            '\S+\.schaeffler',
            '\S+\.schmidt',
            '\S+\.schwarz',
            '\S+\.scjohnson',
            '\S+\.scor',
            '\S+\.seat',
            '\S+\.sener',
            '\S+\.ses',
            '\S+\.sew',
            '\S+\.seven',
            '\S+\.sfr',
            '\S+\.seek',
            '\S+\.shangrila',
            '\S+\.sharp',
            '\S+\.shaw',
            '\S+\.shell',
            '\S+\.shriram',
            '\S+\.sina',
            '\S+\.skype',
            '\S+\.smart',
            '\S+\.softbank',
            '\S+\.sohu',
            '\S+\.sony',
            '\S+\.spiegel',
            '\S+\.stada',
            '\S+\.staples',
            '\S+\.star',
            '\S+\.starhub',
            '\S+\.statebank',
            '\S+\.statefarm',
            '\S+\.statoil',
            '\S+\.stc',
            '\S+\.stcgroup',
            '\S+\.suzuki',
            '\S+\.swatch',
            '\S+\.swiftcover',
            '\S+\.symantec',
            '\S+\.taobao',
            '\S+\.target',
            '\S+\.tatamotors',
            '\S+\.tdk',
            '\S+\.telecity',
            '\S+\.telefonica',
            '\S+\.temasek',
            '\S+\.teva',
            '\S+\.tiffany',
            '\S+\.tjx',
            '\S+\.toray',
            '\S+\.toshiba',
            '\S+\.total',
            '\S+\.toyota',
            '\S+\.travelchannel',
            '\S+\.travelers',
            '\S+\.tui',
            '\S+\.tvs',
            '\S+\.ubs',
            '\S+\.unicom',
            '\S+\.uol',
            '\S+\.ups',
            '\S+\.vanguard',
            '\S+\.verisign',
            '\S+\.vig',
            '\S+\.viking',
            '\S+\.virgin',
            '\S+\.visa',
            '\S+\.vista',
            '\S+\.vistaprint',
            '\S+\.vivo',
            '\S+\.volkswagen',
            '\S+\.volvo',
            '\S+\.walmart',
            '\S+\.walter',
            '\S+\.weatherchannel',
            '\S+\.weber',
            '\S+\.weir',
            '\S+\.williamhill',
            '\S+\.windows',
            '\S+\.wme',
            '\S+\.wolterskluwer',
            '\S+\.woodside',
            '\S+\.wtc',
            '\S+\.xbox',
            '\S+\.xerox',
            '\S+\.xfinity',
            '\S+\.yahoo',
            '\S+\.yamaxun',
            '\S+\.yandex',
            '\S+\.yodobashi',
            '\S+\.youtube',
            '\S+\.zappos',
            '\S+\.zara',
            '\S+\.zip',
            '\S+\.zippo',
            '\S+\.example',
            '\S+\.invalid',
            '\S+\.local',
            '\S+\.localhost',
            '\S+\.onion',
            '\S+\.test']
    dollars = ['\$\d+.\d\d', '\$\d+', '\$\d{1,3}[kKmMbB]', '\$\d{1,3} thousand',
               '\$\d{1,3} million', '\$\d{1,3} billion', '\$\d{1,3} trillion',
               '[Oo]ne.*?dollars',
               '[Tt]wo.*?dollars',
               '[Tt]hree.*?dollars',
               '[Ff]our.*?dollars',
               '[Ff]ive.*?dollars',
               '[Ss]ix.*?dollars',
               '[Ss]even.*?dollars',
               '[Ee]ight.*?dollars',
               '[Nn]ine.*?dollars',
               '[Aa] .*?dollars?',
               '[Ss]everal .*?dollars?']
    
    for elem in times:
        output_string = re.sub(elem, "TIME", output_string)
    
    for elem in dates:
        output_string = re.sub(elem, "DATE", output_string)
    
    for elem in emails:
        output_string = re.sub(elem, "EMAIL_ADDRESS", output_string)
    
    for elem in webs:
        output_string = re.sub(elem, "WEB_ADDRESS", output_string)
    
    for elem in dollars:
        output_string = re.sub(elem, "DOLLAR_AMOUNT", output_string)
    
    return output_string


if __name__ == "__main__":
    in1 = """
What time is it? It is 12:34:56 AM.
No, it is 03:12:59.
I think it is 12:12:12 PM but not sure.
It's 1 AM maybe. It's 12 AM mabye. It is 1 PM maybe. It is 11 PM maybe.
It's 9 o'clock maybe. It's 10 o'clock perhaps.
Today is Monday. Today is Tuesday. Today is Wednesday or not.
Today is Thursday. Today is Friday. Today is Saturday. Today is Sunday. 
I go gym every Mondays. I go gym every Tuesdays. I go gym every Wednesdays. I go gym every Thursdays.
I go gym every Fridays. I go gym every Saturdays maybe. Sundays are good.
Let's do this yesterday or so. Let's do this today or so. Let's do this tomorrow or so.
Yesterday was the day. Today is the day. Tomorrow is the day.
Today is 2020-09-23 which is good. Today is 2020/09/23 which is good.
Today is 09-23-2020 which is good. Today is 09/23/2020 which is good.
Today is 09-23-20 which is good. Today is 09/23/20 which is good.
Today is 09-23 or 09/23 which is good.
Send email to johnsmith@umich.edu or john_smith@gmail.com or j.markus.smith@gmail.com or your_addr@very.long.domain.io and we will do the rest.
I have nine billion dollars.
Today is Sept. 23, 2020.
"""
    print(ner(in1))