Out of a sample of 100 questions:

- There were 43 questions that both the pre-and-post-fine tuning model answered correctly: these
  are the "Both Right" questions.
- There were nine questions that the pre-fine tuning model answered incorrectly and the post-fine
  tuning model answered correctly: these are the "Swap In" questions.
- There was one question that the pre-fine tuning model answered correctly and the post-fine tuning
  model answered incorrectly: this is the "Swap Out" question.
- There were 10 questions that both the pre-and-post-fine tuning models answered incorrectly: these
  are the "Both Wrong" questions

(For the remaining 36 questions, one of the two models did "just ok" on the question, getting the
question right only two or three times out of five)

<br>

# "Both Right" questions

<table>
  <thead>
    <tr>
      <th style="text-align:center">#</th>
      <th>Problem</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">1</td>
      <td>
        Chris is way behind on his math homework. He has 100 math problems to complete in total. He 
        completes 12 problems on Monday night. On Tuesday, he completes 3 times as many problems as 
        he did on Monday. On Wednesday, he completes one-quarter of the remaining math problems. 
        How many math problems does he have left to complete on Thursday?
        </td>
    </tr>
    <tr>
      <td align="center">2</td>
      <td>
        Verna loves to eat fruit. She bought three apples at $1.50 each, five oranges at $0.80 
        each, and six peaches at $0.75 each.  If she gave $20, how much change did she receive?
      </td>
    </tr>
    <tr>
      <td align="center">3</td>
      <td>
        John has 2 houses with 3 bedrooms each.  Each bedroom has 2 windows each.  There are an 
        additional 4 windows in each house not connected to bedrooms.  How many total windows are 
        there between the houses?
      </td>
    </tr>
    <tr>
      <td align="center">4</td>
      <td>
        A chef bought 4 bags of onions. Each bag weighs 50 pounds. A pound of onions cost $1.50. 
        How much did the chef spend?
      </td>
    </tr>
    <tr>
      <td align="center">5</td>
      <td>
        Jayden had $70 from selling pictures he took as a hobby.  His sister Ava gave him half of 
        her $90 allowance to help him buy a new camera that costs $200. How much more does Jayden 
        need to buy the camera?
      </td>
    </tr>
    <tr>
      <td align="center">6</td>
      <td>
        To raise money for their class fund, each of the 30 students from one class sold lollipops 
        that cost $0.8 per lollypop. On average, each student sold 10 lollipops. If they bought the 
        lollipops for $0.5 each, how much money was the class able to raise from the profit of 
        selling lollipops?
      </td>
    </tr>
    <tr>
      <td align="center">7</td>
      <td>
        A marketing company pays its employees on a commission-based salary system. If you sell 
        goods worth $1000, you earn a 30% commission. Sales over $1000 get you an additional 10% 
        commission. Calculate the amount of money Antonella earned if she sold goods worth $2500.
      </td>
    </tr>
    <tr>
      <td align="center">8</td>
      <td>
        In the first half of a soccer match, team A scores 4 goals while team B scores 2 goals 
        fewer than team A. In the second half, team A scores 1/4 of the number of goals scored by 
        team B, which scores 4 times the number of goals it scored in the first half. What's the 
        total number of goals scored in the match?
      </td>
    </tr>
    <tr>
      <td align="center">9</td>
      <td>
        Susan orders 3 magazines that send 12 issues a year.  She has 1 magazine that sends 6 
        issues a year.  Her last magazine sends her 4 times the amount of the 6 issue magazine. How 
        many magazines does she get every year?
      </td>
    </tr>
    <tr>
      <td align="center">10</td>
      <td>
        Martha's cat is 5 times faster than her turtle.  If the cat can run 15 feet/second, how 
        many feet can her turtle crawl in 40 seconds?
      </td>
    </tr>
    <tr>
      <td align="center">11</td>
      <td>
        Out of the 150 teachers on the school basketball court, 60% are history teachers. If the 
        rest of the teachers on the court are math teachers, and each teacher sleeps for 6 hours a 
        day, calculate the total time the math teachers collectively spend sleeping in one day.
      </td>
    </tr>
    <tr>
      <td align="center">12</td>
      <td>
        Hannah's city is having a big display of fireworks for the 4th of July. They're going to 
        set off 15 boxes of 20 fireworks each. Hannah's house is at the right angle to see 40% of 
        the city's fireworks. Hannah will also set off 3 boxes of 5 fireworks each in her backyard. 
        How many fireworks will Hannah see in total?
      </td>
    </tr>
    <tr>
      <td align="center">13</td>
      <td>
      While on vacation in Bali, Thea bought a hat from a craftsman worth $70. If she gave the 
      craftsman four $20 bills, how much change did she get?
      </td>
    </tr>
    <tr>
      <td align="center">14</td>
      <td>
        Suzanne sold 80 cookies for $1 each and 60 cupcakes for $4 each. She gave her two sisters $10 each for helping her. How much money does she have left from her earnings?
      </td>
    </tr>
    <tr>
      <td align="center">15</td>
      <td>
        Kelly has 5 quarters and 2 dimes. If she buys a can of pop for 55 cents, how many cents
        will she have left?
      </td>
    </tr>
    <tr>
      <td align="center">16</td>
      <td>
        The Kennel house keeps 3 German Shepherds and 2 Bulldogs. If a German Shepherd consumes 
        5 kilograms of dog food and a bulldog consumes 3 kilograms of dog food per day. How many 
        kilograms of dog food will they need in a week?
      </td>
    </tr>
    <tr>
      <td align="center">17</td>
      <td>
        Tim decides to light off some fireworks for the fourth of July.  He buys a package of 
        fireworks worth $400 and another pack worth twice that much.  He gets a 20% discount on 
        them.  He also buys a finale firework that costs $150.  How much did he spend in total? 
      </td>
    </tr>
    <tr>
      <td align="center">18</td>
      <td>
        Gary does laundry twice a week. Each load of laundry uses 20 gallons of water, and a gallon 
        of water costs $0.15. How much does Gary spend on water for laundry in a year?
      </td>
    </tr>
    <tr>
      <td align="center">19</td>
      <td>
        Ian has a board that is 40 feet long. He decides to make a cut so he can have two pieces. 
        The longer piece is 4 times longer than the shorter piece. How long is the longer piece?
      </td>
    </tr>
    <tr>
      <td align="center">20</td>
      <td>
        Ali is a superstar counter. He has won 22 medals for counting super fast. His friend Izzy 
        is also a really good counter and has 5 less medals than Ali. Together they have 10 times 
        less medals than have been given out for counting. How many medals have been given out for 
        counting?
      </td>
    </tr>
    <tr>
      <td align="center">21</td>
      <td>
        Elijah has one dog that is one-fourth the weight of Kory’s dog and another dog that is half 
        the weight of Kory’s dog. If Kory’s dog is 60 pounds, how much do Elijah and Kory’s dogs 
        weigh altogether, in pounds?
      </td>
    </tr>
    <tr>
      <td align="center">22</td>
      <td>
        Ashley has an internet connection speed of 20kb per second. Knowing that 1 Mb has 1000 kb, 
        she wants to know her internet connection speed in Mb per hour. What is Ashley’s internet 
        connection speed in Mb per hour?
      </td>
    </tr>
    <tr>
      <td align="center">23</td>
      <td>
        Jimmy has $2 more than twice the money Ethel has. If Ethal has $8, how much money is Jimmy 
        having?
      </td>
    </tr>
    <tr>
      <td align="center">24</td>
      <td>
        Mary has 6 jars of sprinkles in her pantry. Each jar of sprinkles can decorate 8 cupcakes. 
        Mary wants to bake enough cupcakes to use up all of her sprinkles. If each pan holds 12 
        cupcakes, how many pans worth of cupcakes should she bake?
      </td>
    </tr>
    <tr>
      <td align="center">25</td>
      <td>
        John goes to the market and buys 3 goats for $500 each and 2 cows for $1500 each.  How much 
        money did he spend?
      </td>
    </tr>
    <tr>
      <td align="center">26</td>
      <td>
        Sarah has 9 books and Joseph had twice the number of Sarah’s books, but he lost 2 of them. 
        How many books does Joseph currently have?
      </td>
    </tr>
    <tr>
      <td align="center">27</td>
      <td>
        Out of the 200 Grade 5 students, 2/5 are boys and 2/3 of the girls are in the girl scout. 
        How many girls are not in the girl scout?
      </td>
    </tr>
    <tr>
      <td align="center">28</td>
      <td>
        A tank of water has a depth of 17 feet on Monday. On Tuesday, the tank had 7 feet more 
        water. On Wednesday, the depth of the water is two thirds of what it was on Tuesday. What 
        is the tank’s water depth on Wednesday?
      </td>
    </tr>
    <tr>
      <td align="center">29</td>
      <td>
        How many girls are in the school if 40% of a school population is made up of 240 boys?
      </td>
    </tr>
    <tr>
      <td align="center">30</td>
      <td>
        At a restaurant, Juice Box A is 4 dollars. Juice Box B is 5 dollars more than Juice Box A. 
        Juice Box C is 7 dollars more than Juice Box A. How much more is Juice box C than Juice 
        Box B?
      </td>
    </tr>
    <tr>
      <td align="center">31</td>
      <td>
        Frankie and Binkie went bowling together.  Frankie's score was 15 better more than twice as 
        high as Binkie's. If Binkie bowled a score of 90, what was Frankie's score?
      </td>
    </tr>
    <tr>
      <td align="center">32</td>
      <td>
        Carl has four times as many marbles as Sean and Sean has half as many marbles as Cal. If 
        Sean has 56 marbles, how many marbles do Carl and Cal have combined?
      </td>
    </tr>
    <tr>
      <td align="center">33</td>
      <td>
        A restaurant has 40 tables with 4 legs and 50 tables with 3 legs. Calculate the total 
        number of legs the restaurant's tables have.
      </td>
    </tr>
    <tr>
      <td align="center">34</td>
      <td>
        George has 45% more pears than bananas. If George has 200 bananas, how many fruits does 
        George have?
      </td>
    </tr>
    <tr>
      <td align="center">35</td>
      <td>
        John buys a cassette with 2 songs.  The first song is 5 minutes and the second song is 60% 
        longer.  How much time was the total cassette?
      </td>
    </tr>
    <tr>
      <td align="center">36</td>
      <td>
        Matteo traveled at 55 miles per hour for 4 hours. Shandy traveled at 45 miles per hour for 
        10 hours. How many miles farther did Shandy drive than Matteo?
      </td>
    </tr>
    <tr>
      <td align="center">37</td>
      <td>
        Mary and John got married last weekend.  There were 20 private cars and 12 buses parked 
        outside the church.  After the ceremony, each bus carried 35 people and each car carried 3 
        people. How many people were inside the church?
      </td>
    </tr>
    <tr>
      <td align="center">38</td>
      <td>
        Coach brought one bag filled with basketballs to practice and dumped them all out onto the 
        gym floor before practice began.  After the practice time was over, he asked Jordan, Jason, 
        and Jeffrey to pick up the balls and carry them over to the bag.  The three boys picked up 
        and carried all of the balls in one trip.  Jordan carried twice as many balls as Jason, and 
        Jason carried twice as many balls as Jeffrey. If Jason had picked up and carried 2 balls, 
        what is the total number of balls that the coach brought to practice?
      </td>
    </tr>
    <tr>
      <td align="center">39</td>
      <td>
        A tomato vendor decides to switch who he buys his tomatoes for.  He sells 500 tomatoes a 
        day.  He used to buy them for $.5 each but he gets a new vendor who sells them for $.4 
        each.  How much money does he save a week?
      </td>
    </tr>
    <tr>
      <td align="center">40</td>
      <td>
        Rani has ten more crabs than Monic, who has 4 fewer crabs than Bo. If Bo has 40 crabs, 
        calculate the total number of crabs the three have together.
      </td>
    </tr>
    <tr>
      <td align="center">41</td>
      <td>
        200 pounds of carrots are to be distributed to 40 restaurants in a certain city. Each 
        restaurant is to receive 2 pounds of carrots. How many pounds of carrots will not be used?
      </td>
    </tr>
    <tr>
      <td align="center">42</td>
      <td>
        Bailey starts with a certain amount of money. Then she receives a weekly allowance of $5 
        for 8 weeks. At the end of the 8 weeks, if she has a total of $100, how much money did 
        Bailey start with?
      </td>
    </tr>
    <tr>
      <td align="center">43</td>
      <td>
        John makes himself a 6 egg omelet with 2 oz of cheese and an equal amount of ham.  Eggs are 
        75 calories each.  Cheese is 120 calories per ounce.  Ham is 40 calories per ounce.  How 
        many calories is the omelet?
      </td>
    </tr>    
  </tbody>
