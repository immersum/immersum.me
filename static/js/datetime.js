{
  const lang = document.currentScript.lang;
  const dateOptions = {
    year: "numeric",
    month: "long",
    day: "numeric",
  };
  const timeOptions = {
    hour: "numeric",
    minute: "numeric",
  };

  function commentDateTime(datetime) {
    const date = new Date(Date.parse(datetime));
    const dateString = date.toLocaleString(lang, dateOptions);
    const timeString = date.toLocaleString(lang, timeOptions);
    document.write(`${dateString} ${lang === "en" ? "at" : "–"} ${timeString}`);
  }
}
