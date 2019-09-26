#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 30

writing = [
{
"id":0,
"title": "The Day I Swallowed the Sun",
"username": "saltyranchers",
"content":"the day i finally caught the sun <br>"
"between my lips <br>"
"was the day i was set free <br>"
"from the iron cage <br>"
"with its iron bars, <br>"
"that crushed my arms <br>"
"and shattered my lungs.<br>"
"i closed my eyes <br>"
"and let the golden flames <br>"
"drip down the back of my throat <br>"
"and coat my tongue like honey. <br>"
"i felt it spread through <br>"
"my chest, <br>"
"felt the thing i <br>"
"had been chasing <br>"
"for years <br>"
"and years <br>"
"and years. <br>"
"i watched as the inky blackness <br>"
"that had suffocated me <br>"
"for so many silent nights <br>"
"bled from my fingertips and <br>"
"sunk into the dirt, <br>"
"staining the daisies <br>"
"and wilting the poppies. <br>"
"a golden bead <br>"
"slipped <br>"
"down my cheek, <br>"
"and i wondered <br>"
"why my tears <br>"
"had never tasted so <br>"
"sweet. <br>"
"sitting down with the sunflowers, <br>"
"i watched the cotton candy <br>"
"clouds <br>"
"float across the baby blue sky, <br>"
"and began writing about<br>"
"the day i swallowed the sun.<br>",
"type": "poetry",
"genre": "free verse",
"feedback": ""	
},
{
"id":1,
"title": "My Summer Love",
"username": "lindzwrites",
"content":"During all of the commotion, through all of the vibrant talks of liars and lovers"
" that humid Florida summer, a combined soul blossomed from two individuals, creating a life-long memory."
" Under the plethora of a milky twilight’s sparkling stars, and the open air of a southern bay, across a path of ingrown weeds,"
" and a damp bed of trees, lay her and him. Eden-like, their bodies intertwined into a mix of desperate need, passion,"
" and the love that circled around their heads for that short glimpse of night. His breath heavy, and her eyes glossy, they were"
" watched by the constellations of destiny and that wretched fate that it would bring them in the following years. They didn’t tell"
" her about how it would feel to have a burning desire to blindly love him for eternity, never knowing where she was, or why she was"
" there, but rather that she was with him and that was it. But there he was, guiding her down a twisted and narrow forest, in the realm"
" of lust and not-so-divine intervention, leaping farther and farther away from those constellations that shone over them in the same "
"place fortnights ago, laughing and loving and pulsating in a rose glow. No, they were not sharing a piece of spongy pastel cake, or "
"swimming in the blinding salt water, or marvelling at the sky, or staying up late and conversing about the poignancy of their home distances. "
"No, because he had taken her down that hole too far. Their soul -- the one connected so long ago -- started to tug into two hearts again, "
"pleading for an escape. The chord snapped, and she was gone, and he was left sitting high up in the throne of greed, a look of contempt on "
"his face, holding her passion in safekeeping for what would feel like eternity.",
"type": "fiction",
"genre": "romance",
"feedback": ""	
},
{
"id":2,
"title": "Monster",
"username": "meago",
"content":"As I'm sitting here, in this box-shaped room, staring at my prey three feet "
"away from me, I am anxious. This child, an innocent child, will die. She is nothing to "
"me, nothing at all. When she wakes, only then will she notice my presence. She is sleeping"
" calmly, probably dreaming sweet childish fantasies of blue skies and purple unicorns "
"flying to see a magical princess. Little does she know that in a few short hours her "
"rosey red complexion will fade away to meet a dull white color. Little does she know "
"that the curls that surround her face will fade and cover a life-less dull face. Little "
"does she know of her radiant blue eyes fading with the sunset. Unlike the sun, her eyes "
"will never surface again."
"~Little does she know of the monster I am~",
"type": "fiction",
"genre": "science fiction",
"feedback": ""	
},
{
"id":3,
"title": "Grandma's Light",
"username": "blkmirror",
"content":"A fresh breeze of air wafted through the window. She was quietly sleeping on her"
" bed peaceful and untroubled as the sun came up. Her breathing was even, and her breath smelled"
" sweet like rosemary with a hint of the mint toothpaste that she brushed her teeth with the night"
" before. The birds were chirping melodiously and harmoniously and the squirrels were running around"
" the bushes with acorns in their mouths. Everything was calm. The sound of car engines driving "
"through the town in their early morning commute was a faint buzz in the distance."
"<br>"
"A sudden sense of fear ran through her nerves like the chill of an icy wind. She heard a thin"
" shrill voice next to her like the sound of an expiring mouse. She turned. Beside her, he was "
"dead a crumpled heap on the pure white snow. A tear like silver, glistened in the corner of her "
"eye but she knew she had to keep going."
"<br>"
"Soldiers were dying all around her, all she could hear was gunshots. Her gun was at the ready, "
"ready to fire and take a life away. The battle was the bloodiest she’d ever seen. However, she "
"had to keep fighting, for her family. Four years of fighting, of loss, we won, we finally won. "
"Her eyes were as bright as the day, tears streaming down her cheeks."
"Grandma! The little boy said, as a waterfall of sadness was falling from his eyes. Please don’t "
"go Grandma I love you! And then she knew, what they meant, when someone’s life passes before their "
"eyes as they die and she saw the light, bright and shining, and closed her eyes for the final time, "
"sinking it in."
"~Little does she know of the monster I am~",
"type": "fiction",
"genre": "action",
"feedback": ""	
},
{
"id":4,
"title": "Why I Write",
"username": "emly",
"content":"I write to create <br>"
"In the world’s massive novel <br>"
"A page of my own <br>",
"type": "poetry",
"genre": "haiku",
"feedback": ""	
},
{
"id":5,
"title": "Breakup Advice",
"username": "plnt22",
"content":"After those amazing relationships end, you have to ask yourself how things will continue."
" If you broke up with your partner, you must either be unhappy with them, mad at them, tired of them, "
"or some other circumstance. So, if it is you who breaks up with the other, stop and think. As one single "
"person, you don't have any idea what the other might go through. One moment to you is completely different "
"that that of another. For example, you might go on a date and have the time of your life, oblivious to that "
"fact that the one you care for is about to slit their wrists in boredom."
"Just and example."
"But that is something that you can relate to a breakup. You might think that things are better off "
"without the other. They might be tripping and falling behind you, trying to catch up and get you "
"back. It happens a lot, and these breakups are the worst. I myself went through one. And I've scraped "
"my knees so much over these past to years tripping and falling after her(yes, two years. She's so "
"beautiful I can't stop thinking about her). I've found out the the first and most important thing you "
"can do to stay out of those horrible, bad break ups, is to forget. Easier said then done, right? Well, "
"there is only one way to completely get over such a thing. Overwrite the memories that the two of you " 
"shared. Now, people call this a rebound, but isn't every boyfriend/girlfriend after the first a rebound? "
"You must make better memories with this person. Have a greater time, and think about the new things you "
"share rather then all the things you used to share with the other. Take it from me, with time, almost "
"everything is mendable.",
"type": "fiction",
"genre": "romance",
"feedback": ""	
},
{
"id":6,
"title": "Just Swinging",
"username": "ak233",
"content":"There’s something strange and magical about a swing set. As a child, I always loved to swing. "
"Nothing on the playground ever compared to the swings. Sometimes I would close my eyes and let the cool "
"breeze be my friend, seemingly helping me rise off the ground. And when I opened my eyes, I would see that "
"the swing had carried me far beyond the playground, far beyond the grove of trees along the edge of the field,"
" but I was never afraid. It was the only thing that could truly make me forget life and simultaneously make me alive."
"<br>"
"With time, though, I outgrew elementary school and moved on. By then swinging was a mere ghost of a memory and was "
"almost forgotten. Almost. The summer before high school, I revisited my old playground. Like an abandoned house, it "
"had all the nostalgic memories of a previous home, and yet, I was drawn to only the swings. If there’s something strange "
"and magical about a swing set, it’s because it’s never empty for long. The air was still as I got on, the metal chains "
"never made a sound. Slowly, as I swung, I remembered, no, embraced. I embraced the cool wind on my face, the thrill of being "
"weightless, the knowledge of being too high for any trouble to reach. And I embraced what it was like to be a child again. "
"Sometimes I can still see that teenage girl on the deserted playground. Just swinging.",
"type": "nonfiction",
"genre": "memoir",
"feedback": ""	
},
{
"id":7,
"title": "Golden Tint",
"username": "love21",
"content":"I rushed down the stairs skipping every other one. My feet up high and my hands shaking back and forth above my head. "
"It didn't matter how fast I got there or where I was going for that matter but where I am now. I was moving, soaring nearly, my feet "
"caressed the ground in a swift movement. Its for me, its for me, its for me I keep telling myself. I am almost there, so close "
"my hand could reach and grab it. The golden egg was there. The light hit it just right. It was brilliant and my dream. My dream "
"to open the edges and find my love. My love, oh my love, I would find. I began to peel back the aluminum with my tiny fragile "
"fingers. It made the most beautiful sound crinkling in my clutch. The golden tint shown off the windows into the room making the "
"kitchen appear as if magic. Bibbity- bobbity- boo and all was still for the golden tint. Oh my love, my love, my only love the "
"golden easter egg with the brilliance that makes me curious.",
"type": "nonfiction",
"genre": "memoir",
"feedback": ""	
},
{
"id":8,
"title": "Daddy's Womb",
"username": "yunggun21",
"content":"i asked my father if i could swim, <br>"
"and he said that i would drown. <br>"
"The Sea would imprison me – he said <br>"
"if my feet had left the ground.<br>"
"<br>"
"So i walked out to the water, <br>"
"and cried out – how ’bout now! <br>"
"He said, a little bit further, Son, <br>"
"and then you’ll leave the ground. <br>"
"<br>"
"i stepped on sand then stone, <br>"
"from hollow ground to sturdy. <br>"
"The sky was at my level as I <br>"
"gazed at the birdie. <br>"
"<br>"
"The Sea brought me a new idea, <br>"
"the urge to flee to the high. <br>"
"<br>"
"i asked my Father if i could fly, <br>"
"and he said, sure, Son – go try. <br>"
"<br>"
"i jumped as high as i could. <br>"
"Still, i landed on the ground. <br>"
"i saw my Father pull on a chain, <br>"
"then i knew that i was bound. <br>",
"type": "poetry",
"genre": "free verse",
"feedback": ""	
},
{
"id":9,
"title": "Who Is That...",
"username": "noair",
"content":"I shook my head and cocked it to the side. I groaned and pulled the covers over my head, only to make me feel "
"trapped and sweaty. It was too quiet..."
"<br>"
"I lifted up my head from over the covers, and I sighed when I stared across my empty bedroom. The walls seemed to be an "
"eerie blue, and my gasps came out in a hushed echo. It was only 9:00 pm. My parents were usually awake watching T.V or just "
"listening to the radio, but this night was different. I could not hear ANYTHING."
"<br>"
"Suddenly, I heard a voice that I did not recognize. The door was an inch open, but it was suddenly pushed full open, revealing "
"a long silhouette that creeped on the bedroom door. I gasped and slowly slipped under the covers, trying to be unnoticable. Then, "
"the blurry image seemed to crawl toward me, and I could finally see who this person was.",
"type": "fiction",
"genre": "thriller",
"feedback": ""	
},
{
"id":10,
"title": "Emergency",
"username": "kk214",
"content":"\"James Tyler Sanders, get out here! Now!\" A voice shouted, it echoed around the big old house, built nearly six decades ago."
"James grimaced, crouching underneath the old bed in the guest room. He sneezed from the dust, collected underneath the old bed. He then"
" clapped a hand over his mouth, wincing. Suddenly, his ankles were grabbed and he was dragged out from under the bed. The seven-year old "
"shouted in alarm, but nobody heard him."
"The boy looked at his father, tears in his eyes, he tried to struggle away, but his father’s harsh grip didn’t allow that. His father slammed the"
" back of his hand into the side of the boy’s face. “I’ll teach you not to ignore your father when he calls for you!” He shouted."
"James gasped, tears flooding his eyes. He managed to yank his arm away from his father and saw blood welling from claw marks where his father's nails "
"had been digging into his arm. He turned and ran away from his father, fear bright in his panicked, brown eyes. He slid down the banister and "
"landed at the bottom of the stairs. He heard his father thundering down the stairs behind him. He ran to the front door and fumbled with the lock "
"but his father was right behind him. He ran to the kitchen, where the nearest phone was. He heard his father getting closer, screaming profanities." 
"He looked around for the small, grey cordless phone that normally lay on the kitchen counter. He grabbed it and started to dial, 9...1...1... He went to press "
"send when his father yanked the phone from his hands and threw it away from them, it bounced off the cabinet."
"<br>"
"James reached out and grabbed the first thing he touched, a roll of tape. He threw it at his father’s face and grabbed something else and threw it "
"at his father’s face without even registering what it was, fear and adrenaline running his mind. "
"James blinked, suddenly, all he saw was red. His father stumbled a few steps towards James, his hands "
"reached out as if he were Frankenstein. He managed to clasp his large hands around James’ neck and looked him into the eyes. "
"\"You useless excuse of a-” His eyes rolled back into his head and he fell forward, crushing James against the ceramic tile floor of "
"the kitchen."
"James lay there trembling and all he could hear was the phone buzzing, the 911 operator screaming, \"Hello? Hello? Is anyone there? "
"Hello?!\"",
"type": "fiction",
"genre": "thriller",
"feedback": ""	
},
{
"id":11,
"title": "Armageddon in Autumn",
"username": "wittyboy22",
"content":"A storm of amber and gold swarms high. <br>"
"The vivid shards whip and thrash at the sky.<br>"
"And dirgesome, tall skeletons glare on me.<br>"
"The burning clouds gloat--they hiss, “We are free!”<br>"
"An army of motes, they whisper war cries,<br>"
"Like all ether’s locusts; malevolence flies.<br>"
"They stampede and plunder the squalid streets,<br>"
"Crawling o’re concrete. From feet they will feast.<br>"
"Like herds of frantic, heartless mad gophers.<br>"
"Mangled dull corpses dare to eat my loafers.<br>"
"These amber crystals we thoughtlessly laud!<br>"
"To dust returneth, fallen stars! My God.<br>"
"Droves descend from their celestine towers.<br>"
"What has Bard done, but give too much power?<br>",
"type": "poetry",
"genre": "sonnet",
"feedback": ""	
},
{
"id":12,
"title": "Vista of Moonlit Night",
"username": "myfriend22",
"content": "After every interval of a fortnight,<br>"
"The queen of night comes to address,<br>"
"To preach love and cascade light,<br>"
"The mysterious charisma; the white dress!<br>"
"<br>"
"As the moonlight embraces everything,<br>"
"The stars blush and put on veils.<br>"
"Silently, the lake keeps on smiling,<br>"
"With breeze, the perfume of night sails.<br>"
"<br>"
"The nightingale, in praise of moon,<br>"
"Begins chanting a soothing song,<br>"
"The charming vista is a boon,<br>"
"Surely, to nirvana, it belongs.<br>"
"<br>"
"As the bright moonlit night leaves, the craving hearts say,<br>"
"Forever-long, wish the aura would stay this way.<br>",
"type": "poetry",
"genre": "sonnet",
"feedback": ""	
},
{
"id":13,
"title": "Mythical Plague",
"username": "okluv22",
"content": "Abigail listened to the sounds of her parents talking through their thin bedroom walls."
"<br>"
"“I can not believe that they are gone,” her mother said in a numb voice. She had never heard her use that tone before. "
"Abi knew something horrible had happened, but she had no clue what it was. She scrunched up her face in thought, when she "
"heard her parent’s footsteps reverberating through the halls. She picked up her skirts and ran down the corridor, trying to muffle the"
" loud clanking of her shoes against the floor. She went into her bedroom and held the door open slightly, just enough so that she could "
"see her father rubbing her mother’s back, her tears leaving tracks down her face."
"<br>"
"She could not watch anymore, so she closed her door as quietly as possible, and sat down on her bed. Abi looked across the room at her "
"vanity mirror, and stared at her reflection. One eye of midnight blue, and one of emerald green. Her wavy, auburn hair that reached past "
"her tailbone, and thin white lines tracing the left side of her face. She ran her index finger along the pattern, finding the shapes of "
"small leaves and flowers joined together by a community of vines. Most children did not look like her, but she never really minded. "
"It just meant that she and her family were unique."
"<br>"
"Abigail assumed that there would be a ceremony tonight. The fairy populace celebrated almost everything. Life and death, the changing of "
"seasons, and many other strange holiday-like things. Each type of ceremony was very different from the others, but all were happy and" 
"lively. Abi was only half fairy, but she still counted as one and was invited because she had fairy blood. Her father was only "
"allowed because of his marriage to a fairy, also."
"<br>"
"She was broken out of her reverie by a knock on her bedroom door."
"<br>"
"“Come in,” she said, flattening her dress with the palms of her hands."
"<br>"
"Her father cracked open the door and peeked his head inside."
"<br>"
"“Abi,” he said, with a heavy-hearted expression plastered across his face, “Prepare your ceremony dress, it is starting in an hour.”"
"<br>"
"“Yes sir,” she answered, standing up and opening her closet to see the array of fabrics and tints."
"<br>"
"He nodded, shut the door, and walked away as Abigail picked out her ceremony dress and put it on. The fairy women always wore light, "
"easy-to-move-in dresses that represented their elements. The elements were nature, air, fire, and water. Because Abi and her mother’s "
"element was nature, their dresses were light brown with hand sewn vines and flowers lining the entirety of the dress, bringing leaf "
"greens and blood reds over the monotone shade. They were not as modest as the humans dresses, because they only reached their knees, "
"but fairies did not care much about modesty."
"<br>"
"Abigail left her room and started making her way downstairs, and then met her parents in the living area. They walked out of their house "
"and went down to the riverbed where they always held the ceremonies. There were already a lot of fairies gathered under the canopy of "
"trees. Abi had always loved the meeting place, especially in autumn, like it was now. She loved the crisp red, orange, and yellow leaves "
"twisting through the air like flames. The small drops of water falling off of the branches from the rain early this morning. The flowers "
"that lined the bottoms of the tree trunks, bringing an array of color to the autumnal chroma of the forest. You can tell that I am half "
"nature fairy, she thought."
"<br>"
"They started walking down to their table, her mother wiping her tearful eyes every now and then. They sat down and waited for Rune to "
"begin the ceremony. Most fairies had very mystical names, at least according to the humans, but Abi had always thought they were normal, "
"and that her name was strange. Her mother and father had agreed that if the child were a girl, he shall choose the name, and if it was "
"to be a boy, she would decide. So, when the baby was born and was announced as a girl, she was named Abigail. And because her father "
"had a human family, she became one of the only fairies, or half-fairy in her case, to have a human name."
"<br>"
"Rune cleared his throat from his platform, and everyone’s head swiveled to face him as he spoke."
"<br>"
"“As we all know, we lost Thalia and Oriel early this morning under some unfortunate and strange circumstances,” he announced, which caused"
" many attendants to release sobs, most of them stifled by their hands."
"<br>"
"“But, we all know that these inspirational and generous fairies would not want us to grieve over their passings, so we shall not. We-”, "
"his sentence was cut off by an audience member coughing aggressively."
"<br>"
"Everyone twisted in their seats to see Marevien on his knees, arms crossed across his stomach as if he’s trying to hold his body together."
" Everyone raced over to his side, asking what was wrong, but he could not speak, could not breathe. The coughs were shaking his entire self "
"as if there was an earthquake only he could feel. Then, something strange, stranger than the coughing fit by far. A blue liquid came pouring "
"out of his mouth. It looked like a puddle that held the sky in its arms."
"<br>"
"But then, every fairy started coughing. The blue liquid pouring out of their throats. One by one, every fairy stopped coughing. "
"When Abi finished, she felt different. She reached up to wipe her mouth, and froze. The pattern that used to be on her face was gone. "
"She scrambled over to the river and stared at her reflection. Her eyes were both blue, neither of them green"
"<br>"
"She was human."
"<br>"
"They were all human.",
"type": "fiction",
"genre": "science fiction",
"feedback": ""	
},
{
"id":14,
"title": "Scars of the Tiger",
"username": "blazingman2",
"content": "He sat bolt upright, instinctively reaching for his throat. Gasping he looked around the room trying to push away the "
"nightmare’s haunting images that kept replaying before his eyes. The night’s air cooled the sweat that oozed from his skin’s pores, "
"as he pushed down the fear balled up in his throat and stomach. His blazing blues eyes grew wide as he rubbed his neck and found it "
"missing. The animal tendon that he used as a string to hold the fang of the dead mountain lion that had raised him was gone."
"Immediately he stood, fear flashing in his eyes as he scoured the dark room. Moonlight caught on something and flickered. Looking" 
"closer he thought was Misty’s calm motherly green cat eyes. Then they morphed into angry, evil, starving, unforgiving amber eyes;"
" the wall in front of him flashed orange and black stripes, and then flicked to the sharp deadly claws and teeth of the tiger that "
"tried to kill him a few years ago. Shaking, he fell back on his butt, his hand landing on Misty’s tooth. Sighing a shaky relief he"
" tied it around his neck and walked over to the bathroom, dust particles mockingly dancing in the moon’s silver glow."
"Turning on the light and slightly closing the door, he pulled off his shirt and turned his back to the mirror. Looking over his "
"shoulder he used the mirror to trace the scars. Ignoring the other little faint scars, he studied the four long jagged white scars "
"that ran down his tan muscular back. Wincing at remembered pain, he sighed and put his shirt back on. That tiger had been haunting "
"his dreams at least once a week for years."
"Tuning on the faucet he stuck his head under the icy cold water. He gave a shaky breath still trying to shake off the flash backs. "
"Slowly he added warmth to the water till it was soothingly hot. Smiling to himself he remembered how Misty would lick the back of his "
"hair the wrong way after he had had a nightmare to sooth him. Though a cat, she had been a better mother than his real mom or any of "
"his foster care moms."
"“Jack?” a voice asked from the doorway. Jack stood, hitting his head on the sink on the way up. He stood there, his black hair soaked "
"and dripping, looking at the voice’s owner: a sleepy Taylor who looked like thunder had awaken him even though there was no storm. "
"“You ok?” The scrawny blonde haired brown eyed boy asked."
"“Ya. I’m fine.” Jack replied thinking about how Taylor had escaped his kidnappers and now with Jack’s help was heading home."
"“But, what about those scars?” He persisted."
"“Um … they’re nothing and I really don’t want to talk about it right now.”"
"“I’m going to find out sooner or later and you know it.” The 15 year-old said growing in confidence against 18 year-old Jack."
"“Well I’d rather you find out later than sooner,” Jack growled throwing in a bit of a snarl so he would stop arguing. “Now get your "
"butt back to bed.”"
"Taylor left and got into his bed. Jack shook his wet head and turned off the water. He knew the kid was right. At some point "
"they were going to run into one of the few people who knew. Then the beans would be spilled. Crawling into his sleeping bag on "
"the floor he was tempted to just leave, to just run from the past that this adventure was putting on the path ahead of them. I have "
"a job to do and I can’t leave Taylor to fend for himself, Jack thought as he drifted off to sleep. He wouldn’t stand a chance against "
"the vicious killers from my past that are after him, he’d be torn apart like a rabbit in a pack of dogs.",
"type": "fiction",
"genre": "action",
"feedback": ""	
},
{
"id":15,
"title": "Eyes",
"username": "34rtof",
"content": "Flames flicker and burn intensely in her chest. The feeling falling into the depths of her stomach setting it ablaze. Her lips "
"flikcer into a weak smile to hide the growing heat rising to her cheeks. The flames lick her cheeks and gives way for relief. The swirling, "
"awkward heat breaking through her flesh leaving a red behind. The red left behind only causes a smile;making the flames flutter more in her "
"beating heart. It was an odd idea, a concept that tasted like bitter poison. Seeping into her minds cracks and filling the space with serpents."
"<br>"
"The serpents speak crude thoughts that most would drown in. In her mind.. the serpents are deafned by by the suffocating flames. The flames that "
"seemed to diverge from one point. Lizziy's eyes. The eyes that caused the flames to flicker and burn in her chest. Lizzy't eyes were a calm, "
"stark contrast to her's. Being like water that always flowed, never showing its hidden rocks beneath. Eyes that called the her flames, since "
"they were always so giving. Giving light to the dakrest parts of her."
"<br>"
"Yet, the serpents still speak their minds. Forming thoughts that resorted in blood that dripped from her pores. Blood that others fail to see.."
"other than Lizzy.Although that blood soon faded as it was wiped away by blue. The embrace of Lizzy unleashed the rain from her eyes. The swirling "
"love blossomed its petals stretching from her heart to her mind. Throwing away the serpents and returing the flames to her eyes.",
"type": "fiction",
"genre": "romance",
"feedback": ""	
},
{
"id":16,
"title": "Death Has Its Heart in the Right Place",
"username": "mrsharrystyles",
"content": "Looking down the barrel of a gun is a strange feeling, but after staring into Death's dark face so many times, Jack had become accustomed " 
"to the tickles and prickles that run across your spine. It had become a familiar, a common, an ordinary feeling. He almost liked it, the sensation, "
"of Death looming about, waiting for the perfect moment to strike. To him, it was intoxicating. It made his heart race, his blood pump and adrenaline run."
"It was like being in love for the first time, and the last. Yet every time that the Reaper swung his scythe on the mob boss, he always seemed to stop, "
"never finishing the job. It was as though he, Death, took pleasure in seeing Jack sweat under his blade. They both enjoyed the mad thrill, but it seemed "
"that this would be the last time they would saviour it."
"Bang! The thunderous roar of the gun shattered the calm night. It was over."
"'Here. You can keep it,' the assassin tossed the smoking gun onto Jack's cold lap."
"A sinister smile cut the killer's face. Raising his chin proudly, as a young boy does after winning a prize, the mercenary turned around slowly, savouring "
"his victory. Now all he had to do was collect his pay and live comfortably on some exotic island for the rest of his life, without worries, without problems, "
"without necessities, without ' Bang! A second shot."
"The assassin's knees broke under the pain. One moment he was savouring glory and the next he was savouring the bitter sweet taste of warm steel, the killer "
"kiss of a bullet. On all fours, he lifted his trembling hand up to his chest: his shirt was soaked in blood that was spewing out on both sides of his trunk."
"He was cold, weak, in pain. Frozen sweat poured down his face as his insides burnt in anguish."
"Writhing on the floor with no strength at all, he turned around to see who the shooter was. Behind him, sitting in the same leather-cushion seat he had been "
"sitting when the assassin came in, Jack sat. The only difference was that now his right arm was outstretched with his fingers curled around the gun."
"His eyelids were heavy upon his red eyes, but he still maintained them wide open."
"'No ' Impossible ' I shot you ' I shot you in the heart.'"
"Jack licked his lips and explained slowly, enjoying every word, 'I am dextrocardi-ac.'",
"type": "fiction",
"genre": "thriller",
"feedback": ""	
}, 
{
"id":17,
"title": "The Witches",
"username": "cyy6",
"content":"They stay."
"They build their village and their houses. They dance on their strings, and fill their roles. They say their prayers and they preach their book, "
"but nobody is redeemed. The struggle of building a colony hits them and they start to crack. The goats don't milk well and sleeves don't sew right. "
"Mrs. Barsham swears she sees a horned shadow at the foot of her bed."
"They grow angry, they hang and burn their wives and daughters. They laud the land as belonging to their religion, their god, their country."
"But the witches were there first.",
"type": "fiction",
"genre": "science fiction",
"feedback": ""	
},
{
"id":18,
"title": "The Summer",
"username": "quincy98",
"content": "I used to hope and pray for you;"
"But wishes don't always come true;"
"I was all alone;"
"And then it all changed when I met you."
"<br>"
"I know the cure to heal my heart;"
"But it's not here with you;"
"I am running back;"
"To the girl I used to be."
"<br>"
"I am going back;"
"To the boy who never chased me;"
"Now he wants me by his side;"
"The way it always should have been."
"<br>"
"We are together once again;"
"Still young enough;"
"To remember how we felt;"
"Without our other half."
"<br>"
"I am alone no longer;"
"Oh, how good it feels;"
"When you put your arm around me;"
"And your lips meet mine.",
"type": "poetry",
"genre": "lyrics",
"feedback": ""	
},
{
"id":19,
"title": "An Infinite Abyss",
"username": "brookie_st",
"content": "I walked to Elijah. He was wearing his signature beige trousers, harnessed on by a pair of suspenders over a white button-down."
"He sat under his cottonwood tree, the seeds falling, slowed by their feathered parachutes. Each twirling down, mimicking the pirouette of a "
"ballerina. Elijah was oblivious to one stray dancer that had landed in his hair. However, she left as softly as she had arrived, swept away "
"by a summer breeze."
"…"
"I remember that spring years ago when we would come back from school and immediately change out of our uniforms so we could head to the forest, "
"on the border of the schoolyard. Elijah and I used to collect twigs and fallen pine needles to build bird's nests. Our bare feet crushed dried "
"leaves under us, our skin naked against the cool soil. Feeling the shade of the evergreens above, we sauntered into afternoons of blurred landscapes, "
"getting lost in a labyrinth of trees. Putting our ears to the forest floor to listen to the secrets the earth was hiding from us, leaving soft "
"footprints that called us home when the sun was tired. Peacefully lost in a daydream we shared. We slowly made our way through the woods picking up"
"every small branch or tuft of grass that we saw fit, using the larger branches as walking sticks but then getting tired, and dragging them behind us."
"Patches of sun spilled through the cracks in the leaves, we had reached the edge of the forest where the trees began to clear, making room for a "
"meadow. It was barren except for the brilliant yellow daffodils that were scattered throughout the dry grass. The day was hot and Elijah and I were "
"already covered by a thin layer of dirt and sweat, tired from our morning adventure. But as he was looking out into the meadow, admiring our discovery, "
"a giddiness descended on us and he started to laugh, so I began to as well."
"It became our tradition to head to the meadow after school, collecting every twig we could find on the way. He said the daffodils there would be "
"perfect for the nests, so we picked those as well. When our hands became too full we deposited all the flowers we had gathered into a pile, next "
"to the twigs and brown grass. A week later we had almost worked our way through a small section of the meadow. Still adamant on providing homes for "
"birds, Elijah tried to pull a flower, but a bee flew out and stung him on the back of his hand. The sting swelled into a small bulge. It was the "
"first time I had seen him cry. Tears pooling into his eyes and lip quivering, the soft whimpers of a child."
"…"
"The seasons turned slowly as they always do, and spring passed into summer, our favorite season, for it was when we were free of our beige sweater "
"vests and ties. And with the seasons our activities of choice changed. Nest building shifted into frog catching, which shifted into soccer, our new "
"favorite pastime. Elijah’s siblings were always keen on joining us, even if we weren't always keen to have them around, especially his youngest sister, "
"Emelia, who seemed to cry if the wind blew in the wrong direction."
"Countless hours were spent in the torrid heat, but we always returned with grass-stained shirts and sun-stained skin. Elijah's ears were too large for "
"his face which made them stand out even more when they burned. His alabaster complexion never tanned, only burned into a rosy pink, then peeled into a "
"new layer of milky white. A striking contrast to my skin, which resembled the umber brown dirt we raced across every day."
"…"
"I remember that damned day I walked to Elijah. It was late, around 9:30. His raven hair a messy heap above his forehead. He was in his usual attire of "
"suspenders, a white shirt, and beige trousers. He’d asked me if I wanted to canoe with him and I’d said yes."
"…"
"We reached the water and set the canoe down on the tall grass by the seashore. The cicadas screamed at full volume, fighting to attract a mate. "
"Each going through a life cycle of molting, leaving behind skins to scare our sisters with. Their song almost drowning out the crash of waves against "
"the night sand."
"I climbed in first, then Elijah, and we pushed off with our oars, floating away from land. The moon was a dull crescent in the sky, which provided "
"little light in the ebony darkness. Time passed in slow motion as we pushed through the water, but as our eyes adjusted to the dark thousands of stars "
"appeared in the midnight sky, new one's becoming visible with every few minutes that passed."
"Soon we had drifted so far from shore that I could no longer see the Allerton’s seaside home. Eventually, we were surrounded by a boundless expanse of "
"dark water. The canoe bobbed on each wave, current, and ripple, swaying us with it. We stared out into the hundreds of infinities, crisp summer air "
"drying the sweat on our foreheads and noses."
"Our skin soaked in humidity from the air, while our lungs filled with heat. We continued to row into the abyss, hoping to be carried by the ocean "
"into a tomorrow that wasn’t as half lived as yesterday. The thick air was filled with a soporific fog. Our arms grew tired and our eyelids heavy. "
"\"Would you like to take a break?” I asked, he paused for a moment before replying, “Yeah, only for a while and then we can head back,” We set the "
"oars down beside us. It must have been close to 4:30 am, on the cusp of dawn, and a heavy drowsiness was settling upon us."
"<br>"
"…"
"Crying."
"A cold room."
"White lights."
"\"Did he have another episode?\""
"\"Yes, um, what was it this time honey?\""
"I could hear her voice shaking"
"\"Elijah…\""
"Whispers."
"\"Again?\""
"I managed a weak nod."
"More whispers."
"\"Has the exposure therapy helped?\""
"\"He never speaks after his sessions.\""
"A comforting pat."
"\"One moment please Ma’am\""
"She wiped her tears then nose."
"\"Increase Paxil dosage by ten percent.\""
"…"
"<br>"
"I still let his ghost visit me sometimes… to reminisce in my dwindling memories of our summers together. Our frequent visits to the beach behind "
"his house, swimming in the ocean water which made our legs dry from salt. The grassy field near the schoolyard where we spent so many sleepy afternoons "
"sunbathing. His cottonwood tree who’s dancers we wished upon countless times, blowing them away with our childhood dreams of new shoes and hard candies. "
"The night we drifted too far from shore, swimming in the same waves, drowning in the same current, only one of our heads breaking the surface in the end. "
"Seeing the faded version of him in my bedroom some nights when the crashing waves pull me back into the ocean. The tide too strong for me to escape the "
"hurricane. And with that tide, I float slowly back into the sea with him. We swam in the same water that night, we all swim in the same water, it's just "
"harder for some of us to stay afloat.",
"type": "fiction",
"genre": "realistic fiction",
"feedback": ""	
},
{
"id":20,
"title": "Rebirth vs. Suicide",
"username": "peachy_102",
"content": "Rebirth versus suicide. I want to make the conscious decision to no longer exist, to no longer exist as the person I am. I cannot reverse my faults. "
"I cannot take back my words. I cannot succeed when I chose to fail or reclaim any integrity I so irresponsibly lost. Thus, I shall reinvent myself: A revolution "
"of the heart and mind. I shall be born from the blood and tears and grief that killed my former self. What then, if I accept the person I used to be like an old "
"friend or lost lover? Would that vanish the regret? Would that rid me of the knife that works its way through my gut as I try to form words? Would it at least "
"allow me to read my own writing, without calling it trite or mediocre?"
"Would it stop me from hating the new person- from hating me?"
"I can only hope so. I can only hope it will embrace me with all the warmth and freshness of the morning, pulling me into the presence of light and the presence of "
"love and the presence of God."
"I can only hope, with all the desperate, honest longing that is hope, that I can still save myself. I can only hope, with the blinding blanket of snow that is "
"hope, that all things that ail me can be cured, that someone will love me despite them and that someone already does."
"I hope. When there is nothing else I can do, I hope. I hope with the promise of a new day, a baptism, a change. I hope with the hypocrisy that dwells in the pit "
"of the well in my heart and the hypocrisy that settles on the ocean floor. I hope for the miracle of chance- a much greater miracle than many would think. It's "
"the kind of miracle that makes skeptics fall to their knees in prayer, something I yearn to do but my secular mind forbids. "
"Someday soon I will be relieved of my wounded heart and my empty beliefs and the restrictions on my ideals. The verdict's in: Rebirth is victorious.",
"type": "fiction",
"genre": "realistic fiction",
"feedback": ""	
},
{
"id":21,
"title": "a love scorned",
"username": "dreamscapes",
"content": "i was not allowed to look at her."
"<br>"
"father told me it was because she was no good, that she came from horrid magic. but deep down, i think he knew."
"<br>"
"the day he came into my room to find us in bed, legs tangled and hands intertwined like branches, was the first "
"time i’d ever felt true fear. as he pulled me up by the arm, i could do nothing but watch him spit curses at her "
"retreating back."
"<br>"
"\"i love her!\" i cried."
"<br>"
"but a daughter who liked girls the same as boys was no daughter of his.",
"type": "fiction",
"genre": "romance",
"feedback": ""	
},
{
"id":22,
"title": "My Weird Dream (The Monkey Slayer)",
"username": "jorae_gonzales",
"content": "I was surrounded by monkeys. Not just any monkeys, but evil monkeys from the gates of hell. They were "
"coming from left and right. I whipped out a machine gun also known as a mini-gun, which isn’t small at all. The "
"Massive gun is about as long as a bat and as round as a fire hydrant. I mowed them down with thousands of lead "
"bullets, but they still kept coming."
"<br>"
"They were popping out from everywhere. It was like a wild game of whack-a-mole."
"<br>"
"\"Time to light ‘em up!\" I screamed as I pulled out a flamethrower."
"They looked like little fireballs zigzagging around the field like crazy. The demonic chimps grew closer and "
"closer to me. It seemed every time I got rid of one another one took its place. All I had left was a shot gun and "
"a couple of rounds. Next thing I knew the sun was blotted out of the sky by raining deranged apes. I heard a shotgun "
"go off then I woke up.",
"type": "fiction",
"genre": "action",
"feedback": ""	
},
{
"id":23,
"title": "I Am That Girl",
"username": "teen_writer_1",
"content": "I am that girl with blades in her hands."
"With fire in her eyes."
"And words made of sand."
"<br>"
"I am that girl who cuts through the world."
"With a shadow so big it could swallow the stars."
"Her soul is a riddle of bruises and scars."
"<br>"
"I am that girl who despite being brave is afraid of the dark."
"And it's cruel whispers."
"That try to kill her flying sparks. "
"<br>"
"I am that girl who loves all things wild."
"Who runs through the woods."
"Like a careless child."
"<br>"
"I am that girl who lives for the time."
"In which words fly like blood."
"And settle like grime."
"<br>"
"I am that girl who likes the silence."
"That comes with decay."
"But will turn it quickly to cold violence."
"<br>"
"I am that girl.",
"type": "[poetry]",
"genre": "sonnet",
"feedback": ""	
},
{
"id":24,
"title": "A Dream",
"username": "anonymous1234",
"content": "She walked inside of the coffee shop that was on a private beach and sat down on a rather dusty and torn up "
"chair. She called over the waiter and asked for a black coffee. Once the waiter brought out her coffee, she walked outside "
"to feel the fresh air. She watched as the waves crashed against the shore. She heard the seagulls screeching at the top of "
"their lungs. She felt her feet sink in the golden sand while she walked. Her mind was racing after thinking about all the "
"things that had happened that day but she let it all out. She sat down and stared at all of her surroundings. She got up after "
"her mind cleared of thoughts and walked over to the luminous blue water. She smelled the salty air and watched as the water "
"washed off the shore and left seashells. She felt a warm hand touch her on the shoulder. She was startled but was calm and "
"sat there scared. Minutes later, she heard a loud ding and got up. She looked around and saw nothing close to the beach. She "
"set her hand down and felt a rather soft item. It was her bed. She couldn’t see very well as it was dark. She was taken back "
"to existence and realized it was all a dream. Or was it as she saw a black coffee lay on her bedside table next to her lamp.",
"type": "fiction",
"genre": "action",
"feedback": ""	
},
{
"id":25,
"title": "Time Machine",
"username": "joshlovescats",
"content": "It was a regular day at CVJH. A group of friends were quietly sneaking around to the gym. Now the reason they were "
"going into the gym was because there was a rumor that a bomb shelter was under the school bleachers. Well big whoop, a lot of old "
"buildings still had bomb shelters, but in this bomb shelter, there was supposed to be something living inside of it. The thing was "
"supposed to be trapped inside, from the early nineteen hundreds, around the beginning of World War 2, never to leave the school. "
"Well the groups of five boys were going to find out whether it was true or not. They were Austin Carter, Kevin Urquhart, Devin "
"Mcfarlane, Tanner Charles, and I, Josh Zushi."
"I was leading the guys to the area of the supposed bomb shelter. I led them under the bleachers and toward the back. It was hard "
"to move under the bleachers without making any noise, because of all the food wrappers, empty water bottles, and deflated balls, "
"but we managed to make it through without making much noise. At the back of the bleachers, there was an oval trapdoor. It was "
"aligned with metal around the shape, and had a ringed handle. We had to try to lift the big oval, though it was heavy. It weighed "
"about four hundred pounds, but using leverage, we were able to swing it open."
"We quietly crept down the new set of stairs that appeared out of the darkness, and we shone our cell phones down into the pit. "
"The floorboards crept under us with each step we took, making the area even creepier. Once and a while, one of us would stumble "
"or run into thick cobwebs hanging from the lowered ceiling. When we finally made it to the bottom, we were in a trance. The shelter "
"was nothing compared to what we thought it would be. There were shag rugs here and there, a big plasma screen TV, a hot tub, a "
"refrigerator loaded with soda, and a nice little sofa."
"Now this was totally worth finding. Us guys were looking around at all of the cool things in there, all of the closets stuffed "
"with canned foods, the kitchen, bedrooms… we got to this closet that was empty, and the guys thought it would be fun to shove me "
"into it and bolted the door shut. Well it wasn’t fun. When they shoved me in there, they did it so hard that I hit my head down on "
"something. It felt like a little lever. When my head hit it, it went down and all of these lights and beeping noises were blowing off."
"I woke up later from my concussion, stood up, and tried to see if I could open the closet door. To my surprise it swung right open. "
"But something was wrong. Where were the guys, and what happened to all of the furniture? Instead there was a room full of kids about "
"my age, 13, and they all had the same expression on their faces, looks of terror. But this shelter hadn’t been used since WWII. I was "
"stuck in World War II"
"Whoa wake up, what kind of creepy dream was this, and what was going on? Then I realized it. That closet was a time machine, and it "
"brought me to this time. The kids were all crowded inside, lining up in alphabetical order. The teachers were calling names down the "
"list, Brianna Abbot, Wilson Barnacle, Rock Belnap… whoa what the… Mr. Belnap! This was WAY before World War II!"
"The story behind it was that Rock was pulling on Brianna’s pigtails, and the punishment was that he had to stay in the shelter for "
"five minutes. The teachers left Rock behind and locked him up. I, of course, being the genius I am, returned to my own time and told "
"the guys what happened. They obviously thought I was crazy, and didn’t believe me."
"Well at leas I know the true story of the \"bomb shelter\", and why Mr. Belnap spends so much time in the gym.",
"type": "fiction",
"genre": "action",
"feedback": ""	
},
{
"id":26,
"title": "Jerk",
"username": "lovernotafighter4",
"content": "I love your voice,"
"your soft brown hair."
"I love your eyes"
"and love your stare."
"<br>"
"I love your laugh,"
"your cocky smirk,"
"your stupid jokes."
"You precious jerk,"
"<br>"
"you know I do."
"I want my hands"
"all through your hair"
"each treasured strand."
"<br>"
"I’m wrapped around"
"your finger still."
"Am I yet yours?"
"Your love does kill"
"<br>"
"the things I hold"
"so close to me"
"and yet you’re the"
"best jerk I see.",
"type": "poetry",
"genre": "ballad",
"feedback": ""	
},
{
"id":27,
"title": "Passion and Desire",
"username": "danielle_gem",
"content": "Your smile brings warmth into my heart!"
"The way you gaze into my eyes;"
"My love for you will never part,"
"Our burning flame will never die;"
"Your presence gives me life to live,"
"Though poison seep in now-a-days:"
"The lies I told that you forgive,"
"Life with you is worth a stay:"
"Beauty cannot justify our love,"
"But your beauty’s worth gazin’;"
"Our love comes up from above,"
"Being with you’s so amazing;"
"The life you live is well and smart,"
"Be with me ‘til death do us part?",
"type": "poetry",
"genre": "ballad",
"feedback": ""	
},
{
"id":28,
"title": "The Forbidden Dancer",
"username": "manchester_girl",
"content": "She stood on the dancefloor watching, waiting, Oh,dear God she thought Please don't let me mess up now. She was Melonie"
"and she had loved dancing but she couldn't do it because one of the community rules was no dancing, so she daydreamed about it."
"<br>"
"The next moment she was woken out of her dream by Mrs. Fallbright the English teacher and she found everyone staring at her like "
"she had 3 heads or five eyes or something."
"She had started to look so red she had been taken to the nurse and sent home."
"\"What am I going to do with you,\" asked her mother,\"This is the third time this week you were sent to the nurse, What is it in"
"you're head that is making this happen?\" Melonie said nothing instead looking in the mirror behind her mom, looking at herself."
"She would need to re-streak her hair soon she could tell, The electric blue had stated to fade to dull blue."
"Her earrings needed to change too. I have a pair of skull and cross bones I could wear this week she mused."
"\"I said what is in your head child to make you this way.\" her mother said startling her."
"Of course she wouldn't couldn't tell her mom that her thought and dream was dance so there was a dead icy silence in the room."
"Well if I can't dance here, she thought, I'll go somewhere where I can."
"<br>"
"Next she had walked out the door \"Goodbye mom\" was all she said before the door closed, leaving her outside and her mom inside "
"screaming and with hot tears of fury but there was nothing, absolutley nothing she could do about it. Her only child had left her "
"and now she was all alone. Melonie's father had died years before melonie was born so now without melonie she had nothing and noone "
"to depend on.",
"type": "fiction",
"genre": "science fiction",
"feedback": ""	
},
{
"id":29,
"title": "The Swan Princess",
"username": "angelaoxo",
"content": "Odette entered the hidden meadow tentatively, afraid that this was all just a dream. A nightmare. Her feet were bloody "
"from running through the forest barefooted. Her breathing was fast and light, entirely too insufficient for her body; she began to "
"feel light headed. As Odette went further and further into the meadow the less she had to force herself to go at a walking pace; the "
"meadow was the essence of purity. It was as if nothing bad could ever happen there."
"As Odette slowed, she realized how tired her body was. She had been running for hours in the forest, clueless to her location, but "
"only caring that she was not near Him. At the very thought of him Odette’s body tensed; her limbs gave out and she fell onto the ground,"
"the plush grass breaking her fall."
"Odette was so tired, but she forced herself to stay awake. Off in the distance there was the noise of someone approaching. She could "
"barely left her head, but when she did she saw that it was nothing to fear, just a harmless doe. Odette started breathing again, but "
"she didn’t remember holding her breath."
"Odette clenched her feet and a stab of pain shuddered throughout her body; closing her eyes, she tried to control her breathing. When "
"she opened her eyes, she closed them and than opened them again hoping that what she was seeing wasn’t real."
"\"Hello, Odette.\""
"Odette tried to scream, but it caught in her throat. Her eyes clouded with tears as she shook her head. Her captor, Eric, kneeled next "
"to her and stroked her cheek. He smiled a terrible grin and said, \"My little swan almost got away, but have no fear I found you again.\""
"She tried to scream again, but it was futile. Even if she did manage to scream, there was no one around to hear her. She was sobbing then, "
"her whole body was shaking."
"\"Calm down, don’t be frightened my little swan. Your prince is here now. Come on, I’ll take you back and tend your wounds.\""
"Eric lifted her up into his arms and held her close. Odette just stilled in defeat. No matter where she was, Eric would find her. No "
"matter how safe a place seemed, Eric would get to her. No matter what, she was doomed to an eternity of being the swan princess. "
"Except she was never saved by her prince charming, instead her prince was killed by the beast and she remained forever under a spell "
"with no way of undoing it. She was stuck in the pond, just waiting for the moon to hit so she could turn human once more.",
"type": "fiction",
"genre": "science fiction",
"feedback": ""	
},
{
"id":30,
"title": "All I Need Is a Friend",
"username": "ryanmoran",
"content": "Books fill up my room."
"Not baseball cards,"
"or pictures of girls,"
"or basketballs."
"Maybe a blown up picture of …"
"… Pam Anderson might help."
"<br>"
"Black-framed glasses"
"and a white,"
"pale,"
"lanky"
"body."
"I should start working out."
"<br>"
"At least I can read."
"I read four books a day last summer."
"The librarian,"
"80-year-old Mrs. Woodsworth,"
"she knows my middle name."
"If only I had a real friend."
"I am sick of seeing her old,"
"bony,"
"pale body."
"Although it resembles mine."
"<br>"
"The kids at school laugh."
"Is it the way I dress?"
"Lacoste,"
"Ralph Lauren,"
"La Tigre."
"I’ve tried every designer out there."
"Staying in the house really saves me money."
"My stupid rich parents give me $50 a week for lunch."
"50 dollars times 36 weeks …"
"what is that?"
"1,000 dollars,"
"2,000 dollars,"
"10,000 dollars?"
"I should probably know."
"Straight A’s 12 years in a row"
"and counting."
"<br>"
"With all of this,"
"or none of this –"
"it depends how you look at it –"
"all I need is a friend.",
"type": "poetry",
"genre": "free verse",
"feedback": ""	
}
]

