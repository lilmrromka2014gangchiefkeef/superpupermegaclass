from aiogram import types
from aiogram.types import ContentType

from misc import dp

from keyboards import main_kb, history_kb, back_kb


# Реакция на команду /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Привет, я petersbot, я путеводитель и могу рассказать о городе Петербург, его историю ,его достопримечательности и создать оптимальный маршрут для туристов', reply_markup=main_kb)


# Реакция на команду /help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer('Навигация по боту')


# Ответ на текст история Санкт-петербурга
@dp.message_handler(text='История Санкт-петербурга')
async def lisa(message: types.Message):
    print('history_saint_petersburg')
    await message.answer('Выбери по своему желанию:', reply_markup=history_kb)

# Ответ на текст Краткая история
@dp.message_handler(text='Краткая история')
async def lisa(message: types.Message):
    print('Small_saintpetersburg')
    await message.answer('Этот текст был взят с сайта "https://www.sdamna5.ru/istoriya_peterburga_kratko". Приятного чтения!!! По мнению многих, Санкт-Петербург начался с Невы и на это есть причины. На самом деле, Нева стала идеальным местом для строительства оборонительной цитадели, которую возвел Петр I в ходе Северной войны. Официальной датой основания города считается 1703 год, хотя окрестности современного Санкт-Петербурга были заселены еще с доисторических времен. Сначала это были палеоевропейские племена, затем индоевропейские. Немного позже обозначился наплыв прибалтийско-финских народностей, и только с VIII по IX век на берегах Невы появились славяне.Территорию, где позднее появился Санкт-Петербург, контролировала Новгородская Русь. К концу XV века в дельте Невы было полно деревень и небольших поселений. В 1478 году Новгородское княжество было присоединено к Московскому. В XVI веке шведы вновь попытались завоевать устье Невы, но безрезультатно. В 1611 году Швеции все же удалось заполучить некоторые земли на северо-западе Руси и возвести там крепость Ниеншанц. В ходе Северной войны эта крепость была взята русскими.Именно в этот период Петр I, основательно изучив Приневье, выбрал место для строительства Заячьего острова. На этом острове в 1703 году была заложена Петропавловская крепость. Название крепости и будущего города было, в первую очередь, связано с апостолом Петром и небесным покровителем царя. В сентябре того же года в молодой город прибыл первый торговый корабль. Работы по строительству велись, в основном, иностранными инженерами, специально приглашенными в Россию Петром I.В 1712 году столица государства была перенесена из Москвы в Санкт-Петербург. Вместе с тем переехал и царский двор со всеми официальными учреждениями. Во время правления Петра I ­в городе были возведены такие выдающиеся достопримечательности, как Невская лавра, Кунсткамера, Гостиный двор, Петербургская Академия наук, Большой Петергофский дворец и т.д. После смерти Петра I в царской России было немало правителей, каждый из которых оставлял свой след в развитии города.Так, например, во время правления Елизаветы Петровны население города увеличилось до 74 тысяч человек. Тогда же началось строительство Зимнего дворца, а местом летнего отдыха монархии стал Петергоф. Во время правления Екатерины II летняя резиденция была перенесена в Царское Село. В этот же период были открыты Эрмитаж и Публичная библиотека. В XIX век Санкт-Петербург достиг особого расцвета. Это не только «золотой век» столицы, но и время, когда творили Пушкин, Баратынский, Росси.Вместе с тем, это период войны с Наполеоном, восстания декабристов и отмены крепостного права. Определенный след в Санкт-Петербурге оставила династия Романовых. Во время правления Александра I состоялась победа над французской армией. Александру II удалось подавить восстание, призванное свергнуть самодержавие. После его смерти в 1881 году трон перешел к Александру III, а затем к Николаю II - последнему царю России. После Февральской революции 1917 года Николай II был вынужден отречься от престола. Вскоре он и его семья были расстреляны, а власть перешла в руки Временного правительства. В 1918 году столица государства была перенесена в Москву.В этот же период Санкт-Петербург был переименован в Петроград, а после смерти В. И, Ленина - в Ленинград. В ходе Второй мировой войны население города пережило Ленинградскую блокаду (1941-1944) - событие, унесшее жизни более 700 тыс. человек. В послевоенные годы Ленинград полностью восстанавливался от разрушений, наступивших в ходе бомбежек и обстрелов. К 1980 году население уже составляло 5 млн. человек. В 1991 году городу вновь было возвращено его историческое название.',reply_markup=main_kb)