</table>

<br>

# "Swap In" questions

<table>
  <thead>
    <tr>
      <th style="text-align:center">#</th>
      <th>Problem</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">1</td>
      <td>
        Martha is planning her Christmas party. She invited 2 families with 6 people and 3 families 
        with 4 people.  8 people couldn't come due to illness, and 1/4 that number had previous 
        commitments. How many people show up for Martha's party?
      </td>
    </tr>
    <tr>
      <td align="center">2</td>
      <td>
        Mike decides he wants to replace his movie collection with digital versions.  He has 600 
        movies.  A third of the movies are in various series and he knows he can get those for only 
        $6 of the cost of a normal movie by just buying the series together.  40% of the remaining 
        movies are older movies which are $5.  How much does replacing the movies cost if a normal 
        movie costs $10?
      </td>
    </tr>
    <tr>
      <td align="center">3</td>
      <td>
        Mike was a pen pal with 5 people.  He stopped being penpals with 2 of them. They each send 
        2 letters a week that are 5 pages long.  He responds in kind.  He can write a page every 6 
        minutes.  How many hours does he spend writing a week?
      </td>
    </tr>
    <tr>
      <td align="center">4</td>
      <td>
        Mary buys 3 bags of M&Ms. The first bag has 300 M&Ms in it. The second bag has 12 more M&Ms 
        than the first, and the third bag has a hole in it, so it only has half the number of M&Ms 
        that the first bag had. How many M&Ms did Mary get total?
      </td>
    </tr>
    <tr>
      <td align="center">5</td>
      <td>
        A pirate crew is digging for buried treasure on the island marked X on a map. They dug ten 
        holes the first day, thirteen holes the second day, and eight holes the third day. They 
        stopped digging early on the third day to fill in two holes the pirates kept falling in. On 
        the fourth day of digging, they unearthed a treasure chest full of gold, jewels, and an 
        aged hat. The island had four times as many holes by then as it did at the end of the first 
        day. How many holes did the pirates dig on the fourth day before finding the treasure?
      </td>
    </tr>
    <tr>
      <td align="center">6</td>
      <td>
        Tatiana is deciding how much of her weekend she wants to spend playing soccer. She has 7 
        hours on Saturday and 5 hours on Sunday. She is dividing her time between soccer, video 
        games, and reading. If she reads for 3 hours and plays video games for 1/3 of the remaining 
        time, what percentage of her weekend does she spend playing soccer?
      </td>
    </tr>
    <tr>
      <td align="center">7</td>
      <td>
        Janet buys a brooch for her daughter.  She pays $500 for the material to make it and then 
        another $800 for the jeweler to construct it.  After that, she pays 10% of that to get it 
        insured.  How much did she pay?
      </td>
    </tr>
    <tr>
      <td align="center" style="white-space: normal;">8</td>
      <td>
        A local gas station is selling gas for $3.00 a gallon.  An app company is offering $.20 
        cashback per gallon if you fill up at this station.  If someone buys 10 gallons of gas, how 
        much with their gas be, after the cashback rewards?
      </td>
    </tr>
    <tr>
      <td align="center">9</td>
      <td>
        Nik has 200 crayons. He wants to separate them into groups of 8 and put them into boxes.  
        Each box weighs 8 ounces. Each crayon weighs 1 ounce. If he puts all of his crayons into 
        boxes, what is the total weight, in pounds, of the crayons and the boxes, when there are 16 
        ounces to a pound?
      </td>
    </tr>
  </tbody>
