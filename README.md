# Toll fee calculator

A calculator for vehicle toll fees! 🚗💻💰

## Background

Our city has decided to implement toll fees in order to reduce traffic
congestion during rush hours.

This is the current draft of requirements:

- Fees will differ between 9 SEK and 22 SEK, depending on the time of day.
- The maximum fee for one day is 60 SEK.
- Only the highest fee should be charged for multiple passages within a 60
  minute period.
- Some vehicle types are fee-free.
- Fee-free days are; Saturdays, Sundays, holidays and day before holidays and
  the whole month of July. See [Transportstyrelsen][] for details.

## Your main assignment

The last city-developer quit recently, claiming that this solution is
production-ready. You are now the new developer for our city - congratulations!

Your job is to deliver the code and from now on, you are the responsible
go-to-person for this solution. This is a solution you will have to put your
name on.

## Instructions

1.  Choose one of language alternatives available.
2.  Modify and re-factor the code as you see fit.
3.  Deliver your solution by e-mail or another suitable way.

## Optional assignments
The assignments below are optional and can be done if you feel like it and if you can spare some extra time. If you 
choose to do one of the below optional assignments, we would like to see your solution for the main assignment first.
However, feel fre to slim down the functionality of the main assignment as you see fit if you rather would like to 
specifically focus on one of the optional assignments more.

### *The Toll Fee Calculator Web UI* ✨
> ℹ️ **Optional**

The mentioned that they had been working on an awesome UI where the *city traffic control manager*
easily could add passages manually and calculate costs. We thought that was great, until we tried it out... This was
promised to be production ready, but we feel something is fishy as the *manager* got furious using it!

- Fix the application 🛠️
- Allow adding multiple passages 🚗 🏎️ 🏍️
- Show total cost using your great logic from main assignment 💰
- Tidy up the UI ✨

### *The Toll Fee Calculator API* 📑
> ℹ️ **Optional**

The developer also mentioned that they had been working on an awesome API where the *city traffic control UX department*
easily could check for costs for passages. They got excited, until they tried it out... This was
also promised to be production ready, but we feel something is odd as the *UX people* got mad calling the endpoints!

- Fix the API 👷‍👷
- Allow checking costs for passages according to the OpenAPI spec 🧮
- Use your awesome logic from the main assignment! 📈

## Help, I don't know Go, C, C#, Python, Java or Java-/TypeScript?!

No worries! We accept submissions in other languages as well, why not try it in
[Rust][] or [Kotlin][]?

[transportstyrelsen]: https://transportstyrelsen.se/sv/vagtrafik/Trangselskatt/Trangselskatt-i-goteborg/Tider-och-belopp-i-Goteborg/ "Trängselskatt i Göteborg - Transportstyrelsen"
[rust]: https://www.rust-lang.org/
[kotlin]: https://kotlinlang.org
