/* ==========================================================================
   Kopi Rakyat — main.js
   Interaksi: menu mobile, scroll-spy, tombol ke atas, animasi muncul,
   dan validasi formulir kontak.
   ========================================================================== */

(function () {
  "use strict";

  /** Ganti nomor ini saat dipakai untuk klien lain (format internasional). */
  const WHATSAPP_NUMBER = "6281234567890";

  // ---------------------------------------------------------------------
  // Menu mobile
  // ---------------------------------------------------------------------
  function initMobileMenu() {
    const toggle = document.querySelector(".nav__toggle");
    const menu = document.getElementById("menu-utama");
    if (!toggle || !menu) return;

    function close() {
      menu.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Buka menu navigasi");
    }

    toggle.addEventListener("click", function () {
      const isOpen = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(isOpen));
      toggle.setAttribute("aria-label", isOpen ? "Tutup menu navigasi" : "Buka menu navigasi");
    });

    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", close);
    });
  }

  // ---------------------------------------------------------------------
  // Scroll-spy: tandai tautan sesuai bagian yang terlihat
  // ---------------------------------------------------------------------
  function initScrollSpy() {
    const links = Array.from(document.querySelectorAll(".nav__link"));
    const sections = links
      .map(function (link) {
        const id = link.getAttribute("href").replace("#", "");
        return document.getElementById(id);
      })
      .filter(Boolean);

    if (!sections.length) return;

    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          links.forEach(function (link) {
            const match = link.getAttribute("href") === "#" + entry.target.id;
            link.classList.toggle("is-active", match);
          });
        });
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0 }
    );

    sections.forEach(function (section) {
      observer.observe(section);
    });
  }

  // ---------------------------------------------------------------------
  // Tombol kembali ke atas
  // ---------------------------------------------------------------------
  function initToTop() {
    const button = document.getElementById("to-top");
    if (!button) return;

    function onScroll() {
      button.hidden = window.scrollY < 400;
    }

    button.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // ---------------------------------------------------------------------
  // Animasi muncul saat menggulir
  // ---------------------------------------------------------------------
  function initReveal() {
    const items = document.querySelectorAll("[data-reveal]");
    if (!items.length) return;

    if (!("IntersectionObserver" in window)) {
      items.forEach(function (item) {
        item.classList.add("is-visible");
      });
      return;
    }

    const observer = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            obs.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );

    items.forEach(function (item) {
      observer.observe(item);
    });
  }

  // ---------------------------------------------------------------------
  // Validasi formulir kontak
  // ---------------------------------------------------------------------
  const RULES = {
    nama: function (value) {
      return value.trim().length >= 2;
    },
    telepon: function (value) {
      const digits = value.replace(/\D/g, "");
      return digits.length >= 8;
    },
    pesan: function (value) {
      return value.trim().length >= 5;
    },
  };

  function showError(field, show) {
    const message = document.querySelector('[data-error-for="' + field.name + '"]');
    field.classList.toggle("is-invalid", show);
    if (message) message.hidden = !show;
  }

  function initContactForm() {
    const form = document.getElementById("form-kontak");
    if (!form) return;

    const status = document.getElementById("status-form");

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      let valid = true;

      Object.keys(RULES).forEach(function (name) {
        const field = form.elements[name];
        if (!field) return;
        const ok = RULES[name](field.value);
        showError(field, !ok);
        if (!ok) valid = false;
      });

      if (!valid) {
        if (status) {
          status.textContent = "Mohon periksa kembali isian yang masih salah.";
          status.className = "contact-form__status is-error";
        }
        return;
      }

      // Di produksi, kirim ke backend atau arahkan ke WhatsApp.
      const nama = form.elements.nama.value.trim();
      const pesan = form.elements.pesan.value.trim();
      const teks = "Halo, saya " + nama + ". " + pesan;
      const url =
        "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(teks);

      if (status) {
        status.textContent = "Terima kasih, " + nama + "! Mengarahkan ke WhatsApp...";
        status.className = "contact-form__status is-success";
      }

      window.open(url, "_blank", "noopener");
      form.reset();
    });

    // Hapus tanda error begitu pengguna mengetik.
    Object.keys(RULES).forEach(function (name) {
      const field = form.elements[name];
      if (!field) return;
      field.addEventListener("input", function () {
        if (RULES[name](field.value)) showError(field, false);
      });
    });
  }

  // ---------------------------------------------------------------------
  // Inisialisasi
  // ---------------------------------------------------------------------
  document.addEventListener("DOMContentLoaded", function () {
    initMobileMenu();
    initScrollSpy();
    initToTop();
    initReveal();
    initContactForm();
  });

  // Diekspor untuk memudahkan pengujian di lingkungan non-browser.
  if (typeof module !== "undefined" && module.exports) {
    module.exports = { WHATSAPP_NUMBER: WHATSAPP_NUMBER, RULES: RULES };
  }
})();