titles=["The Day I Swallowed the Sun",
"My Summer Love",
"Monster",
"Grandma's Light",
"Why I Write",
"Breakup Advice",
"Just Swinging",
"Golden Tint",
"Daddy's Womb",
"Who Is That...",
"Emergency",
"Armageddon in Autumn",
"Vista of Moonlit Night",
"Mythical Plague",
"Scars of the Tiger",
"Eyes",
"Death Has Its Heart in the Right Place",
"The Witches",
"The Summer",
"An Infinite Abyss",
"Rebirth vs. Suicide",
"a love scorned",
"My Weird Dream (The Monkey Slayer)",
"I Am That Girl",
"A Dream",
"Time Machine",
"Jerk",
"Passion and Desire",
"The Forbidden Dancer",
"The Swan Princess",
"All I Need Is a Friend"
]

usernames=[
"saltyranchers",
"lindzwrites",
"meago",
"blkmirror",
"emly",
"plnt22",
"ak233",
"love21",
"yunggun21",
"noair",
"kk214",
"wittyboy22",
"myfriend22",
"okluv22",
"blazingman2",
"34rtof",
"mrsharrystyles",
"cyy6",
"quincy98",
"brookie_st",
"peachy_102",
"dreamscapes",
"jorae_gonzales",
"teen_writer_1",
"anonymous1234",
"joshlovescats",
"lovernotafighter4",
"danielle_gem",
"manchester_girl",
"angelaoxo",
"ryanmoran"
]