# Ответ на тексть полная история
@dp.message_handler(text='Полная история')
async def lisa(message: types.Message):
    print('history_saint_petersburg full')
    await message.answer('Этот текст был взят с сайта "https://101hotels.com/recreation/russia/sankt-peterburg/history" Приятного чтения!!! История Санкт-Петербурга началась в 1703 году – именно тогда, 27 мая, Пётр Первый основал будущую Северную Столицу на землях, отвоёванных у Швеции. Назван город в честь апостола Петра.Первой питерской постройкой стала Петропавловская крепость, заложенная на Заячьем острове. Территория современного Петербурга была сильно заболоченной, для строительства болота осушались. Географическое расположение города послужило причиной того, что в истории Санкт-Петербурга неоднократно случались наводнения, которые приводили к значительным жертвам и разрушениям. Самое сильное наводнение было зафиксировано в ноябре 1824 года (уровень воды поднялся на 4 метра 21 сантиметр), также сильные наводнения происходили в восемнадцатом веке (1724 и 1777 годы) и в двадцатом веке (1924 год).Для того, чтобы быстрее строились каменные дома, Пётр Первый ввёл каменный налог – каждому приезжему необходимо было сдать на въезде в город какое-то количество камня или равноценную сумму денег.В 1712 году в истории Санкт-Петербурга произошло событие, которое сыграло решающую роль в его дальнейшем развитии – Питер стал столицей России вместо Москвы. Самое интересное, что официального указа о переносе столицы из Москвы в Санкт-Петербург так и не было издано – в Питер просто был переведён весь царский двор и официальные ведомства. Столичным статусом Санкт-Петербург обладал до 1918 года.В 1719 году в Санкт-Петербурге был открыт первый музей, в который мог попасть любой желающий – Кунсткамера.В 1724 году была создана Петербургская Академия Наук. В 1825 году на Сенатской площади Санкт-Петербурга произошло восстание декабристов. В 1837 году именно в Петербурге была открыта первая в России железная дорога. В связи с тем, что на заработки в Санкт-Петербург приезжало очень большое количество крестьян, размеры города и численность его населения сильно увеличились, и к концу девятнадцатого века Питер стал одним из крупнейших промышленных городов не только России, но и Европы.В 1905 году в Санкт-Петербурге началась первая русская социалистическая революция. В 1907 году на главную улицу Санкт-Петербурга выехал первый автобус, называвшийся тогда омнибус-мотором. В 1914 году Николай Второй переименовал Санкт-Петербург в Петроград, так как на фоне шедшей в это время Первой мировой войны все названия, носящие оттенок «неметчины» вызывали резко негативную реакцию.В 1917 году обе революции – февральская и октябрьская – также брали своё начало в Санкт-Петербурге, хотя, в итоге, после революций и прихода советской власти, этот город перестал быть российской столицей.Это случилось потому, что политический климат Санкт-Петербурга, так же, как и его природный климат, оказался очень нестабильным. Вначале переезд нового правительства виделся как временная мера, но – факт остаётся фактом – именно с тех пор Москва вновь стала и остаётся до сих пор столицей России. В 1924 году Петроград был переименован в Ленинград.С 8 сентября 1941 до 27 января 1944 года продолжалась блокада Ленинграда, во время которой город с остальной страной связывала лишь Дорога Жизни, которая проходила через Ладожское озеро. Из-за постоянных бомбёжек до города добирался лишь каждый третий грузовик. Жертвами блокады стали около восьмисот тысяч ленинградцев.После снятия блокады Ленинград первым среди русских городов был удостоен звания Города-Героя. В послевоенные годы происходило активное восстановление Ленинграда.Историческое название – Санкт-Петербург – было возвращено городу в сентябре 1991 года. В настоящее время Санкт-Петербург носит негласный статус Культурной столицы России, что вполне обоснованно – тридцать шесть культурно-исторических комплексов Питера включены в список исторического наследия ЮНЕСКО, в городе постоянно функционируют более двухсот музеев, двух тысяч библиотек, восемьдесят театров и множество других учреждений культуры.',reply_markup=main_kb)

# Ответ на любой текст, кроме хендлеров выше
@dp.message_handler()
async def echo(message: types.Message):
    print(message.from_user.username, message.date, '\nMessageID:', message.message_id, 'Message text:', message.text, '\nChatID:', message.chat.id, 'UserID:', message.from_user.id)
    await message.answer(message.text)


# Ответ на любой контент, кроме того, что выше
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    await message.reply('Я не знаю, что с этим делать. Если что-то непонятно, есть команда /help' )