</table>

<br>

# "Swap Out" question

<table>
  <thead>
    <tr>
      <th style="text-align:center">#</th>
      <th>Problem</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">1</td>
      <td>
        Calvin is making soup for his family for dinner. He has a pot with enough soup to fill 
        four adult's bowls or eight child's bowls. He is an adult and will be eating with his adult 
        wife and their two children. If everyone eats one bowl at a meal, how many times will each 
        child be able to have a bowl of soup for lunch from the leftover soup?
      </td>
    </tr>
  </tbody>
</table>

<br>

# "Both Wrong" questions

<table>
  <thead>
    <tr>
      <th style="text-align:center">#</th>
      <th>Problem</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">1</td>
      <td>
        Ava and Emma want to know who is better at the new video game Ava got for her birthday. 
        They are each going to play one level and whoever has the highest score wins. They receive 
        10 points for every enemy they jump on, 5 points for each berry they collect, and 30 points 
        for every second left on the timer when they finish the level. If Ava jumps on 8 more 
        enemies than Emma and collects 3 more berries, but finishes the level 4 seconds slower, 
        what is the difference between their two scores?
      </td>
    </tr>
    <tr>
      <td align="center">2</td>
      <td>
        Fishio posted her selfie on Instagram. She received 2000 likes on the photo after 1 week. 
        Three weeks later, the number of likes was 70 times as many as the initial number of likes. 
        If she received 20000 more new likes recently, how many Instagram likes are there?
      </td>
    </tr>
    <tr>
      <td align="center">3</td>
      <td>
        An interior design firm offers installation for $129.00.  It includes hanging 4 mirrors, 2 
        shelves, 1 chandelier, and 10 pictures.  They will install additional items for an extra 
        $15.00 per item.  Angela has 6 mirrors and 2 chandeliers and 20 pictures that she needs 
        installed/hung.  How much will this cost her?
      </td>
    </tr>
    <tr>
      <td align="center">4</td>
      <td>
        Debra is monitoring a beehive to see how many bees come and go in a day. She sees 30 bees
        leave the hive in the first 6 hours, and then she sees 1/2 that many bees return in the 
        next 6 hours. She sees two times as many bees as she saw first leave the hive fly from the 
        hive and leave in the next 6 hours. Then every bee that left before that hadn't already 
        returned returns to the hive in the next 6 hours. How many bees did Debra see return to the 
        hive in the last 6 hours of the day?
      </td>
    </tr>
    <tr>
      <td align="center">5</td>
      <td>
      Chase and Rider can ride their bikes thrice a day for 5 days; but on two other days, they 
      ride twice the times they do on usual days. How many times do they ride their bikes a week?
      </td>
    </tr>
    <tr>
      <td align="center">6</td>
      <td>
        Carolyn works for a delivery service company that hires on a contract basis. In May, they 
        hired 40 employees, paying each employee $15 per hour for a 40-hour workweek. In June, 1/4 
        of the employees' contracts expired. Calculate the total amount of money the company paid 
        to the employees in the two months.
      </td>
    </tr>
    <tr>
      <td align="center">7</td>
      <td>
        A new arcade opens up and Jack decides to play with his 3 friends.  Jack can play a game 
        with 1 quarter for 20 minutes.  Two of his friends are significantly worse than him and 
        can only play half as long.  One of them is significantly better and can play for 1.5 times 
        as long.  They play for 4 hours.  How much money is used?
      </td>
    </tr>
    <tr>
      <td align="center">8</td>
      <td>
        After scoring 14 points, Erin now has three times more points than Sara, who scored 8. How 
        many points did Erin have before?
      </td>
    </tr>
    <tr>
      <td align="center">9</td>
      <td>
        Jason was told he could earn $3.00 for doing his laundry,  $1.50 for cleaning his room, 
        $0.75 for taking the trash to the curb each week and $0.50 for emptying the dishwasher.  
        In a two week period, Jason emptied the dishwasher 6 times, did his laundry once, took the 
        trash out twice and cleaned his room once.  How much money did Jason earn? 
      </td>
    </tr>
    <tr>
      <td align="center">10</td>
      <td>
        90 single use contacts come in 1 box and will last Pete 45 days.  Each box is $100.00 and 
        currently 10% off.  If he buys 2 boxes of contact, how much will each pair of contacts 
        cost?
      </td>
    </tr>
  </tbody>
</table>