tags=usernames+titles

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/upload_writing')
def upload_writing():
	return render_template('uploadWriting.html',writing=writing, current_id = current_id)

@app.route('/save_writing', methods=['GET', 'POST'])
def save_writing():

	global current_id
	global writing

	json_data = request.get_json()
	title = json_data["title"]
	username = json_data["username"]
	content = json_data["content"]
	typE = json_data["type"]
	genre = json_data["genre"]
	feedback = json_data["feedback"]

	#add new entry to writing array
	current_id += 1
	new_writing = {
		"id": current_id,
		"title": title,
		"username": username,
		"content": content,
		"type": typE,
		"genre": genre,
		"feedback": feedback,
	}
	writing.append(new_writing)
	titles.append(title)
	usernames.append(username)

	return jsonify(writing = writing)

@app.route('/view_all')
def view_all():
	return render_template('view_all.html',writing=writing, current_id = current_id)

@app.route('/delete_writing/<id>', methods=['GET','POST'])
#takes in an id, updates data, 
def delete_writing(id=None):
    index=0
    i=0

    #find index to delete
    for piece in writing:
        if piece["id"] == int(id):
            index = i
            un = piece["username"]
            ttle = piece["title"]
        i = i + 1

    del writing[index]
    titles.remove(ttle)
    usernames.remove(un)

    return jsonify(writing = writing)

@app.route('/edit_item/<item_id>', methods=['GET', 'POST'])
def edit_item(item_id=None):
	global writing

	index=0
	i=0

	for piece in writing:
		if piece["id"] == int(item_id):
			index=i
		i = i+1
	item = int(item_id)
	title = writing[index]["title"]
	username = writing[index]["username"]
	content = writing[index]["content"]
	typE = writing[index]["type"]
	genre = writing[index]["genre"]
	feedback = writing[index]["feedback"]

	return render_template('edit_item.html', index = index, item=item, title=title, username=username,
		content=content, typE=typE, genre=genre, writing=writing)

@app.route('/save_edits/<item_id>', methods=['GET','POST'])
def save_edits(item_id=None):

	index=0
	i=0

	for piece in writing:
		if piece["id"] == int(item_id):
			index=i
		i = i+1

	json_data = request.get_json()
	writing[index]["title"] = json_data["title"]
	writing[index]["username"] = json_data["username"]
	writing[index]["content"] = json_data["content"]
	writing[index]["type"] = json_data["type"]
	writing[index]["genre"] = json_data["genre"]
	writing[index]["feedback"] = json_data["feedback"]

	return jsonify(writing = writing)
@app.route('/search')
def search_edit():
	return render_template('search_edit.html',writing=writing, tags=tags)

@app.route('/view_item_feedback/<item_id>', methods=['GET', 'POST'])
def view_item_feedback(item_id=None):
	global writing

	index=0
	i=0

	for piece in writing:
		if piece["id"] == int(item_id):
			index=i
		i = i+1
	item = int(item_id)
	title = writing[index]["title"]
	username = writing[index]["username"]
	content = writing[index]["content"]
	typE = writing[index]["type"]
	genre = writing[index]["genre"]
	feedback = writing[index]["feedback"]

	return render_template('view_item_feedback.html', index = index, item=item, title=title, username=username,
		content=content, typE=typE, genre=genre, writing=writing, feedback=feedback)

@app.route('/save_feedback/<item_id>', methods=['GET','POST'])
def save_feedback(item_id=None):

	index=0
	i=0

	for piece in writing:
		if piece["id"] == int(item_id):
			index=i
		i = i+1

	json_data = request.get_json()
	writing[index]["title"] = json_data["title"]
	writing[index]["username"] = json_data["username"]
	writing[index]["content"] = json_data["content"]
	writing[index]["type"] = json_data["type"]
	writing[index]["genre"] = json_data["genre"]
	writing[index]["feedback"] = json_data["feedback"]

	print(writing)
	return jsonify(writing = writing)

if __name__ == '__main__':
   app.run(debug = True)


